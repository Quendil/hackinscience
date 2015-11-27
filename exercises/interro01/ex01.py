def affComb():
    for i in range(0, 10):
        for j in range(0, 10):
            for k in range(0, 10):
                a = str(i)+str(j)+str(k)
                if a == '999':
                    print(a)
                else:
                    print(a, end=', ')
