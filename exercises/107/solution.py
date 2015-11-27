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
    m = a[0], b[0]
    n = c[0], d[0]
    for i in range(1, len(a)):
        m = m, [a[i], b[i]]
    for i in range(0, len(c)):
        n = n, [c[i], d[i]]
    print('Accepted', m)
    print('Refused', n)
