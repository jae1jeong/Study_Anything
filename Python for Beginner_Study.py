
# 과제1
print("과제 1\n")


ss = '파이썬은완전재미있어요'

sslen = len(ss)
for i in range(0,sslen):
    if i % 2 != 0:
        print('$',end='')
    else:
        print(ss[i],end='')


# 과제2
print("\n\n과제 2")

inStr,outStr = "",""
print(inStr,outStr)
count,i = 0,0

inStr = input("문자열을 입력하세요: ")
count = len(inStr)

for i in range(0,count):
    outStr +=inStr[count-(i+1)]
print("내용을 거꾸로 출력 --> %s" % outStr)

# 과제3
print("\n과제 3\n")


ss = input("입력 문자열==> ")
print("출력 문자열 ==>",end='')

if ss.startswith('(') == False:
    print("(",end ='')

print(ss,end ='')

if ss.endswith(')') == False:
    print(")",end='\n')

# 과제 4
print("\n과제 4")

inStr = "   한글 Python 프로그래밍"
outStr = ''

for i in range(0, len(inStr)):
    if inStr[i] != ' ':
        outStr += inStr[i]

print("\n원래 문자열 ==>" + '['+inStr +']')
print("공백 삭제 문자열 ==>" + '['+outStr +']')


# 과제 5
print("\n과제 5\n")
ss = input("입력 문자열==>")

print("출력 문자열 ==>",end='')
for i in range(0,len(ss)):
    if ss[i] != 'o':
        print(ss[i],end="")

    else:
        print('$',end='')
# 코드 한줄로 print(ss.replace('o',"$"))

print("\n\n과제 6")

ss = input("날짜(연/월/일) 입력 ==> ")

ssList = ss.split('/')

print("입력한 날짜의 10년 후 ==> %s년" % str(int(ssList[0])+10),end= '')
print("%s월"% ssList[1],end='')
print("%s일"% ssList[2],end='\n')


print("\n과제 7\n")

for i in range(0,3):
    ss = input("아무거나 입력해봐: ")

    if ss.isdigit() == True:
        print("숫자네요.")
    elif ss.isalpha() == True:
        print("글네요.")
    elif ss.isalnum() == True:
        print("글자+숫자네요.")
    else:
        print("잘 모르겠네요.")

print("\n과제 8\n")

import turtle as tt
import random
from tkinter.simpledialog import *

inStr = ''
swidth,sheight=300,300
tX,tY,txtSize=[0] *3

tt.title('거북이 글자쓰기')
tt.shape('turtle')
tt.setup(width=swidth+50,height=sheight+50)
tt.screensize(swidth,sheight)
tt.penup()

inStr = askstring('문자열 입력','거북이 쓸 문자열을 입력')
for ch in inStr:
    tX = random.randrange(-swidth/2,swidth/2)
    tY = random.randrange(-sheight/2,sheight/2)
    r = random.random(); g = random.random(); b = random.random();
    txtSize = random.randrange(10,50)


    tt.goto(tX,tY)
    tt.pencolor((r,g,b))
    tt.write(ch,font=('맑은고딕',txtSize,'bold'))

tt.done()

print("\n과제 9\n")

coffee = 0

coffee = int(input("what would you want to drink sir?(1:보통,2:설탕,3:블랙): "))

print()
print('#1. 뜨거운 물을 준비한다.');
print('#2. 종이컵을 준비한다. ');

if coffee == 1:
    print("#3. 보통커피를 탄다.")
elif coffee ==2:
    print('#3. 설탕커피를 탄다.')
elif coffee == 3:
    print('#3. 블랙커피를 탄다.')
else:
    print("#3  아무 커피나 탄다.")

print("#4. 물을 붓는다.")
print('#5. 스푼으로 젓는다.')
print()
print('Here yours sir, Have a Nice Time\n')

print("\n과제 10\n")



def coffee_machine(button):
    print()
    print('#1. (자동으로) 뜨거운 물을 준비한다.');
    print('#2. (자동으로) 종이컵을 준비한다. ');

    if coffee == 1:
        print("#3. (자동으로) 보통커피를 탄다.")
    elif coffee == 2:
        print('#3. (자동으로) 설탕커피를 탄다.')
    elif coffee == 3:
        print('#3. (자동으로) 블랙커피를 탄다.')
    else:
        print("#3  (자동으로) 아무 커피나 탄다.")

    print("#4. (자동으로) 물을 붓는다.")
    print('#5. (자동으로) 스푼으로 젓는다.')
    print()

