# -*- coding: utf-8 -*-
"""2026-10-24 午间版 — Claude 비상 발행(중국어판 정기 담당 없음). 원문 확인한 10건."""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from newslib import write_edition, B, KR

stories = [
dict(id="cn1", topic="cn", secondary=["poleco", "east"], region="曼谷—罗勇",
 headline="泰国三机场高铁项目陷僵局：泰国国家铁路局起诉正大财团追讨逾133亿泰铢（约26亿元）",
 summary=[
  "连接廊曼、素万那普和乌塔堡三座机场的高铁全长220公里，总投资2245.44亿泰铢（约445亿元），2019年10月24日由正大集团（CP）牵头的Asia Era One财团签约，特许经营期50年。财团股东中，中国铁建（China Railway Construction Corporation）持股10%。",
  "财团要求改为“边建边付”模式，但修改合同须重新经过东部经济走廊（EEC）政策委员会和内阁批准，未能在9月30日期限前完成。财团7月6日致函泰国国家铁路局（SRT），提出以9月30日为期终止合作协议，并同意将机场快线运营维持到2027年1月。",
  "泰国国家铁路局10月21日向中央行政法院起诉，追讨机场快线特许经营费及违约利息共133.36亿泰铢（约26.43亿元）。铁路局表示私方不能单方面解约，合同仍有效；诉讼可能耗时3至5年以上。铁路局董事会将于10月30日开会。"
 ],
 context="💡 替代方案之一是把中泰铁路延伸至林查班港和罗勇，目前仍在研究阶段。",
 source="Pattaya Mail（芭提雅邮报）", url="https://www.pattayamail.com/latestnews/news/thailands-224-billion-baht-high-speed-rail-project-faces-collapse-569494",
 title_th="Thailand's 224-billion-baht high-speed rail project faces collapse",
 published="2026-10-24T02:50:00+07:00",
 related=[], tags=["三机场高铁", "正大集团", "中国铁建", "国家铁路局", "EEC"],
 impact=["交通·事故"],
 for_me="机场快线（Airport Rail Link）暂时照常运营，至少维持到2027年1月。",
 also=[], issue=None,
 quick_replies=["高铁还能建成吗？", "机场快线别停就好", "关注10月30日会议"]),

dict(id="cn2", topic="cn", secondary=["society", "bangkok"], region="曼谷",
 headline="泰国移民局在曼谷抓获两名被国际刑警组织红色通缉的中国男子",
 summary=[
  "泰国移民局局长诺帕信（Noppasin Phunsawat）与中央调查局联合行动，10月20日约19:00在曼谷分别抓获两名中国男子：陈某（30岁）藏身奇隆（Chit Lom）一带豪华公寓，杨某（28岁）藏身是隆一带另一处公寓。",
  "两人均被国际刑警组织发布红色通缉令，涉及阿联酋迪拜的绑架、非法拘禁案。据报道，今年6月7名嫌犯从迪拜一处豪宅绑走一名土耳其商人、其中国籍女友和孟加拉籍司机，三人遗体后在迪拜东南方向的沙漠中被发现。",
  "在泰国，陈某因居留许可已于9月23日到期而被控逾期居留，杨某的居留许可被撤销。两人已移交移民局调查部门，泰国警方正与国际执法机构协调。"
 ],
 context="",
 source="MGR Online（经理人在线）", url="https://mgronline.com/crime/detail/9690000101968",
 title_th="รวบ 2 หนุ่มจีนผู้ต้องหาหมายแดงอินเตอร์โพล คดีอุ้มฆ่า 3 ศพ ฝังอำพรางทะเลทรายดูไบ หนีซุกคอนโดหรูกลางกรุง",
 published="2026-10-22T13:35:00+07:00",
 related=[], tags=["移民局", "国际刑警", "红色通缉", "迪拜", "逾期居留"],
 impact=["治安"],
 for_me="",
 also=[], issue=None,
 quick_replies=["抓得好", "会被引渡吗？", "曼谷公寓也要留意"]),

dict(id="cn3", topic="cn", secondary=["east", "society"], region="芭提雅",
 headline="芭提雅宗天一公寓20楼坠落，61岁中国男子身亡",
 summary=[
  "10月23日约07:00，芭提雅宗天地区帖普拉西路（Thepprasit Road）一栋公寓旁的路面上发现一名61岁中国籍男子徐某的遗体。他与泰籍伴侣（未登记结婚）住在该楼20层，生前患有疾病。",
  "芭提雅警察局调查人员在现场发现一封写给伴侣的手写信。警方表示坠落的具体经过尚未查明，仍在收集证据、询问相关人员；遗体已送往芭提雅医院，并已与中国驻泰国大使馆联系。"
 ],
 context="💡 如您或身边的人情绪低落，可寻求亲友或专业心理支持。",
 source="The Pattaya News（芭提雅新闻）", url="https://thepattayanews.com/2026/10/23/61-year-old-chinese-man-dies-after-fall-from-20th-floor-of-pattaya-condominium/",
 title_th="61-Year-Old Chinese Man Dies After Fall from 20th Floor of Pattaya Condominium",
 published="2026-10-23T22:29:00+07:00",
 related=[], tags=["芭提雅", "宗天", "坠楼", "中国公民", "使馆"],
 impact=[],
 for_me="",
 also=[], issue=None,
 quick_replies=["愿逝者安息", "等警方调查结果", "独居长者需多关心"]),

dict(id="cn4", topic="cn", secondary=["north", "society"], region="达府湄索",
 headline="11名外国人逃离缅甸妙瓦底入境泰国湄索被拘，含4名中国人",
 summary=[
  "泰国移民官员与边境特遣部队接到线报后，在达府湄索县湄卡萨乡一片甘蔗田中找到11名无证男子，他们承认数小时前非法渡过莫埃河入境。",
  "11人中有中国籍4人、印度籍2人，巴基斯坦、越南、尼日利亚、肯尼亚籍各1人，另有1名非洲籍人士国籍未明。据报道，他们是从缅甸妙瓦底逃出，躲避疑似诈骗团伙和当地战事。",
  "这些人将移交湄索警察局按非法入境处理；当局将甄别其中是否有人口贩卖受害者，若是则可获得特别保护而非直接遣返。边境巡逻已加强，并在湄索对外主要道路增设检查站。"
 ],
 context="💡 以“高薪工作”为名诱骗到缅甸边境诈骗园区的情况仍在发生，赴泰求职务必核实雇主。",
 source="Chiang Rai Times（清莱时报）", url="https://www.chiangraitimes.com/crime/soldiers-foreigners-mae-sot/",
 title_th="Soldiers Detain 11 Foreigners Fleeing Scam Gangs in Myanmar",
 published="2026-10-24T05:59:00+07:00",
 related=[], tags=["湄索", "妙瓦底", "电诈园区", "非法入境", "人口贩卖"],
 impact=["治安"],
 for_me="被骗入境外诈骗园区者可向泰国警方说明情况，当局会甄别是否为人口贩卖受害者。",
 also=[], issue=None,
 quick_replies=["终于逃出来了", "高薪招聘别轻信", "希望都能平安回国"]),

dict(id="vi1", topic="visa", secondary=["south"], region="帕岸岛",
 headline="帕岸岛撤销一名以色列女子签证，因屡遭投诉行为不当",
 summary=[
  "帕岸岛县长领导的外国人投诉审查委员会（成员包括旅游警察和地方行政官员）认定，一名33岁以色列女子的行为威胁公共秩序、善良风俗和当地安全，撤销其签证，她将被尽快驱逐出境。",
  "当地官员称，她多次口头威胁要动手、对官员和居民出言不逊，拖欠酒店长住费用，并拒交塘沙瀑布国家公园门票。报道称，她是近期帕岸岛第三名被撤销签证的以色列人，今年1月以来当地已撤销10名外国人的签证。"
 ],
 context="💡 泰国近期要求各府对“问题游客”快速处理，持任何签证在泰都需遵守当地法规和公共秩序。",
 source="Chiang Rai Times（清莱时报）", url="https://www.chiangraitimes.com/crime/israeli-woman-visa-revolked/",
 title_th="Israeli Woman on Koh Pha Ngan Has Visa Revolked",
 published="2026-10-24T06:46:00+07:00",
 related=[], tags=["签证", "撤销签证", "驱逐出境", "帕岸岛", "外国游客"],
 impact=["签证·居留"],
 for_me="在泰外国人若被多次投诉扰乱秩序，可能被撤销签证并驱逐。",
 also=[], issue=None,
 quick_replies=["守规矩最重要", "处理得很快", "入乡随俗"]),

dict(id="wt1", topic="weather", secondary=["south", "bangkok"], region="南部·全国",
 headline="泰国气象厅发布第2号警报：南部10月24日至28日大到暴雨，曼谷26至27日有大雨",
 summary=[
  "泰国气象厅10月24日05:00发布第2号警报：南部持续降雨，10月24日至28日部分地区有大到暴雨，山脚坡地、河道附近和低洼地区可能出现山洪；10月25日有5个南部府份可能遭遇特大暴雨。",
  "受来自中国的冷空气影响，10月25日至27日泰国上部地区有雷阵雨和阵风：东北部25日、北部、中部和东部26日有局部大雨，曼谷及周边26日和27日有大雨。泰国湾和安达曼海雷雨区浪高可超过2米。"
 ],
 context="💡 雷雨时远离空旷地带、大树和不稳固的广告牌；出海请谨慎。气象厅24小时热线1182。",
 source="The Nation（民族报）", url="https://www.nationthailand.com/news/general/40072666",
 title_th="TMD warns 5 southern provinces of very heavy rain on October 25",
 published="2026-10-24T05:50:00+07:00",
 related=[], tags=["气象厅", "暴雨", "山洪", "南部", "冷空气"],
 impact=["天气·灾害"],
 for_me="前往南部或周末出行者请留意最新预报，曼谷26至27日出门备好雨具。",
 also=[], issue=None,
 quick_replies=["南部又要下大雨", "曼谷也要下了", "出行注意安全"]),

dict(id="ea1", topic="east", secondary=["travel"], region="芭提雅",
 headline="三天连休，芭提雅格兰岛游客爆满，巴厘海码头排长队",
 summary=[
  "泰国10月23日至25日三天连休，10月23日（周五）大批游客前往格兰岛（Koh Larn），芭提雅巴厘海码头全天繁忙，渡轮和快艇售票处及登船口排起长队。",
  "当天天气晴好，预计周末游客还会增加。报道提醒，出行请预留排队购票和登船的时间，尤其是出发高峰时段。"
 ],
 context="",
 source="Pattaya Mail（芭提雅邮报）", url="https://www.pattayamail.com/latestnews/news/koh-larn-draws-holiday-crowds-during-thailands-three-day-break-569488",
 title_th="Koh Larn draws holiday crowds during Thailand's three-day break",
 published="2026-10-24T03:58:00+07:00",
 related=[], tags=["格兰岛", "巴厘海码头", "连休", "芭提雅", "渡轮"],
 impact=["交通·事故"],
 for_me="周末去格兰岛请提早出发，预留排队时间。",
 also=[], issue=None,
 quick_replies=["人太多了", "错峰出行", "格兰岛海水不错"]),

dict(id="ea2", topic="east", secondary=["poleco"], region="罗勇",
 headline="乌塔堡机场第二跑道完工逾30%，预计2028年底建成",
 summary=[
  "据东部经济走廊（EEC）办公室和意泰发展公司（ITD）提供的资料，罗勇乌塔堡国际机场第二跑道建设进度已超过30%。跑道长3505米、宽60米，含滑行道等配套设施，计划2028年底完工。",
  "该工程属于EEC“航空城”开发计划；飞机维修（MRO）中心合同已于2026年10月初签署，新空中交通管制塔台计划于2026年招标。"
 ],
 context="",
 source="Pattaya Mail（芭提雅邮报）", url="https://www.pattayamail.com/latestnews/news/u-tapao-airports-second-runway-passes-30-completion-569497",
 title_th="U-Tapao Airport's second runway passes 30% completion",
 published="2026-10-24T03:43:00+07:00",
 related=[], tags=["乌塔堡机场", "第二跑道", "EEC", "航空城", "罗勇"],
 impact=[],
 for_me="",
 also=[], issue=None,
 quick_replies=["乌塔堡越来越重要", "2028年见", "东部发展快"]),

dict(id="pe1", topic="poleco", secondary=["north", "cn"], region="乌隆",
 headline="泰国内阁11月2日至3日赴乌隆开流动会议，商会提42个项目约398亿泰铢（约79亿元）",
 summary=[
  "泰国阿努廷政府第二次流动内阁会议将于11月2日至3日在乌隆府举行，总理11月2日将主持乌隆世界园艺博览会开幕。涉及乌隆、黎府、廊开、廊磨南蒲、汶干5府，重点为高价值农业、边境贸易、旅游和禁毒。",
  "各府商会合计提出42个项目，金额398.28亿泰铢（约78.94亿元），属建议而非已批预算。其中汶干府提议在“黄金四角”框架下促进泰国、老挝、越南、中国的商务对接，并在第五座泰老友谊大桥附近设经济特区。",
  "国家经济社会发展委员会秘书长表示，不再沿用每府约5000万泰铢（约991万元）的旧模式，将侧重政策与法规支持。园艺博览会11月1日开幕至2027年3月14日，目标约350万人次参观。"
 ],
 context="",
 source="Prachachat（民族经济报）", url="https://www.prachachat.net/politics/news-2085402",
 title_th="ครม.สัญจรอุดรชง 4 หมื่นล้าน เชื่อมค้าจีน",
 published="2026-10-24T07:05:00+07:00",
 related=[], tags=["流动内阁", "乌隆", "园艺博览会", "边境贸易", "汶干"],
 impact=[],
 for_me="",
 also=[], issue=None,
 quick_replies=["东北部要发展了", "园艺博览会想去看看", "有中国相关项目吗？"]),

dict(id="lf1", topic="life", secondary=["poleco"], region="全国",
 headline="泰国住房银行推出房贷，300万泰铢（约59万元）以下住房首两年利率2.60%",
 summary=[
  "泰国住房银行（GH Bank）推出“Home for Everyone PLUS”贷款，适用于价格不超过300万泰铢（约59万元）的购房或建房，最长40年，每借100万泰铢（约20万元）初期月供从3600泰铢（约714元）起，申请截至2030年12月30日或额度用完为止。",
  "一般收入类别首两年年利率2.60%，第3年3.40%，第4至5年4.00%；须先通过GHB ALL GEN应用程序登记取得参与代码，再到全国分行申请。报道未说明外国人是否符合申请资格。"
 ],
 context="💡 外国人在泰购房受法律限制，是否可申请请直接向银行核实。",
 source="Pattaya Mail（芭提雅邮报）", url="https://www.pattayamail.com/latestnews/news/thailands-gh-bank-offers-home-loans-from-2-60-for-properties-up-to-3-million-baht-569535",
 title_th="Thailand's GH Bank offers home loans from 2.60% for properties up to 3 million baht",
 published="2026-10-24T02:27:00+07:00",
 related=[], tags=["房贷", "住房银行", "利率", "购房", "GH Bank"],
 impact=["汇率·物价"],
 for_me="",
 also=[], issue=None,
 quick_replies=["利率挺低", "外国人能申请吗？", "有人办过吗？"]),
]

