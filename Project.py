import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

df = pd.read_csv('Accident.csv',encoding = 'CP949')



seoul = df.loc[1:299,['시도','시군구','시간대','발생건수','부상신고']]
busan = df.loc[300:491,['시도','시군구','시간대','발생건수','부상신고']]
kyeonggi = df.loc[492:863,['시도','시군구','시간대','발생건수','부상신고']]
kangwon = df.loc[864:1075,['시도','시군구','시간대','발생건수','부상신고']]
chungbuk = df.loc[1076:1206,['시도','시군구','시간대','발생건수','부상신고']]
chungnam = df.loc[1207:1385,['시도','시군구','시간대','발생건수','부상신고']]
jeonbuk = df.loc[1386:1544,['시도','시군구','시간대','발생건수','부상신고']]
jeonnam = df.loc[1545:1805,['시도','시군구','시간대','발생건수','부상신고']]
kyeongbuk = df.loc[1806:2071,['시도','시군구','시간대','발생건수','부상신고']]
kyeongnam = df.loc[2072:2282,['시도','시군구','시간대','발생건수','부상신고']]
jeju = df.loc[2283:2306,['시도','시군구','시간대','발생건수','부상신고']]
daegu = df.loc[2307:2402,['시도','시군구','시간대','발생건수','부상신고']]
incheon = df.loc[2403:2519,['시도','시군구','시간대','발생건수','부상신고']]
gwangju = df.loc[2520:2579,['시도','시군구','시간대','발생건수','부상신고']]
daejeon = df.loc[2580:2639,['시도','시군구','시간대','발생건수','부상신고']]
ulsan = df.loc[2640:2699,['시도','시군구','시간대','발생건수','부상신고']]
sejong = df.loc[2700:2711,['시도','시군구','시간대','발생건수','부상신고']]

geumjeonggu = df.loc[420:431,['시도','시군구','시간대','발생건수','부상신고']]
geumjeonggu_num = geumjeonggu.loc[:,['발생건수']]
geumjeonggu_injury = geumjeonggu.loc[:,['부상신고']]
dongraegu = df.loc[360:371,['시도','시군구','시간대','발생건수','부상신고']]
dongraegu_num = dongraegu.loc[:,['발생건수']]
dongraegu_injury = dongraegu.loc[:,['부상신고']]

seoul_num = (seoul.loc[:,['발생건수']])
busan_num = (busan.loc[:,['발생건수']])
kyeonggi_num = (kyeonggi.loc[:,['발생건수']])
kangwon_num = (kangwon.loc[:,['발생건수']])
chungbuk_num = (chungbuk.loc[:,['발생건수']])
chungnam_num = (chungnam.loc[:,['발생건수']])
jeonbuk_num = (jeonbuk.loc[:,['발생건수']])
jeonnam_num = (jeonnam.loc[:,['발생건수']])
kyeongbuk_num = (kyeongbuk.loc[:,['발생건수']])
kyeongnam_num = (kyeongnam.loc[:,['발생건수']])
jeju_num = (jeju.loc[:,['발생건수']])
daegu_num = (daegu.loc[:,['발생건수']])
incheon_num = (incheon.loc[:,['발생건수']])
gwangju_num = (gwangju.loc[:,['발생건수']])
daejeon_num = (daejeon.loc[:,['발생건수']])
ulsan_num = (ulsan.loc[:,['발생건수']])
sejong_num = (sejong.loc[:,['발생건수']])

time = ['00시-02시','02시-04시','04시-06시','06시-08시','08시-10시','10시-12시','12시-14시','14시-16시','16시-18시','18시-20시','20시-22시','22시-0시']
time2 = [0,1,2,3,4,5,6,7,8,9,10,11]


plt.title('시간대별 교통사고 발생수')
plt.plot(time2,geumjeonggu_num,'bo-')
plt.plot(time2,dongraegu_num,'bo-',c='r')
plt.xticks(time2,time)
plt.xlabel('시간')
plt.ylabel('발생건수')

plt.show()

plt.title('금정구와 동래구 부상신고 수')
plt.plot(time2,geumjeonggu_injury,'bo-')
plt.plot(time2,dongraegu_injury,'bo-',c = 'r')
plt.xticks(time2,time)
plt.xlabel('시간')
plt.ylabel('부상자 수')

plt.show()