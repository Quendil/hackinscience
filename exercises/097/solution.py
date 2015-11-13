def love_meet(l, m):
    print(set(l).intersection(set(m)))

def affair_meet(l, m, n):
    print(set(m).intersection(set(n)).difference(set(l)))
