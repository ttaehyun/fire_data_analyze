from main import *
#작동기기 화재 건수에 대한 발화요인 중첩그래프 그리기
data_origin = fire["발화열원"].value_counts()

dataframe = data_origin.to_frame(name='횟수')

fire_reason = fire[["발화열원","발화요인대분류"]]
fire_reason = fire_reason.loc[fire_reason["발화열원"]=="작동기기", ["발화열원","발화요인대분류"]]
fire_reason = fire_reason["발화요인대분류"].value_counts()
fire_reason_fm = fire_reason.to_frame(name= '작동기기')
print(dataframe)
fire_reason_fm = fire_reason_fm.transpose()
fire_reason_fm.plot(kind='bar',stacked=True)
print(fire_reason_fm)
plt.show()