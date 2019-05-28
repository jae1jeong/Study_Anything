
#int: {0:d}, bin:{0:b}, oct{0:o},hex{0:x} 대문자로 받고 싶으면 {}안에 있는 문자를 대문자로 바꾸면 대문자로 출력 oct() 8진수 변환 ,hex() 16진수 변환 함수 int(data,8) 8진수
# 아스키 코드 변환 A = chr(65) ord("A") = 65
# 몫 // 나머지 %

a = list(map(int,input().split()))

for i in range(len(a)):
    if a[i] == 0:
        print(0)
        break
    else:
        print(a[i])
        i = i +1