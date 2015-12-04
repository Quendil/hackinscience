def facto(x):
    s = 1
    if x == 0:
        print('1')
    if x < 0:
        print('opération impossible')
    if x > 0:
        for i in range(1, x + 1):
            s = s*i
        return s
