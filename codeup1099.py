


m = [[int(x)for x in input().split()]for raw in range(10)]



def move(x,y):
    if m[x][y+1] == 1:
        if m[x+1][y] == 1:
            return
        elif m[x+1][y] == 0:
            m[x+1][y] = 9
            move(x+1,y)
        elif m[x+1][y] == 2:
            m[x+1][y] = 9
            return
        else:
            None
    else:
        m[x][y+1] = 9
        move(x,y+1)


m[1][1] = 9
move(1,1)

for i in range(10):
    for j in range(10):
        print(m[i][j],end= ' ')
    print()