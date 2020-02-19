n = int(input())
for i in range(n+1):
    if i == n:
        break
    case = int(input())
    for j in range(1, case+1):
        for k in range(1, case+1):
            print('*', end='')
            if k == case:
                print('')
                break
        if j == case:
            break
    
    # print('')