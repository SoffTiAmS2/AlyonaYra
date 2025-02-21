print("19-----------------")

def f(x, y, p):
    if x + y >= 174 and p == 3: return True
    if x + y < 174 and p == 3: return False
    if x + y >= 174: return False

    # if p%2 == 0:
    return f(x+1, y, p+1) or f(x, y+1, p+1) or f(x+3, y, p+1) or f(x, y+3, p+1) or f(x*2, y, p+1) or f(x, y*2, p+1)
    # else:
    #     return f(x+1, y, p+1) and f(x, y+1, p+1) and f(x+3, y, p+1) and f(x, y+3, p+1) and f(x*2, y, p+1) and f(x, y*2, p+1)


for i in range(1, 155):
    if f(19, i, 1):
        print(i)
        break

print("20-----------------")

def f(x, y, p):
    if x + y >= 174 and p == 4: return True
    if x + y < 174 and p == 4: return False
    if x + y >= 174: return False

    if p%2 == 1:
        return f(x+1, y, p+1) or f(x, y+1, p+1) or f(x+3, y, p+1) or f(x, y+3, p+1) or f(x*2, y, p+1) or f(x, y*2, p+1)
    else:
        return f(x+1, y, p+1) and f(x, y+1, p+1) and f(x+3, y, p+1) and f(x, y+3, p+1) and f(x*2, y, p+1) and f(x, y*2, p+1)

cnt = 0
for i in range(1, 155):
    if f(19, i, 1):
        print(i)
        cnt += 1
        if(cnt == 2):
            break
        
print("21-----------------")

def f(x, y, p):
    if x + y >= 174 and (p == 5 or p == 3): return True
    if x + y < 174 and p == 5: return False
    if x + y >= 174: return False

    if p%2 == 0:
        return f(x+1, y, p+1) or f(x, y+1, p+1) or f(x+3, y, p+1) or f(x, y+3, p+1) or f(x*2, y, p+1) or f(x, y*2, p+1)
    else:
        return f(x+1, y, p+1) and f(x, y+1, p+1) and f(x+3, y, p+1) and f(x, y+3, p+1) and f(x*2, y, p+1) and f(x, y*2, p+1)


for i in range(1, 155):
    if f(19, i, 1):
        print(i)

        
print("-----------------")

def f1(x, y, p):
    if x + y >= 174 and p == 3: return True
    if x + y < 174 and p == 3: return False
    if x + y >= 174: return False

    if p%2 == 0:
        return f1(x+1, y, p+1) or f1(x, y+1, p+1) or f1(x+3, y, p+1) or f1(x, y+3, p+1) or f1(x*2, y, p+1) or f1(x, y*2, p+1)
    else:
        return f1(x+1, y, p+1) and f1(x, y+1, p+1) and f1(x+3, y, p+1) and f1(x, y+3, p+1) and f1(x*2, y, p+1) and f1(x, y*2, p+1)


for i in range(1, 155):
    if f1(19, i, 1):
        print(i)

        