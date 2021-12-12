from main import *

fire_sick = fire[["부상","발화열원"]]

sick = fire_sick.sort_values(by="부상", ascending=False)
print(sick.head())