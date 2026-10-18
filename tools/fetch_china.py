# -*- coding: utf-8 -*-
"""'🇨🇳 中国要闻' 칸 수집기 — 중국어판(zh) 전용. 한국판 tools/fetch_korea.py --standalone 과 같은 구조(공유 시스템 패턴).

원칙(Mingoo 2026-10-17 18:33 BKK): 시스템(코드·도구·자동화)은 공유, 편집 기준은 언어별로 분리.
  → 이 스크립트의 '구조'(수집→정리→점수→data/<home>.json+.js, 바뀐 게 없으면 안 씀)는 한국판과 같고,
    '무엇을 고르나'(매체·가중치·제외 목록)는 tools/sources.zh.json 에서만 읽는다(코드에 매체를 박지 않음).
    Claude 가 나중에 fetch_home.py(언어 공통) 로 합칠 때 이 파일의 점수 규칙을 site/zh.json 설정으로 옮기면 된다.

  python3 tools/fetch_china.py --standalone [--force] [--out DIR] [--dry]
    → DIR/data/china.json + china.js(window.CHINA_NEWS) — LLM 없음, 결정적. 같은 입력 → 같은 결과.
    항목 10건이 이전과 같고 updated_at 이 5시간 안이면 파일을 건드리지 않음(커밋 안 생김). --force 면 항상 씀.

고르는 규칙(독립 모드):
  - 최근 36시간 기사만. 칼럼·评论·图片·视频·直播·广告 류와 연예 가십 제목은 뺀다.
  - 같은 사건(제목 글자 2-gram 유사도 ≥0.5)은 하나로 묶고, 묶음 대표는 weight 가 가장 큰 매체.
  - 점수 = 대표 매체 weight×3 + 묶음 매체 수(≤5)×4 + (Google 新闻 화제 피드에 있으면 +8) − 경과시간×0.6
  - 한 매체가 4건을 넘지 않게(다양성). 화면에 보이는 매체 이름은 sources.zh.json 의 name.
"""
import sys, re, json, pathlib, argparse, urllib.request, xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime
from datetime import datetime, timezone, timedelta

HERE = pathlib.Path(__file__).resolve().parent
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36"}
BKK = timezone(timedelta(hours=7))
CST = timezone(timedelta(hours=8))
MAX_AGE_H = 36
SKIP_TITLE = re.compile(r"[【\[]\s*(评论|社论|图片|组图|视频|直播|专题|广告|快讯合集|早报|晚报|新闻联播)\s*[】\]]|^\s*(视频|图集|直播)[｜|:：]|"
                        r"^(好评中国|人民锐评|新华时评|央视快评|国际锐评|钟声|和音|任仲平)[｜|:：]|评论员|(八卦|恋情|绯闻|网红|明星同款|彩票|开奖)")
GN_SUFFIX = re.compile(r"\s+-\s+[^-]{1,30}$")


def fetch(url, timeout=25):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout).read()


def clean(t):
    t = re.sub(r"\s+", " ", (t or "")).strip()
    return t


def parse_rss(data, src, gnews=False):
    out = []
    for it in ET.fromstring(data).iter("item"):
        t = clean(it.findtext("title"))
        pub = it.findtext("pubDate")
        if not t or not pub:
            continue
        outlet = clean(it.findtext("source")) if gnews else src["name"]
        if gnews:
            t = GN_SUFFIX.sub("", t) if outlet and t.endswith(outlet) else t
        try:
            d = parsedate_to_datetime(pub)
        except Exception:
            continue
        if d.tzinfo is None:
            d = d.replace(tzinfo=CST)
        out.append(dict(title=t, url=clean(it.findtext("link")), outlet=outlet or src["name"], published=d.astimezone(BKK)))
    return out


def parse_cctv(data, src):
    txt = data.decode("utf-8", "replace")
    j = json.loads(txt[txt.index("(") + 1: txt.rindex(")")])
    out = []
    for x in j["data"]["list"][:120]:
        try:
            d = datetime.strptime(x["focus_date"], "%Y-%m-%d %H:%M:%S").replace(tzinfo=CST)
        except Exception:
            continue
        out.append(dict(title=clean(x.get("title")), url=x.get("url", ""), outlet=src["name"], published=d.astimezone(BKK)))
    return out


def parse_sina(data, src):
    j = json.loads(data.decode("utf-8", "replace"))
    out = []
    for x in j["result"]["data"]:
        try:
            d = datetime.fromtimestamp(int(x["ctime"]), CST)
        except Exception:
            continue
        out.append(dict(title=clean(x.get("title")), url=x.get("url", ""), outlet=src["name"], published=d.astimezone(BKK)))
    return out


