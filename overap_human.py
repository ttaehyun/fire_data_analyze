from main import *

fire_dead_origin = fire.loc[fire["인명피해(명)소계"]>0, ["발화열원","발화요인대분류","인명피해(명)소계"]]
#인명피해 큰 발화열원에서 발화 대분류 구분
reason_origin = fire_dead_origin.loc[fire_dead_origin["발화열원"] == "작동기기",["발화열원","발화요인대분류"]]
# reason_origin.to_csv("fire//reason_origin.csv",index= False,encoding='utf-8-sig')
# print(reason_origin.size)
reason_origin_ct = reason_origin["발화요인대분류"].value_counts()
print(reason_origin_ct)
reason_origin_ct = reason_origin_ct.to_frame(name = "인명피해수")
reason_origin_ct = reason_origin_ct.transpose()
reason_origin_ct.plot(kind='bar',stacked= True)
plt.show()