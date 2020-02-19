n = int(input())
for i in range(1,n+1):
    case = int(input())
    print("Case ",i,":",end='')
    for i in range(1, case+1):
        if case % i == 0:
            print(' ', i,end='')
    if i == n:
        break
    print('')