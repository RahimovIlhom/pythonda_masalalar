x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())
a = ((x2 - x1)**2 + (y2 - y1)**2) ** (1 / 2)
b = ((x3 - x1)**2 + (y3 - y1)**2) ** (1 / 2)
c = ((x3 - x2)**2 + (y3 - y2)**2) ** (1 / 2)
P = a + b + c
p = P / 2
s = ((p - a) * (p - b) * (p - c))
print(int(P), int(s))

