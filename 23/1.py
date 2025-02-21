def f(x, p, de):
    if(x > 1000): return 0
    if(p == 9):
        if(x >= 99):
            de += [x]
            return 1
        else: return 0
    return f(x+3, p+1, de) + f(x+4, p+1, de) + f(x*2, p+1, de)

de = []
f(1, 0, de)
print(len(set(de)))
    