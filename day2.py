#%% 1 ~ 100 까지의 합 구하기 

numbers = []
sum = 0

print("리스트 길이:",len(numbers))

for i in range(100):
    numbers.append(i+1)
    sum += numbers[i]
    
print("리스트 길이:", len(numbers))
print("합계:", sum)

#%% dict for
mango = {
    "name": "8D 건조망고",
    "type": "당절임",
    "ingredient":["망고","설탕","메타중아황산나트륨","치자황색호"],
    "origin": "필리핀"
    }
mango["price"]=5000

mango.keys()
mango.values()

for key in mango:
    print(key,":",mango[key])
    

#%%
number = input("정수입력 > ")
number = int(number)

if number%2 == 0:
    print("짝수입니다")
else:
    print("홀수입니다")
    

#%% if else, count numbers

# numbers 내부에 들어있는 숫자가 몇 번 등장하는지를 출력하는 코드 작성 

numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3] # list
counter = {} # dict 

for number in numbers:
    if number in counter:
        counter[number] = counter[number]+1
    else:
        counter[number]=1

print(counter)

#%% dict 

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

