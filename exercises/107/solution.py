def select_student(l, v):
    a = []
    b = []
    c = []
    d = []
    import operator
    e = dict(l)
    for i in e:
        if e[i] > v:
            a.append(i)
            b.append(e[i])
        else:
            c.append(i)
            d.append(e[i])
    for i in range(0, len(a)):
        print('Accepted', [a[i], b[i]])
    for i in range(0, len(c)):
        print('Refused', [c[i], d[i]])
