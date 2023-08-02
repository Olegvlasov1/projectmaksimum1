from math import sqrt
a = 1
b = 1
c = 1
n1 = []
n2 = []
n3 = []
while c < 20:
    c = sqrt(a**2 + b**2)
    if a < 20 and a + b > c and b + c > a and a + c > b:
        a += 1
    if b < 20 and a + b > c and b + c > a and a + c > b:
        a = 0
        b += 1
    n1.append(c)
    n2.append(a)
    n3.append(b)
    print(n1, n2, n3)