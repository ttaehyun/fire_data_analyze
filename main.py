import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)
fire = pd.read_csv("fire//화재통계.csv", encoding= 'CP949')

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

#발화열원 많은 유형 추출
origin = fire["발화열원"]
print(origin.size)                                  #series에서 개수 세기 len(변수) or 변수.size or len(변수.index)
origin_dict = dict()
for type in origin:
    if (type in origin_dict):
        origin_dict[type] += 1
    else:
        origin_dict[type] = 1
# print(origin_dict)

# 발화열원별 개수 추출한 값 csv파일에 저장
origin_frame = pd.DataFrame(origin_dict,index= ['횟수'])
origin_frame = origin_frame.transpose()
print(origin_frame)
origin_frame = origin_frame.reset_index()
# origin_frame.to_csv("fire//origin_sum_num.csv",encoding='utf-8-sig')

print(origin_frame)
origin_frame.plot(kind='barh',x= 'index', y = '횟수', color = 'red')
# plt.show()

#발화열원별 발생빈도
origin_per = dict()
all_num = origin.size
for type in origin_dict.keys():
    origin_per[type] = round(origin_dict[type] / all_num *100,2)

print(origin_per)

origin_per_fm = pd.DataFrame(origin_per, index=['발생빈도'])
origin_per_fm = origin_per_fm.transpose()
# origin_per_fm = origin_per_fm.reset_index()
print(origin_per_fm)
origin_per_fm.plot(kind='pie', y = '발생빈도')

# plt.show()

#사망자, 부상자수 많은 발화열원 추출

fire_dead = fire[["사망","발화열원"]]
dead = fire_dead.sort_values(by="사망", ascending= False)
print(dead.head())

#재산피해금액과 장소의 연관성 알아보자