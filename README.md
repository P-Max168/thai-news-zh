# 泰国新闻速览 (zh.pmaxone.com)

태국 뉴스 한눈에(tnews.pmaxone.com, P-Max168/thai-news-kr)의 중국어판. **시스템은 공유, 편집 기준은 언어별 분리**(Mingoo 2026-10-17 결정).

- 공유 코드(index.html·assets/·tools/ 등)는 한국판 커밋에서 `tools/dev/sync_core.sh <ko커밋> <이 저장소>` 로만 가져온다. 여기서 직접 고치지 않는다(`.core-version` 에 기준 커밋).
- 이 저장소 전용(동기화가 건드리지 않음): `site/LANG`(=zh)·`site/zh.json`·`site/topics.zh.json`·`i18n/zh.json`·`tools/sources.zh.json`·`tools/fetch_china.py`·`tools/TRANSLATION_RULES.zh.md`·`tools/DISCUSSION_PERSONA.zh.md`·`data/`·`ads/`·`CNAME`·`robots.txt`·`.github/`.
- 판: 하루 1번 점심판(md, 13:00 BKK). 금지 구간(push 안 함): 07:00–08:10·18:00–18:40 BKK(한국판 빌드), 13:00–13:40(zh 빌드).
- 화폐: `1,234泰铢（约247元）` (THB_CNY, tools/fetch_ticker.py). 헤더 숫자 칸만 ฿.
- Firestore: 같은 프로젝트, `zh_` 접두사 컬렉션, 운영자 문서 `config/admins_zh`.
- 광고: `data/ads.json` enabled:false — 드래곤 중국어 문구 Mingoo 확인 뒤 켬.
- 숨긴 코너: places·rentals·jobs (site/zh.json hidden_sections).

공개 전 남은 승인(Mingoo): GitHub 저장소 P-Max168/thai-news-zh 생성 + Pages, Cloudflare `zh` CNAME → p-max168.github.io(DNS only), Firebase 규칙 게시 + Auth 승인 도메인 zh.pmaxone.com + config/admins_zh 문서.
