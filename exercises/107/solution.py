def select_student(l, v):
    a = []
    b = []
    import operator
    d = dict(l)
    for i in d:
        if d[i] > v:
            a.append(i)
            a.append(d[i])
        else:
            b.append(i)
            b.append(d[i])
    print(dict([('Accepted', a)]))
    print(dict([('Refused', b)]))
