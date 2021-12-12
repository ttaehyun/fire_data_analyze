from main import *

#발화열원 많은 유형 추출

origin = fire["발화열원"]
origin_dict = dict()
        #series에서 개수 세기 len(변수) or 변수.size or len(변수.index)

for type in origin:
    if (type in origin_dict):
        origin_dict[type] += 1
    else:
        origin_dict[type] = 1

#발화열원별 발생빈도
origin_per = dict()
all_num = origin.size
for type in origin_dict.keys():
    origin_per[type] = round(origin_dict[type] / all_num *100, 2)

# 발화열원별 개수 추출한 값 csv파일에 저장
# 횟수 그래프
origin_frame = pd.DataFrame(origin_dict,index= ['횟수'])
origin_frame = origin_frame.transpose()
origin_frame = origin_frame.reset_index()
# origin_frame.to_csv("fire//origin_sum_num.csv",encoding='utf-8-sig')
origin_frame.plot(kind='barh',x= 'index', y = '횟수', color = 'red')

#빈도 그래프
origin_per_fm = pd.DataFrame(origin_per, index=['발생빈도'])
origin_per_fm = origin_per_fm.transpose()
origin_per_fm.plot(kind='pie', y = '발생빈도')

print(origin_frame)
print(origin_per_fm)
plt.show()