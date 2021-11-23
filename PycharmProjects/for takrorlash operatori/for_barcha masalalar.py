#1-masala
# k = int(input("k = "))
# n = int(input("n = "))
# for i in range(n):
#     print(k, end = " ")

#2-masala
# k = int(input("k = "))
# n = int(input("n = "))
# if n > k:
#     for i in range(k, n+1):
#         print(i)
# else:
#     for i in range(k, n+1):
#         print(i)
# print(abs(n - k) + 1)

#3-masala
# k = int(input("k = "))
# n = int(input("n = "))
# if n > k:
#     for i in range(n, k-1, -1):
#         print(i)
# else:
#     for i in range(n, k-1, -1):
#         print(i)
# print(abs(n - k) + 1)

#4-masala
# a = float(input("a = "))
# for i in range(1,11):
#     print(a * i)

#5-masala
# a = float(input("a = "))
# for i in range(1, 11):
#     print(a * i / 10)

#6-masala
# a = float(input("a = "))
# for i in range(2, 11, 2):
#     print(a * (1 + i / 10))

#7-masala
# a = int(input("a = "))
# b = int(input("b = "))
# s = 0
# for i in range(a, b+1):
#     s += i
# print(s)

#8-masala
# a = int(input("a = "))
# b = int(input("b = "))
# s = 1
# for i in range(a, b+1):
#     s *= i
# print(s)

#9-masala
# a = int(input("a = "))
# b = int(input("b = "))
# s = 0
# for i in range(a, b+1):
#     s += i*i
# print(s)

#10-masala.
# n = int(input("n = "))
# s = 0
# for i in range(1,n+1):
#     s += i ** (-1)
# print(s)

#11-masala
# n = int(input("n = "))
# s = 0
# for i in range(n+1):
#     s += (n + i) ** 3
# print(s)

#12-masala
# n = int(input("n = "))
# p = 1
# for i in range(n+1):
#     p *= (1 + i / 10)
# print(p)

#13-masala
# n = int(input("n = "))
# p = 0
# for i in range(1,n+1):
#     p += (-1)**(i+1)*(1+i/10)
# print(p)

#14-masala
# n = int(input("n = "))
# s = 0
# for i in range(1, n+1):
#     s += (2 * i - 1)
#     print(s)

#15-masala
# a = float(input("a = "))
# n = int(input("n = "))
# p = 1
# for i in range(n):
#     p *= a
# print(p)

#16-masala
# a = float(input("a = "))
# n = int(input("n = "))
# p = 1
# for i in range(n):
#     p *= a
#     print(p)

#17-masala
# a = float(input("a = "))
# n = int(input("n = "))
# s = 0
# for i in range(n+1):
#     s += a ** i
# print(s)

#18-masala
# a = float(input("a = "))
# n = int(input("n = "))
# s = 0
# for i in range(n+1):
#     s += (-1)**i * a ** i
# print(s)

#19-masala
# n = float(input("n = "))
# p = 1
# for i in range(1, int(n+1)):
#     p *= i
# print(p)

#20-masala
# n = float(input("n = "))
# p = 1
# s = 0
# for i in range(1, int(n+1)):
#     p *= i
#     s += p
# print(s)

#21-masala
# n = int(input("n = "))
# p = 1
# s = 0
# for i in range(1, n+1):
#     p *= i
#     s += 1/p
# print(s+1)

#22-masala
# x = float(input("x = "))
# n = int(input("n = "))
# h, p = 1, 1
# s = 0
# for i in range(1, n+1):
#     h *= x
#     p *= i
#     s += h / p
# print(s+1)

#23-masala
# x = float(input("x = "))
# n = int(input("n = "))
# s = 0
# for i in range(1, n+1):
#     p, h = 1, 1
#     for k in range(1, 2*i):
#         p *= k
#         h *= x
#     s += (-1)**(i+1)*h / p
# print(s)

#24-masala
# x = float(input("x = "))
# n = int(input("n = "))
# s = 0
# for i in range(1, n+1):
#     p, h = 1, 1
#     for k in range(1, 2*i+1):
#         p *= k
#         h *= x
#     s += (-1)**(i)*h / p
# print(1+s)

#25-masala
# x = float(input("x = "))
# n = int(input("n = "))
# s = 0
# for i in range(1, n+1):
#     s += (-1)**(i-1) * x ** i / i
# print(s)

#26-masala
# x = float(input("x = "))
# n = int(input("n = "))
# s = 0
# for i in range(1, n+1):
#     s += (-1)**(i-1) * x ** (2*i-1) / (2 * i - 1)
# print(s)

#27-masala
# x = float(input("x = "))
# n = int(input("n = "))
# s = 0
# p, h = 1, 1
# for i in range(1,n+1):
#     h *= 2 * i - 1
#     p *= (2*i)*(2*i+1)
#     s += x**(2*i+1) * h / p
# print(s)

#28-masala
# x = float(input("x = "))
# n = int(input("n = "))
# s = 0
# p, h = 1, 1
# for i in range(1, n+1):
#     h *= x
#     p *= 2*i
#     s += (-1)**(n+1) * h / p
# print(s+1)

#29-masala
# a = float(input("a = "))
# b = float(input("b = "))
# n = int(input("n = "))
# h = (b - a) / n
# for i in range(n+1):
#     print(a + i * h)

#30-masala
# import math
# a = float(input("a = "))
# b = float(input("b = "))
# n = int(input("n = "))
# h = (b - a) / n
# y = 0
# for i in range(n+1):
#     y = 1 - math.sin(a + i * h)
#     print(y)

#31-masala
# n = int(input("a = "))
# a = 2
# for i in range(n):
#     a = 2 + 1 / a
#     print(a)

#32-masala
# n = int(input("a = "))
# a = 1
# for i in range(1,n+1):
#     a = (a + 1) / i
#     print(a)

#33-masala
# n = int(input("n = "))
# f1 = 1
# f2 = 1
# a = 0
# for i in range(n):
#     print(f2)
#     a = f2
#     f2 = f1 + f2
#     f1 = a

#34-masala
# n = int(input("n = "))
# a1 = 1
# a2 = 2
# a = 0
# print(a1, a2, sep = "\n")
# for i in range(n-2):
#     a = a2
#     a2 = (a1 + a2 * 2) / 2
#     a1 = a
#     print(a2)

#35-masala
n = int(input("n = "))
a1 = 1
a2 = 2
a3 = 3
print(a1, a2, a3, end = " ")
for i in range(3, n):
    s = a3
    p = a2
    a3 = a3 + a2 - 2 * a1
    a2 = s
    a1 = p
    print(a3, end = " ")


#27, 28, 30