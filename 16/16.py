a = [0] *2025
for n in range(2025):
    if n==1: a[n] = 1
    if n>1: a[n] = n * a[n-1]
print((2*a[2024] + a[2023])/a[2022])



from sys import setrecursionlimit
setrecursionlimit(3000)
def f(n):
    if n==1: 
        return 1
    if n>1: 
        return n*f(n-1)

print((2*f(2024) + f(2023))/f(2022))