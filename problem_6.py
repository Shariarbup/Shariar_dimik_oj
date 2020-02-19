n = int(input())

for i in range(1, n+1):
    case = int(input())
    lsb = case % 10
    case =case / 10
    for i in range(4):
        
        rem = case % 10
        div = case / 10
        if div == 0:
            # ss = lsb + rem
            break
    print('Sum = ',format(lsb + rem))
    