briefing = [
  B("cn", "三机场高铁陷僵局，铁路局起诉正大财团追讨**133.36亿泰铢（约26.43亿元）**", "cn1"),
  B("cn", "移民局在曼谷抓获**2名**被国际刑警红色通缉的中国男子", "cn2"),
  B("cn", "11名外国人逃离妙瓦底入境湄索被拘，含**4名中国人**", "cn4"),
  B("visa", "帕岸岛撤销一名以色列女子签证，今年已撤销**10名**外国人签证", "vi1"),
  B("weather", "南部**10月24日至28日**大到暴雨，曼谷26至27日有大雨", "wt1"),
  B("east", "三天连休，格兰岛游客爆满，巴厘海码头**排长队**", "ea1"),
]

china_top = []

fx = dict(THB_CNY=0.1982, source="open.er-api.com（data/ticker.json）", note="THB_CNY 2026-10-24 07:02 BKK")

data = dict(
  id="2026-10-24-md", date="2026-10-24", edition="md", edition_label="午间版",
  weekday="星期六", timezone="Asia/Bangkok (UTC+7)",
  coverage="2026年10月22日至10月24日08:30（曼谷时间）发布的泰国新闻；本期为应急版，候选取自10月24日08:25收集批次，仅收录已核对原文的10篇报道。",
  previous="2026-10-23-md",
  briefing=briefing,
  highlights=["cn1", "cn4", "wt1"],
  stories=stories, china_top=china_top, fx=fx)

if __name__ == "__main__":
    write_edition(data)
