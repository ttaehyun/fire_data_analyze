from main import *

#사망자, 부상자수 많은 발화열원 추출
#사망자,부상자가 있을 때의 발화열원 수 구하기
fire_dead_origin = fire.loc[fire["사망"]>0, ["사망","발화열원"]]
print(fire_dead_origin)
#딕셔너리로 발화원인 수 표현
fire_dead_origin_dc = dict()
print(f"사망자 수: {fire_dead_origin.size}")
for type in fire_dead_origin["발화열원"]:
    if (type in fire_dead_origin_dc):
        fire_dead_origin_dc[type] += 1
    else:
        fire_dead_origin_dc[type] = 1
print(fire_dead_origin_dc)