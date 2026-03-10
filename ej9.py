def suc_rec(n):
    if n == 1:
        return n
    elif n % 2 == 0:
        return suc_rec(n // 2)
    else:
        return suc_rec(3*n + 1)

print(suc_rec(10))
