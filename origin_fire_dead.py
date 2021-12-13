from main import *

#사망자, 부상자수 많은 발화열원 추출

#사망자,부상자가 있을 때의 발화열원 수 구하기
fire_dead_origin = fire.loc[fire["인명피해(명)소계"]>0, ["발화열원","발화요인대분류","인명피해(명)소계"]]
print(fire_dead_origin.sort_values(by=["인명피해(명)소계"], ascending= False))
print(fire_dead_origin["발화열원"].value_counts())
fire_human_fm = fire_dead_origin["발화열원"].value_counts()
fire_human_fm = fire_human_fm.to_frame(name= "인명피해(명)소계")
fire_human_fm = fire_human_fm.reset_index()
print(fire_human_fm)
fire_human_fm.plot(kind='barh',x='index',y='인명피해(명)소계',color='yellow')
plt.show()

#인명피해 큰 발화열원에서 발화 대분류 구분
reason_origin = fire_dead_origin.loc[fire_dead_origin["발화열원"] == "작동기기",["발화열원","발화요인대분류"]]
reason_origin.to_csv("fire//reason_origin.csv",index= False,encoding='utf-8-sig')
# print(reason_origin.size)
reason_origin_ct = reason_origin["발화요인대분류"].value_counts()
print(reason_origin_ct)
reason_origin_ct = reason_origin_ct.to_frame(name = "사건수")
reason_origin_ct = reason_origin_ct.reset_index()
reason_origin_ct.plot(kind='barh',x='index',y='사건수',color='green')
plt.show()
#쌓이는 그래프로? 원그래프??
#발화열원으로 작동기기가 제일 많은 것으로 보아 사람들의 생활에 인접한,
# 쉽게 지나칠 수 있는 곳에서 발화열원이 됨을 알수 있따. 더욱 조심하자