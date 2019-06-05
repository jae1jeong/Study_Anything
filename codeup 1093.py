a = input()
b = input().split() # 공백 단위로 입력 받는다.

n = int(a) # 입력 받은 a를 int로 바꾸고
arr = [] # 리스트 선언
for i in range(24):
    arr.append(0) # 0으로 다 초기화
for i in range(n):# n 개수만큼
    arr[int(b[i])] +=1 # int로 변환한 b의 원소 값만큼 arr 원소 값을 1씩 더해준다.

for i in range(1,24): # arr 출력
    print(arr[i],end= ' ')