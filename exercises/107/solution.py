def select_student(l, v):
    a = []
    b = []
    c = []
    d = []
    e = []
    f = []
    import operator
    z = dict(l)
    for i in z:
        if z[i] > v:
            a.append(i)
            b.append(z[i])
        else:
            c.append(i)
            d.append(z[i])
    for i in range(0, len(a)):
        m = a[i], b[i]
        e.append(list(m))
    for i in range(0, len(c)):
        n = c[i], d[i]
        f.append(list(n))
    e.sort(reverse=True, key=operator.itemgetter(1))
    f.sort(key=operator.itemgetter(1))
    g = {'Accepted': list(e), 'Refused': list(f)}
    return(g)
