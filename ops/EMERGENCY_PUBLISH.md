# Claude 비상 발행 절차 — 중국어판 (thai-news-zh)

Claude 예약 작업이 이 문서를 그대로 따른다. 사람도 읽을 수 있게 짧게 쓴다.
시각은 `ops/SCHEDULE_3EDITION.md` 표의 Claude 비상 열과 같다(2026-10-28 맥스: 사이트별 표 시각 유지).
판 담당 표시: `tools/edition_claim.py`. 후보: 한국어판 `candidates` 브랜치.

## 0. 언제 무엇을 하나 (방콕 Asia/Bangkok)

| 방콕 시각 | 판 | 할 일 |
|---|---|---|
| **08:10** | am | 오늘 `YYYY-MM-DD-am` 이 main `data/index.json` latest(또는 dates)에 없으면 → 비상 발행(`take`) |
| **13:10** | md | 오늘 `YYYY-MM-DD-md` 이 없으면 → 비상 발행(`take`) |
| **19:10** | pm | 오늘 `YYYY-MM-DD-pm` 이 없으면 → 비상 발행(`take`) |

판이 이미 있으면 그 자리에서 끝낸다(토큰 쓰지 않음). 확인만 하고 끝난 실행은 기록도 남기지 않는다.

## 1. 확인 (판이 있는지)

- 판 id: `YYYY-MM-DD-am|md|pm` (방콕 날짜).
- 저장소: `git clone --depth 30 https://github.com/P-Max168/thai-news-zh` (또는 기존 클론에서 `git pull --rebase`).
- `python3 -c "import json;print(json.load(open('data/index.json'))['latest'])"` 가 오늘 해당 슬롯 판이면 끝.
- `python3 tools/edition_claim.py status <판 id>` 로 담당 표시 확인.

## 2. 이어받기 전 제미나이 확인

`gh run list -R P-Max168/thai-news-zh --workflow gemini-edition.yml -L 3 --json status,createdAt,displayTitle`  
오늘 이 판 회차에 queued·in_progress 실행이 있으면 take 하지 말고 1분 간격으로 최대 15분(Actions 대비 시각 07:45·12:45·18:45 기준) 기다렸다가 판이 나왔는지 다시 본다. 실행이 실패로 끝났거나 15분이 지나도 판이 없을 때만 take.

## 3. 비상 발행

1. 담당 표시: `python3 tools/edition_claim.py take claude <판 id>`. HOLD 면 끝.
2. 후보: 한국어판 `candidates` 브랜치 —  
   `git fetch https://github.com/P-Max168/thai-news-kr +candidates:refs/remotes/kr/candidates` 후  
   `mkdir -p drafts/candidates && git show kr/candidates:candidates/latest.md > drafts/candidates/latest.md`  
   (해당 슬롯 수집분이 있으면 그걸 쓴다. am≈07:20·md≈12:20·pm≈18:20 BKK).
3. 편집 기준: `tools/TRANSLATION_RULES.zh.md`·`ROUTINE_MD.md`(涉华·签证·治安 우선, 간체, 한글·태국 문자 금지, 금액 `350泰铢（约70元）` — 환율은 `data/ticker.json` 의 THB_CNY).
4. 편집 파일: `tools/editions/_template.py` 를 복사해 `tools/editions/<판 id>.py`. highlights 3개, briefing 4~7줄.
5. 빌드: `TNK_TEST=1 bash tools/lang_build.sh build <판 id>` 가 `BUILD OK` 가 될 때까지(또는 동일 검증 경로).
6. 배포: `TNK_PUBLISHER=claude TNK_LIVE_CHECK=pages bash tools/deploy.sh`.
7. 기록: 한국어판 저장소 `collab/STATUS.md` 에 한 줄 — `| 시각 | Claude | 비상 발행 zh <판 id> N건 | 이유: … |`. 커밋·push(`git pull --rebase` 후 일반 push, force 금지).

## 4. 하지 않는 것

- 질문·운영자 댓글 공개, 광고·검색·개인정보 설정 변경(맥스님 승인 필요).
- force push, 이번 판이 아닌 다른 판의 데이터 수정.
- 확인 못 한 사실 쓰기. 기사 수를 채우려고 약한 기사 넣기.
- CNAME·DNS·firestore.rules·robots·ads 설정 변경.

## 5. 실패하면

- 어느 단계에서 왜 멈췄는지 `collab/STATUS.md`(한국어판)에 한 줄 남기고 끝낸다(다음 확인 시각에 다시 본다).
