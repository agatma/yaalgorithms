# (2n)! / n! * (n+1)!

def fac(n):
    return 1 if n == 0 else fac(n-1) * n

n = int(input())

print(int(fac(2*n)/(fac(n)*fac(n+1))))