def gather(cfg, log):
    allx, signal = [], []
    for src in cfg["sources"] + cfg.get("fallback", []):
        try:
            data = fetch(src["url"])
            ty = src["type"]
            xs = parse_cctv(data, src) if ty == "cctv_jsonp" else parse_sina(data, src) if ty == "sina_roll" \
                else parse_rss(data, src, gnews=(ty == "gnews"))
            log.append("%-18s OK %3d" % (src["id"], len(xs)))
        except Exception as e:  # 한 곳이 깨져도 나머지로 만든다
            log.append("%-18s FAIL %s" % (src["id"], type(e).__name__)); continue
        for x in xs:
            x["weight"] = src.get("weight", 5); x["src"] = src["id"]
        (signal if src.get("role") else allx).extend(xs)
    return allx, signal


def bigrams(t):
    t = re.sub(r"[\s\W_]+", "", t)
    return {t[i:i + 2] for i in range(len(t) - 1)}


def sim(a, b):
    A, B = bigrams(a), bigrams(b)
    return len(A & B) / max(1, min(len(A), len(B)))


def pick(items, signal, now, n=10, per_outlet=4):
    fresh = [x for x in items if timedelta(0) <= now - x["published"] <= timedelta(hours=MAX_AGE_H)
             and len(x["title"]) >= 8 and not SKIP_TITLE.search(x["title"])]
    fresh.sort(key=lambda x: (-x["weight"], -x["published"].timestamp(), x["title"]))
    groups = []
    for x in fresh:
        for g in groups:
            if sim(g[0]["title"], x["title"]) >= 0.5:
                g.append(x); break
        else:
            groups.append([x])
    scored = []
    for g in groups:
        head = g[0]
        outlets = {y["outlet"] for y in g}
        hot = any(sim(head["title"], s["title"]) >= 0.5 for s in signal)
        age = (now - head["published"]).total_seconds() / 3600
        score = head["weight"] * 3 + min(5, len(outlets)) * 4 + (8 if hot else 0) - age * 0.6
        scored.append((round(score, 3), head, len(outlets), hot))
    scored.sort(key=lambda s: (-s[0], s[1]["title"]))
    out, cnt = [], {}
    for score, h, k, hot in scored:
        if cnt.get(h["outlet"], 0) >= per_outlet:
            continue
        cnt[h["outlet"]] = cnt.get(h["outlet"], 0) + 1
        out.append(dict(headline=h["title"], source=h["outlet"], url=h["url"],
                        published=h["published"].isoformat(timespec="seconds"), outlets=k, hot=hot, score=score))
        if len(out) >= n:
            break
    return out


def standalone(a):
    cfg = json.loads((HERE / "sources.zh.json").read_text(encoding="utf-8"))["china_news"]
    now = datetime.now(BKK)
    log = []
    items, signal = gather(cfg, log)
    print("\n".join(log))
    top = pick(items, signal, now)
    if len(top) < 5:
        print("후보가 %d건뿐 — 파일을 바꾸지 않음(이전 것 유지)" % len(top)); sys.exit(2)
    outdir = pathlib.Path(a.out) / "data"; outdir.mkdir(parents=True, exist_ok=True)
    jf, js = outdir / "china.json", outdir / "china.js"
    if jf.exists() and not a.force:
        try:
            old = json.loads(jf.read_text(encoding="utf-8"))
            same = [x["url"] for x in old["items"]] == [x["url"] for x in top]
            if same and now - datetime.fromisoformat(old["updated_at"]) < timedelta(hours=5):
                print("변경 없음 — china.json 그대로(updated_at %s)" % old["updated_at"]); return
        except Exception:
            pass
    doc = dict(updated_at=now.replace(microsecond=0).isoformat(), lang="zh-Hans", items=top)
    for i, x in enumerate(top, 1):
        print("%2d %5.1f [%s] %s  %s" % (i, x["score"], x["source"], x["headline"], x["published"][5:16]))
    if a.dry:
        return
    txt = json.dumps(doc, ensure_ascii=False, indent=1)
    jf.write_text(txt, encoding="utf-8")
    js.write_text("window.CHINA_NEWS = " + txt + ";\n", encoding="utf-8")
    print("저장:", jf, js, doc["updated_at"])


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--standalone", action="store_true")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--out", default=str(HERE.parent))
    a = ap.parse_args()
    if not a.standalone:
        print(__doc__); sys.exit(0)
    standalone(a)
