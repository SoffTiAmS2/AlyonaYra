from itertools import product


cnt = 0
for i in product("012345678", repeat=5):
    a = "".join(i)
    if(a.count('0') == 1 and a[0] != '0'):
        if not('10' in a or '30' in a or '50' in a or '70' in a or '01' in a or '03' in a or '05' in a or '07' in a):
            cnt += 1
            print(a)

print(cnt)