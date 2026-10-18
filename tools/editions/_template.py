# -*- coding: utf-8 -*-
"""중국어판(zh) 판 편집 파일 템플릿 — 2026-10-18 Grok. 편집 기준은 zh 전용(시스템 공유·편집 기준 분리).
준비: bash tools/lang_build.sh prep   → tools/editions/<YYYY-MM-DD>-md.py 가 이 파일 복사본으로 생김 → ※ 부분을 실제 내용으로 교체
실행: bash tools/lang_build.sh build <id>   (= python3 tools/build_data.py tools/editions/<id>.py + 화면 점검)
※ 이 템플릿 자체는 id 가 'YYYY-MM-DD-md' 라 실행해도 검증에서 멈춘다(가짜 판 방지).
※ 뉴스·인용·숫자·URL·시각은 원문에서 확인한 것만. 절대 지어내지 않는다. 글은 간체 중국어(TRANSLATION_RULES.zh.md) — 한글·태국 문자 금지(검증이 막음).
※ 금액: 바트 금액마다 '350泰铢（约70元）' — 이 판 fx.THB_CNY 하나로 환산·정수 반올림(검증이 막음). ฿ 기호는 본문에 쓰지 않음.

주제 id(site/topics.zh.json, topic = 주 주제 1개, secondary = 보조 0~3개):
  cn 涉华·中国人(中国游客·在泰华人·中泰关系·使馆提醒)  visa 签证·移民  bangkok 曼谷  east 东部(芭提雅·罗勇)  north 北部  south 南部
  poleco 政经·汇率  society 社会·治安  life 生活·物价  travel 旅游·美食  weather 天气·交通  ent 娱乐·体育
impact(0~3개, site/zh.json impacts): 签证·居留 / 汇率·物价 / 交通·事故 / 治安 / 天气·灾害
기사 id: 주제 약어+번호(cn1 vi1 bk1 ea1 no1 st1 pe1 so1 lf1 tr1 wt1 en1). tags 2~6개 필수.
"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from newslib import write_edition, B, KR

stories = [
dict(id="cn1", topic="cn", secondary=["east"], region="芭提雅",   # ※ 예시 — 실제 기사로 교체
 headline="※ 中文标题（简体，不超过40字）",
 summary=["※ 第1段（只写原文确认的内容）", "※ 第2段"],
 context="※ 💡 背景（可选）——给在泰华人/中国游客的实用提示，不确定的规定写“建议核实”",
 # update="※ 只有后续报道时：上期之后的新进展",
 source="※ 媒体名（中文/原名）", url="https://※原文URL",
 title_th="※ 原文标题（泰文/英文/中文）",
 published="2026-01-01T12:00:00+07:00",   # ※ 原文发布时间(+07:00)
 related=[], tags=["※关键词1", "※关键词2", "※关键词3"],
 impact=[],                                # 签证·居留 / 汇率·物价 / 交通·事故 / 治安 / 天气·灾害 中 0~3 个
 for_me="※ 对在泰华人·中国游客意味着什么（一句，只写事实）。没有就 \"\"",
 also=[], issue=None,
 quick_replies=["※ 有人知道吗？", "※ 简短反应", "※ 求经验"]),
]

# 简报 5~6 行: B(主题, "一句话 + **加粗关键词/数字**", 文章id)。每行不同文章。
briefing = [
  B("cn", "※ **关键词** 一句话摘要", "cn1"),
]

# 🇨🇳 中国要闻(最多10条, 主页 data/china.json 过期时的备用): china.yml 每2小时自动更新，这里可留空 []。
china_top = []

_fx = pathlib.Path(__file__).resolve().parents[2] / "drafts" / "fx-YYYY-MM-DD-md.json"   # ※ lang_build prep 가 받은 환율(파일 이름의 날짜를 이 판 id 로)
fx = json.loads(_fx.read_text()) if _fx.exists() else dict(THB_CNY=0.0, source="※", note="※")

data = dict(
  id="YYYY-MM-DD-md", date="YYYY-MM-DD", edition="md", edition_label="午间版",   # ※ 실행한 날(방콕) + md(시험 기간 13:00 하루 1판)
  weekday="※星期几", timezone="Asia/Bangkok (UTC+7)",
  coverage="※ 收集范围说明（例：前一天13:00之后～今天12:30）",
  previous="※ 上一期 id（data/index.json 的 latest，第一期写 \"\"）",
  briefing=briefing,
  highlights=["cn1", "※", "※"],   # 要闻3条（文章id）
  stories=stories, china_top=china_top, fx=fx)

if __name__ == "__main__":
    write_edition(data)
