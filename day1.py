#%% keyword 
import keyword
print(keyword.kwlist)

import keyword as kw
print(kw.kwlist)

#%% datetime
import datetime as dt
now = dt.datetime.now()
print("# 현재 시각 출력하기")
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")

#%% list
list_a = [273, 32, 103, "문자열", True, False]
print("# 리스트 뒤에 요소 추가하기")
list_a.append(4)
list_a.append(5)
print(list_a)

print("# 리스트 중간에 요소 추가하기")
list_a.insert(0,10)
print(list_a)

list_a.extend([4,5,6])
print(list_a)

#%% list for
array = [273, 32, 103, 57, 52]

for element in array:
    print(element)



    