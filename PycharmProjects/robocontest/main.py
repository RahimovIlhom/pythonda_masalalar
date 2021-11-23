# def Factorial(a):
#     return 1 if a==1 else a + Factorial(a-1)
# n = int(input())
# print(Factorial(n)%(n+1))
# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# x = a**b - c
# while x != d:
# 	if x>d:
# 		x = x - d
# 	else:
# 		d = d - x
# print(x)

# a, b = int(input()), int(input())
# c = (a + b) / 2
# d = (a * b) ** (1/2)
# print(c, d)
# if c > d: print(">")
# elif c < d: print("<")
# else: print("=")

a = [1, 1]
b = []
n = int(input("n = "))
for j in range(n):
    b.append(1)
    print(1, end=" ")
    for i in range(1+j):
        c = a[i]+a[i+1]
        print(c, end=" ")
        b.append(c)
    b.append(1)
    print(1)
    a.clear()
    a.append(b)
    b.clear()
