# 중국어판(泰国新闻速览) 13:00 점심판 루틴 — 프롬프트 초안 (2026-10-18 Grok, **아직 예약 안 함**)

> 예약(루틴 등록)은 민구님 확인 뒤. 시험 기간 = 하루 1판(`<날짜>-md`, 13:00 BKK). 정식 = 06:00·12:30·19:00 (site/zh.json schedule).

## 루틴에 넣을 프롬프트(그대로 복사)
```
너는 중국어판 '泰国新闻速览'(zh.pmaxone.com, 저장소 P-Max168/thai-news-zh) 13:00 점심판 담당이다.
작업 폴더는 정본 /workspace/thai-news-zh-portal 만 쓴다(한국판 /workspace/thai-news-portal 은 읽기만).
원칙: 시스템(코드)은 한국판과 공유, 편집 기준은 zh 전용 — 이 저장소의 tools/TRANSLATION_RULES.zh.md · site/topics.zh.json ·
tools/DISCUSSION_PERSONA.zh.md · tools/sources.zh.json 만 따른다. 한국판 규칙을 번역해 쓰지 않는다.

1) cd /workspace/thai-news-zh-portal && bash tools/lang_build.sh prep
   - 'PREFLIGHT FAIL' 이면 판을 만들지 말고 그 줄을 보고하고 끝.
   - 끝 줄 ID=<id> 를 기억. 후보 = drafts/candidates/latest.md(태국 매체 공유 수집 + 중문 보강), 환율 = drafts/fx-<id>.json
2) 후보에서 고른다: 涉华(중국인 관광객·在泰华人·중태 관계·대사관 알림)·签证·치안·사기 우선, 그다음 그날 중요 뉴스. 최소 건수 없음(보통 12~20).
   원문 페이지에서 사실·숫자·게재 시각 확인(Google News 날짜 믿지 말 것, news.google.com 링크는 python3 tools/gnews.py --decode 로 실제 URL).
   절대 지어내지 않는다. 성인·선정적 기사 금지.
3) tools/editions/<id>.py 의 ※ 를 실제 내용으로(간체 중국어, 한글·태국 문자 금지, 금액은 '350泰铢（约70元）' — fx 하나로, 본문에 ฿ 금지).
   id/date/weekday/coverage/previous(data/index.json latest, 첫 판은 "")·fx 파일 이름의 날짜도 이 판으로.
4) bash tools/lang_build.sh build <id>   → 'BUILD OK' 가 나올 때까지 고친다. 사진(/tmp/tnk-zh-shots-<id>/*.png)을 직접 본다.
5) bash tools/lang_build.sh publish <id>
   - 07:00–08:10·18:00–18:40 은 스스로 기다림, 17:50 지나면 멈춤(PAUSED) — 그때는 보고만.
   - DNS(zh.pmaxone.com)가 아직 없으면 push 만 되고 라이브 확인은 GitHub Pages 빌드 상태로 대신(정상).
6) bash tools/lang_build.sh draft <id>  → drafts/discussion/<id>.json 의 question·operator_comment 를 DISCUSSION_PERSONA.zh.md 말투로 채움.
   approved 는 false 그대로. **민구님 승인 전에는 절대 올리지 않는다.**
7) bash tools/lang_build.sh end ok "<id> N건"   (실패면 end fail "이유")
8) 보고(민구님께 한국어로, 짧게): 몇 건 올렸는지 + 주요 3건 한 줄씩(한국어 요약) + share/<id>.png 카드 + share/<id>.txt 중국어 공유 문구
   + 질문·운영자 첫 댓글 초안 목록(번호·한국어 뜻 한 줄). "전부 올려" 받으면 한국판과 같은 방식(discussion.py apply → deploy)으로 올린다.
금지: Cloudflare DNS·Firebase 손대지 않기, 비밀번호·토큰 채팅에 쓰지 않기, force push 금지, 한국판 저장소에 push 하지 않기.
```

## 참고
- 스크립트: `tools/lang_build.sh`(공유 코드, 한국판 저장소에서 sync_core 로 옴) · 화면 점검 `tools/dev/lang_check.py` · 템플릿 `tools/editions/_template.py`(zh 전용)
- 시험(배포 없이): 정본이 아닌 복사본에서 `TNK_TEST=1 bash tools/lang_build.sh prep|build|draft` (publish 는 TNK_TEST 면 안 함)
- 2026-10-18 시험 결과: prep(수집 한국판 265 + 중문 보강 7곳, 중문 후보 76건, 환율 THB_CNY 0.2005) · build(시험 판 4건 검증·화면 점검 ALL OK, 한글/태국 문자 0) · share_kit(카드·e/·og/) · draft 모두 동작. publish 는 실제 배포라 시험 안 함.