print("\n과제 11\n")

coffee = int(input("Asir, what would you want to drink?(1:보통,2:설탕,3:블랙): "))
coffee_machine(coffee)
print('Asir,Here yours sir, Have a Nice Time\n')

coffee = int(input("Bsir, what would you want to drink?(1:보통,2:설탕,3:블랙): "))
coffee_machine(coffee)
print('Bsir,Here yours sir, Have a Nice Time\n')

coffee = int(input("Csir, what would you want to drink?(1:보통,2:설탕,3:블랙): "))
coffee_machine(coffee)
print('Csir,Here yours sir, Have a Nice Time\n')


print("\n과제 12\n")

def coffee_machine(button):
    print()
    print('#1. (자동으로) 뜨거운 물을 준비한다.');
    print('#2. (자동으로) 종이컵을 준비한다. ');

    if coffee == 1:
        print("#3. (자동으로) 아메리카노를 탄다.")
    elif coffee == 2:
        print('#3. (자동으로) 카페라떼를 탄다.')
    elif coffee == 3:
        print('#3. (자동으로) 카푸치노를 탄다.')
    elif coffee == 4:
        print('#3. (자동으로) 에스프레소를 탄다.')

    else:
        print("#3  (자동으로) 아무 커피나 탄다.")

    print("#4. (자동으로) 물을 붓는다.")
    print('#5. (자동으로) 스푼으로 젓는다.')
    print()

coffee = int(input("로제씨, what would you want to drink?(1:아메리카노,2:카페라떼,3:카푸치노,4:에스프레소): "))
coffee_machine(coffee)
print('로제씨,Here yours sir, Have a Nice Time\n')

coffee = int(input("리사씨, what would you want to drink?(1:아메리카노,2:카페라떼,3:카푸치노,4:에스프레소): "))
coffee_machine(coffee)
print('리사씨,Here yours sir, Have a Nice Time\n')

coffee = int(input("지수씨, what would you want to drink?(1:아메리카노,2:카페라떼,3:카푸치노,4:에스프레소): "))
coffee_machine(coffee)
print('지수씨,Here yours sir, Have a Nice Time\n')

coffee = int(input("제니씨, what would you want to drink?(1:아메리카노,2:카페라떼,3:카푸치노,4:에스프레소): "))
coffee_machine(coffee)
print('제니씨,Here yours sir, Have a Nice Time\n')


print("\n과제 13\n")

def plus(v1,v2):
    result= 0
    result = v1+v2
    return result

hap = 0
hap = plus(100,200)
print("100과 200의 plus() 함수 결과는: %d "%hap)


print("\n과제 14\n")

def calc(v1,v2,op):
    result =0
    if op == '+':
        result = v1 + v2
    elif op == '-':
        result = v1 - v2
    elif op == '*':
        result = v1 * v2
    elif op == '/':
        result = v1 / v2

    return result

res = 0
var1,var2,oper = 0,0,""

oper = input("계산을 입력하세요(+,-,*,/): ")
var1 = int(input("첫 번쨰 수를 입력하세요: "))
var2 = int(input(" 두 번쨰 수를 입력하세요: "))
res = calc(var1,var2,oper)
print("##계산기 : %d %s %d = %d"%(var1,oper,var2,res))

print("\n과제 15\n")


def calc(v1,v2,op):
    result =0

    if op == '+':
        result = v1 + v2
    elif op == '-':
        result = v1 - v2
    elif op == '*':
        result = v1 * v2
    elif op == '/':
        if v1 or v2 == 0:
            print('0으로 나누면 안 됩니다.')
        else:
            result = v1 / v2
    elif op == '**':
        result = v1 ** v2

    return result

res = 0
v1,v2,op = 0,0,""
op = input("계산을 입력하세요(+,-,*,/,**): ")
v1 = int(input("첫 번쨰 수를 입력하세요: "))
v2 = int(input("두 번쨰 수를 입력하세요: "))
res = calc(v1,v2,op)
print("##계산기 : %d %s %d = %d"%(v1,op,v2,res))


print("\n과제 16\n")

def func1():
    a =10
    print("func1()에서 a값 %d"%a)
def func2():
    print("func1()에서 a값 %d"%a)
a = 20

func1()
func2()

print("\n과제 18\n")

def func1():
    global a
    a = 10
    print("func1()에서 a값 %d"%a)
