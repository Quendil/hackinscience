def love_meet(l, m):
    return(set(l).intersection(set(m)))


def affair_meet(l, m, n):
    return(set(m).intersection(set(n)).difference(set(l)))
