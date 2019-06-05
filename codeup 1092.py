
a,b,c = map(int,input().split())



t_num = max(a,b,c)
while t_num:
    if t_num % a ==0 and t_num % b ==0 and t_num % c ==0:
        print(t_num)
        break
    t_num +=1