def func2():
    print("func1()에서 a값 %d"%a)

a = 20

func1()
func2()


print("\n과제 19\n")

def func1():
    result = 100
    return result

def func2():
    print("반환값이 없는 함수 실행")



hap = 0

hap = func1()
print("func1에서 돌려준 값 ==> %d "% hap)
func2()

print("\n과제 20\n")

def multi(v1,v2):
    reList = []
    res1 = v1+v2
    res2 = v1-v2
    reList.append(res1)
    reList.append(res2)
    return reList


my_ls = []
hap,sub =0,0

my_ls = multi(100,200)

hap = my_ls[0]
sub = my_ls[1]
print("multi()에서 돌려준 값 ==> %d, %d"%(hap,sub))

print("\n과제 21\n")

def para2_func(v1,v2):
    result = 0
    result = v1 +v2
    return result

def para3_func(v1,v2,v3):
    result = 0
    result = v1 +v2 +v3
    return result

hap =0
hap =(para2_func(10,20))
print("매개변수가 2개인 함수를 호출한 결과==> %d"%hap)
hap =(para3_func(10,20,30))
print("매개변수가 3개인 함수를 호출한 결과==> %d"%hap)

print("\n과제 22\n")

def para_func(v1,v2,v3=0):
    result = 0
    result = v1+v2+v3
    return result

hap =0

hap = para_func(10,20)
print("매개변수가 2개인 함수를 호출한 결과==> %d"%hap)

hap = para_func(10,20,30)
print("매개변수가 3개인 함수를 호출한 결과==> %d"%hap)

print("\n과제 23\n")

def para_func(v1,v2,v3=0,v4=0,v5=0,v6=0,v7=0,v8=0,v9=0,v10=0):
    result = 0
    result = v1+v2+v3+v4+v5+v6+v7+v8+v9+v10
    return result

hap =0

hap = para_func(10,20)
print("매개변수가 2개인 함수를 호출한 결과==> %d"%hap)

hap = para_func(10,20,30,40,50,60,70,80,90,100)
print("매개변수가 10개인 함수를 호출한 결과==> %d"%hap)


print("\n과제 24\n")
def para_func(*para):
    result =0
    for num in para:
        result = result +num
    return result

hap =0
hap = para_func(10,20)
print("매개변수가 2개인 함수를 호출한 결과==> %d"%hap)
hap = para_func(10,20,30)
print("매개변수가 3개인 함수를 호출한 결과==> %d"%hap)

hap = para_func(10,20,30,40,50,60,70,80,90,100)
print(hap)

print("\n과제 25\n")

import random

def getNuber():
    return random.randrange(1,46)


lotto = []
num = 0

print("**로또 추첨을 시작합니다. **\n");

while True:
    num = getNuber()
    if lotto.count(num) == 0:
        lotto.append(num)

    if len(lotto) >=6:
        break
print("추첨된 로또 번호 ==> ",end='')
lotto.sort()

for i in range(0,6):
    print("%d "%lotto[i],end='')


print("\n과제 26\n")

import Module1
Module1.func1()
Module1.func2()
Module1.func3()


import random
from tkinter.simpledialog import *

def getString():
    reStr = ''
    reStr = askstring('문자열 입력','거북이 쓸 문자열을 입력')
    return reStr

def getRGB():
    r,g,b = 0,0,0
    r = random.random()
    g = random.random()
    b = random.random()
    return(r,g,b)

def getXYAS(sw,sh):
    x,y,angle,size = 0,0,0,0
    x = random.randrange(-sw/2,sw/2)
    y = random.randrange(-sh/2,sh/2)
    angle = random.randrange(0,360)
    size = random.randrange(10,50)
    return [x,y,angle,size]


import turtle as tt

inStr = ''
swidth,sheight = 300,300
tX,tY,tAngle,tSize = [0] * 4

tt.title("거북이 글자쓰기(모듈버전)")
tt.shape('turtle')
tt.setup(width=swidth+50,height =sheight+50)
tt.screensize(swidth,sheight)
tt.penup()
tt.speed(5)

inStr = getString()
for ch in inStr:
    tX,tY,tAngle,txtSize = getXYAS(swidth,sheight)
    r,g,b = getRGB()
    tt.goto(tX,tY)
    tt.left(tAngle)

    tt.pencolor((r,g,b))
    tt.write(ch,font=("맑은고딕",txtSize,'bold'))

tt.done()