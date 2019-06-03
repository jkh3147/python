# 본인의 과제명 작성

학과 | 학번 | 성명
---- | ---- | ---- 
전기컴퓨터공학부 |201524566 | 정경호


## 프로젝트 개요
시간대별 교통사고 발생 현황을 파악한다. 그 중 부산대학교가 위치한 부산시 금정구의 현황을 알아본다.

## 사용한 공공데이터 
[데이터보기](https://github.com/cybermin/python2019/blob/master/%EB%B6%80%EC%82%B0%EA%B5%90%ED%86%B5%EA%B3%B5%EC%82%AC_%EB%8F%84%EC%8B%9C%EC%B2%A0%EB%8F%84%EC%97%AD%EC%82%AC%EC%A0%95%EB%B3%B4_20190520.csv)

## 소스
* [링크로 소스 내용 보기](https://github.com/cybermin/python2019/blob/master/tes.py) 

* 코드 삽입
~~~python
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

df = pd.read_csv('Accident.csv',encoding = 'CP949')

seoul = df.loc[1:299,['시도','시군구','시간대','발생건수']]
busan = df.loc[300:491,['시도','시군구','시간대','발생건수']]
kyeonggi = df.loc[492:863,['시도','시군구','시간대','발생건수']]
kangwon = df.loc[864:1075,['시도','시군구','시간대','발생건수']]
chungbuk = df.loc[1076:1206,['시도','시군구','시간대','발생건수']]
chungnam = df.loc[1207:1385,['시도','시군구','시간대','발생건수']]
jeonbuk = df.loc[1386:1544,['시도','시군구','시간대','발생건수']]
jeonnam = df.loc[1545:1805,['시도','시군구','시간대','발생건수']]
kyeongbuk = df.loc[1806:2071,['시도','시군구','시간대','발생건수']]
kyeongnam = df.loc[2072:2282,['시도','시군구','시간대','발생건수']]
jeju = df.loc[2283:2306,['시도','시군구','시간대','발생건수']]
daegu = df.loc[2307:2402,['시도','시군구','시간대','발생건수']]
incheon = df.loc[2403:2519,['시도','시군구','시간대','발생건수']]
gwangju = df.loc[2520:2579,['시도','시군구','시간대','발생건수']]
daejeon = df.loc[2580:2639,['시도','시군구','시간대','발생건수']]
ulsan = df.loc[2640:2699,['시도','시군구','시간대','발생건수']]
sejong = df.loc[2700:2711,['시도','시군구','시간대','발생건수']]

geumjeonggu = df.loc[420:431,['시도','시군구','시간대','발생건수']]
geumjeonggu_num = geumjeonggu.loc[:,['발생건수']]

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

plt.title('금정구 시간대별 사고 발생수')
plt.plot(time2,geumjeonggu_num,'bo-')
plt.xticks(time2,time)
plt.xlabel('시간')
plt.ylabel('발생건수')

plt.show()

~~~
