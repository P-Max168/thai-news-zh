# -*- coding: utf-8 -*-
"""2026-10-27 午间版 — Claude 비상 발행(그록 담당 표시 후 제미나이 실행 실패 → take). 원문 확인한 7건."""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from newslib import write_edition, B, KR

stories = [
dict(id="cn1", topic="cn", secondary=["travel"], region="全国",
 headline="中国使馆提醒发布一周多，泰国酒店中国客预订仍偏弱",
 summary=[
  "中国驻泰国大使馆10月16日发布提醒，重点针对与边境地区有关的求职诈骗和绑架风险，提醒中国公民谨慎规划行程，不要乘坐陌生人安排的交通工具。提醒提到，有中国公民（包括网红和艺人）被高薪工作诱骗后被带往缅甸边境。",
  "据泰国酒店业人士介绍，中国客人预订明显偏弱：11月、12月的提前预订放缓，部分通过中国旅游平台预订的团队套餐被取消。曼谷、普吉、芭提雅的酒店经理都说中国旅行社态度谨慎；自由行客人仍在网上订房，团队游和包机产品更犹豫。",
  "泰国旅游与体育部部长苏拉萨（Surasak）表示，真正的游客没有这种风险，多数问题出在接受可疑工作邀请的人身上；外交部长西哈萨（Sihasak）请中方让提醒措辞保持适度。截至10月中旬，中国游客已超过414万人次，仍是泰国最大客源市场；泰国旅行社协会预计2026年全年为500万至550万人次。"
 ],
 context="💡 部分酒店已向客人提供旅游警察热线和持牌接送信息，并在抵达处增加会说中文的员工。来泰前核实工作邀请，不坐陌生人安排的车。",
 source="Chiang Rai Times（清莱时报）", url="https://www.chiangraitimes.com/business/china-warning-hotels-thailand/",
 title_th="China Tourist Travel Advisory Still Weighs on Thai Hotels",
 published="2026-10-27T09:55:00+07:00",
 related=[], tags=["中国使馆提醒", "中国游客", "酒店预订", "求职诈骗", "旅游业"],
 impact=["治安"],
 for_me="",
 also=[], issue=None,
 quick_replies=["正常旅游没问题吧？", "团队游确实少了", "高薪工作别轻信"]),

dict(id="cn2", topic="cn", secondary=["north", "society"], region="达府",
 headline="泰国高速公路警察截停轿车，4名非法入境中国男子被捕，原拟经湄索去缅甸",
 summary=[
  "泰国高速公路警察在达府—南邦方向的1号公路巡逻时，示意一辆高速行驶的轿车停车检查，车上有一名30岁泰国男司机和4名中国男子，4人都拿不出证件。",
  "据司机交代，这4名中国男子从老挝经清莱府的天然通道非法进入泰国，他受雇到南邦府一家商场接上4人，准备送到达府湄索（Mae Sot），再让他们越境前往缅甸妙瓦底（Myawaddy），每趟报酬6,000泰铢（约1,188元）。",
  "司机被控协助外国人非法入境并躲避抓捕，4名中国男子被控非法入境和居留，案件已移交达府班达（Ban Tak）警察局处理。"
 ],
 context="💡 妙瓦底一带是电诈园区集中地区。非法越境不仅违法，还可能落入犯罪团伙手中。",
 source="FM91（泰国交通广播电台）", url="https://fm91bkk.com/newsarticle/81019",
 title_th="ตำรวจทางหลวง สกัดจับเก๋งซิ่ง ลักลอบพา 4 ชาวจีนเข้าเมือง สอบปากคำคนขับรับสารภาพเตรียมนำไปส่งที่แม่สอด แลกกับค่าจ้าง 6 พันบาท",
 published="2026-10-26T21:23:00+07:00",
 related=[], tags=["非法入境", "中国公民", "湄索", "妙瓦底", "高速公路警察"],
 impact=["治安", "签证·居留"],
 for_me="",
 also=[], issue=None,
 quick_replies=["又是去园区的？", "非法入境风险太大", "边境查得严了"]),

dict(id="cn3", topic="cn", secondary=["society", "visa"], region="曼谷",
 headline="泰国破获“假泰国父亲”冒领国籍网络，发出46张逮捕令，8家医院涉案",
 summary=[
  "泰国警察总署总监萨兰（Samran Nuanma）下令，移民局、首都警察第8分局和内政部行政厅N.I.C.E.小组等联合行动，打击“假泰国父亲”网络：泰国男子在外籍母亲所生孩子的出生证明上登记为父亲，让孩子违规取得泰国国籍。",
  "第三阶段行动共发出46张逮捕令，对象包括政府官员、医院员工、外籍母亲、假父亲和真实的外籍父亲等；有24名孩子需核查国籍，涉及8家公立和私立医院。DNA检测显示，登记的泰国父亲与孩子没有血缘关系。前两阶段已查出25名孩子、抓获42名嫌疑人。",
  "其中一案，一名27岁男子出生证明上的父亲是泰国人、母亲是中国人，DNA显示生父是中国人；他已大学毕业，在北榄府一家电缆公司工作，月薪约3万泰铢（约5,940元）。另有一名假父亲承认收了5,000泰铢（约990元）。警方表示，违规取得的泰国国籍将被撤销，同时顾及孩子的利益。"
 ],
 context="💡 警方表示还将追查中介、出证官员和实际受益人。",
 source="Bangkok Biznews（曼谷商业新闻）", url="https://www.bangkokbiznews.com/news/news-update/1258069",
 title_th="จับ 36 คน วงจร 'พ่อไทยทิพย์' งานเข้า 8 โรงพยาบาลรัฐ-เอกชน ลั่น 46 หมายจับ",
 published="2026-10-27T12:30:00+07:00",
 related=[], tags=["假父亲", "泰国国籍", "出生登记", "DNA", "移民局"],
 impact=["签证·居留", "治安"],
 for_me="",
 also=[dict(source="Thai Post（泰国邮报）", url="https://www.thaipost.net/criminality-news/1096068/")], issue=None,
 quick_replies=["查得真细", "孩子怎么办？", "医院也有人参与"]),

dict(id="cn4", topic="cn", secondary=["life"], region="全国",
 headline="11所学校师生赴华夏令营机场受阻，调查认定泰国教育官员涉严重违纪",
 summary=[
  "泰国基础教育委员会（OBEC）秘书长塔努（Thanu Khwankhet）10月26日公布调查结果：此前组织学生赴中国参加短期学习的人，确为该委员会一名8级公务员。",
  "来自11所学校的学生和家长10月15日到达素万那普机场后，发现约定的机票并没有订位，无法按计划出发，家长已向警方报案。",
  "事实调查委员会认定该公务员涉嫌严重违纪，并可能涉及刑事犯罪。委员会将启动严重违纪调查，并指派法务人员报案追究刑责；当事人有权查看证据并为自己辩护。"
 ],
 context="💡 报名海外游学项目时，可先核实机票订位和主办方资质。",
 source="Daily News（每日新闻）", url="https://www.dailynews.co.th/news/6308014/",
 title_th="“ธนู” เปิดผลสอบปมซัมเมอร์เรียนจีน พบมูลผิดวินัยร้ายแรง–จ่อเอาผิดอาญา ขรก.ระดับ 8",
 published="2026-10-27T12:09:00+07:00",
 related=[], tags=["赴华夏令营", "教育部门", "违纪", "素万那普机场", "游学"],
 impact=[],
 for_me="",
 also=[], issue=None,
 quick_replies=["孩子们太可怜了", "要严惩", "游学要多核实"]),

dict(id="pe1", topic="poleco", secondary=["cn"], region="全国",
 headline="泰国投资促进委员会：前9个月投资申请1.71万亿泰铢，中国项目数居首",
 summary=[
  "泰国投资促进委员会（BOI）秘书长纳立（Narit Therdsteerasukdi）表示，2026年前9个月共收到1,954个投资促进申请，总额1.71万亿泰铢（约3,381亿元），同比增长28%。",
  "数字产业最多，139个项目超过1.17万亿泰铢（约2,317亿元），接近去年的两倍；其次是电子电器、农业与食品、能源与基础设施。外国直接投资申请1,309个，金额同比增长62%。",
  "按金额计，新加坡排第一，214个项目共1.16万亿泰铢（约2,306亿元）；中国排第二，493个项目共633.9亿泰铢（约125.5亿元），项目数量排第一。"
 ],
 context="",
 source="Kaohoon International（Kaohoon国际）", url="https://www.kaohooninternational.com/economics/593255",
 title_th="Thailand’s BOI Investment Applications Hit THB1.7 Trillion in 9M26, Driven by Digital and Electronics Sectors",
 published="2026-10-27T00:00:00+07:00",
 related=[], tags=["投资促进委员会", "BOI", "外国投资", "数字产业", "中国企业"],
 impact=[],
 for_me="",
 also=[], issue=None,
 quick_replies=["中国企业还是多", "数据中心真火", "新加坡这么多？"]),

dict(id="bk1", topic="bangkok", secondary=["weather", "travel"], region="廊曼机场",
 headline="廊曼机场11月1日起取消手持金属探测器，改为人工搜身",
 summary=[
  "廊曼国际机场通过官方脸书宣布，11月1日起安检不再使用手持金属探测器，改为人工搜身。旅客仍先通过金属探测门或人体扫描仪，只有需要进一步检查时才搜身。",
  "机场表示，这是按照泰国民航局第113号规定和国际民航组织建议，与国际航空安保做法接轨，搜身会“适当并尊重旅客权利”。",
  "机场提醒旅客，高峰时段可能排队更久，请预留时间：排队时先取出金属物品，提前整理好行李；如有伤病、体内植入医疗器械或怀孕等情况，安检前先告知安检人员。"
 ],
 context="💡 泰国民航局此前还建议旅客在托运前给行李内外拍照。10月16日至22日，廊曼机场检查了927件托运行李，发现1,122件违禁或不合规物品。",
 source="Thaiger（泰格新闻）", url="https://thethaiger.com/news/world/aviation/don-mueang-airport-swaps-hand-held-detector-for-pat-down-search",
 title_th="Don Mueang Airport swaps hand-held detector for pat-down search",
 published="2026-10-27T11:03:00+07:00",
 related=[], tags=["廊曼机场", "安检", "搜身", "11月1日", "民航局"],
 impact=["交通·事故"],
 for_me="11月1日后从廊曼机场出发，安检请多预留时间。",
 also=[], issue=None,
 quick_replies=["要早点去机场", "搜身有点尴尬", "国际惯例就好"]),

dict(id="ea1", topic="east", secondary=["society"], region="春武里林查班港",
 headline="泰国海关在林查班港查获藏在木材里的3.1吨象牙，估值1.55亿泰铢（约3,069万元）",
 summary=[
  "泰国海关厅10月26日与特别调查厅（DSI）、国家公园野生动植物保护厅等召开记者会，公布在春武里府林查班港（Laem Chabang）两个集装箱中查获象牙。",
  "货物申报为来自赞比亚的568块锯材，其中32块被挖空，用蜡封住藏匿象牙。共查获象牙3,108.87公斤，包括469根象牙及象牙段、1,038块碎片，另有335根尾毛和一具野生动物尸体，估值约1.55亿泰铢（约3,069万元）。",
  "联合国毒品和犯罪问题办公室（UNODC）和野生动物司法委员会（WJC）提供了情报。官方援引海关法、象牙法、野生动物保护法和《濒危野生动植物种国际贸易公约》处理此案。"
 ],
 context="",
 source="The Nation（民族报）", url="https://www.nationthailand.com/news/general/40072759",
 title_th="Thailand seizes over 3.1 tonnes of ivory hidden in timber from Zambia",
 published="2026-10-26T17:02:00+07:00",
 related=[], tags=["象牙", "林查班港", "海关", "走私", "赞比亚"],
 impact=["治安"],
 for_me="",
 also=[dict(source="Chiang Rai Times（清莱时报）", url="https://www.chiangraitimes.com/crime/thailand-ivory-seized/")], issue=None,
 quick_replies=["3吨太惊人", "大象太可怜", "要追查到底"]),
]

