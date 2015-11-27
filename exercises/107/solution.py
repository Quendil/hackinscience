def select_student(l, v):
    a = []
    b = []
    c = []
    d = []
    y = []
    z = []
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
    y.append(list(m))
    z.append(list(n))
    for i in range(1, len(a)):
        m = a[i], b[i]
        y.append(list(m))
    for i in range(0, len(c)):
        n = c[i], d[i]
        z.append(list(n))
    print('Accepted', y)
    print('Refused', z)
