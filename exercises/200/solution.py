def is_prime(x):
    n = 2
    s = 0
    if x == 2:
        return(True)
    else:
        while n < x:
            if x % n == 0:
                s = 1
            n = n + 1
        if s == 1:
            return(False)
        else:
            return(True)
