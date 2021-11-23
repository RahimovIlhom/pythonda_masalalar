a = int(input())
b = a % 10
c = int(a / 10 % 10)
d = int(a / 100)
print(d * 100 + b * 10 +c)