briefing = [
  B("cn", "中国使馆提醒一周多，泰国酒店**中国客预订仍偏弱**", "cn1"),
  B("cn", "“假泰国父亲”冒领国籍网络被破获，**46张逮捕令**、8家医院涉案", "cn3"),
  B("cn", "4名非法入境中国男子被捕，原拟经**湄索去缅甸**", "cn2"),
  B("bangkok", "廊曼机场**11月1日**起改为人工搜身", "bk1"),
  B("poleco", "前9个月投资申请**1.71万亿泰铢**，中国项目数居首", "pe1"),
  B("east", "林查班港查获**3.1吨象牙**", "ea1"),
]

china_top = []

fx = dict(THB_CNY=0.19801, source="open.er-api.com（data/ticker.json）", note="THB_CNY 2026-10-27 07:02 BKK")

data = dict(
  id="2026-10-27-md", date="2026-10-27", edition="md", edition_label="午间版",
  weekday="星期二", timezone="Asia/Bangkok (UTC+7)",
  coverage="2026年10月26日至10月27日12:30（曼谷时间）发布的泰国新闻；本期为应急版，候选取自10月27日中午的选题清单，仅收录已核对原文的7篇报道。",
  previous="2026-10-26-md",
  briefing=briefing,
  highlights=["cn1", "cn3", "bk1"],
  stories=stories, china_top=china_top, fx=fx)

if __name__ == "__main__":
    write_edition(data)
