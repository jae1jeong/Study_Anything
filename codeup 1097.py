import pprint
k  = [[int(x) for x in input().split()]for y in range(19)] # 19 x 19 2차원 행렬 입력


n = int(input()) # 횟수 입력

for i in range(n): #횟수 입력만큼 반복
    x,y = input().split()  # x와y를 입력 받아서

    for i in range(19): # 행
        if k[int(x) - 1][i] == 1: # x-1인 이유는 인덱스가 0부터 시작해서 1 빼기
            k[int(x) - 1][i] = 0
        else:
            k[int(x) - 1][i] = 1
    for j in range(19):# 열
        if k[j][int(y)-1] == 1: # y도 똑같음
            k[j][int(y)-1] = 0
        else:
            k[j][int(y)-1] = 1

for i in range(19): # 행렬을 출력 예시와 똑같게 출력하기
    for j in range(19):
        print(k[i][j],end=' ')
    print()



