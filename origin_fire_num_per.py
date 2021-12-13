import pandas as pd

from main import *

#발화열원 많은 유형 추출

# origin = fire[["발화열원","인명피해(명)소계"]]
# print(origin["발화열원"].size)
data_origin = fire["발화열원"].value_counts()

dataframe = data_origin.to_frame(name='횟수')
print(dataframe)
dataframe = dataframe.reset_index()
# print(dataframe)
dataframe.plot(kind='barh',x='index', y = '횟수', color = 'red')
plt.show()

#발화열원별 발화요인대분류
#작동기기에 대한 발화요인대분류
fire_reason = fire[["발화열원","발화요인대분류"]]
fire_reason = fire_reason.loc[fire_reason["발화열원"]=="작동기기", ["발화열원","발화요인대분류"]]
fire_reason.to_csv("fire//elect_reason.csv",index= False,encoding='utf-8-sig')
print(fire_reason["발화열원"].size)
print(fire_reason)
fire_reason = fire_reason["발화요인대분류"].value_counts()
fire_reason_fm = fire_reason.to_frame(name= '횟수')
print(fire_reason_fm)
fire_reason_fm = fire_reason_fm.reset_index()
fire_reason.plot(kind='barh',x= 'index',y='횟수',color= 'blue')
plt.show()
