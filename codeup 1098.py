
h,w = map(int,input().split())
n = int(input())

m = []
for i in range(h):
    m.append([])
    for j in range(w):
        m[i].append(0)

for _ in range(n):
    l,d,x,y = map(int,input().split())

    if d == 0: # 가로
        i = 0
        for i in range(l):
            m[x-1][y+i-1] = 1 # 길이만큼 반복 ,입력한 좌표 부터 i를 더해나가면서 1
            i +=1
    elif d == 1:# 세로
        i = 0
        for i in range(l):
            m[x+i-1][y-1] = 1
            i +=1
    else:
        break

for i in range(h):
    for j in range(w):
        print(m[i][j],end=' ')
    print()





