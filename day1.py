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

#%% dict
dict_a = {
    "name": "8D 건조망고",
    "type": "당절임",
    "ingredient":["망고","설탕","메타중아황산나트륨","치자황색호"],
    "origin": "필리핀"
    }
dict_a["price"]=5000
dict_a["name"]="8D 건조 파인애플"

#%% dict for

for key in dict_a:
    print(key,":",dict_a[key])
    
#%% if else
number = input("정수입력>")
number = int(number)

if number > 0:
    print("양수입니다")
elif number < 0:
    print("음수입니다")
else:
    print(" 0 입니다")
    
#%% count numbers
# numbers 내부에 들어있는 숫자가 몇 번 등장하는지를 출력하는 코드 작

numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3] # list
counter = {} # dict 

for number in numbers:
    if number in counter:
        counter[number] = counter[number]+1
    else:
        counter[number]=1

print(counter)
    
#%% 
    
character ={
        "name":"기사",
        "level": 12,
        "items":{
            "sword": "불꽃의 검",
            "armor": "풀플레이트"
            },
        "skill": ["베기","세게 베기","아주 세게 베기"]
        }

for key in character:
    if type(character[key]) is dict:
        for small_key in character[key]:
            print(small_key,":",character[key][small_key])
    elif type(character[key]) is list:
        for item in character[key]:
            print(key,":",item)
    else:
        print(key,":",character[key])
        
#%% mult
def mul(*values):
    output = 1
    for value in values:
        output *= value
    return output
print(mul(5,7,9,10))

    