#1-masala
# def sign(x):
#     if x > 0:
#         return 1
#     elif x == 0:
#         return 0
#     else:
#         return -1
# x = int(input("x = "))
# print(sign(x))

#2-masala
# def RootsCount(a, b, c):
#     d = b**2 - 4*a*c
#     if d > 0:
#         return 2
#     elif d == 0:
#         return 1
#     else:
#         return 0
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# print(RootsCount(a, b, c))

#3-masala
# from math import pi
# def CirsleS(r):
#     return pi * r ** 2
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# print(CirsleS(a), CirsleS(b), CirsleS(c))

#4-masala
# from math import pi
# def RingS(r1, r2):
#     s = pi * (r1**2 - r2**2)
#     return s
# a1, a2 = 4, 2
# b1, b2 = 2, 1
# c1, c2 = 3, 2
# print(RingS(a1, a2))
# print(RingS(b1, b2))
# print(RingS(c1, c2))

#5-masala
# def Range(a, b):
#     if a > b:
#         return 0
#     else:
#         s = 0
#         while b >= a:
#             s += b
#             b -= 1
#         return s
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# print(Range(a, b))
# print(Range(b, c))

#6-masala
# def Calc(a, b, op):
#     if op == 1:
#         return a - b
#     elif op == 2:
#         return a * b
#     elif op == 3:
#         return a / b
#     else:
#         return a + b
# a = int(input("a = "))
# b = int(input("b = "))
# n1 = 1
# n2 = 2
# n3 = 4
# print(Calc(a,b,n1),Calc(a,b,n2),Calc(a,b,n3))

#7-masala
# def Quarter(x, y):
#     if x > 0 and y > 0:
#         return 1
#     elif x > 0 and y < 0:
#         return 4
#     elif x < 0 and y > 0:
#         return 2
#     else:
#         return 3
# print(Quarter(2, 3),Quarter(-2, 3),Quarter(2, -3), sep = "\n")

#8-masala
# def Even(k):
#     if k % 2 == 0:
#         return 1
#     else:
#         return 0
# n = int(input("n = "))
# k = 0
# while n > 0:
#     k += Even(n)
#     n -= 1
# print(k)

#9-masala
# from math import sqrt
# def IsSquare(k):
#     if sqrt(k) - sqrt(k) // 1 == 0:
#         return 1
#     else:
#         return 0
# n = int(input("n = "))
# k = 0
# while n > 1:
#     k += IsSquare(n)
#     n -= 1
# print(k)

#10masala 5ga karrali sonlar uchun
# def isPowerS(k):
#     if k % 5 == 0:
#         return 1
#     else:
#         return 0
# n = int(input("n = "))
# k = 0
# while n > 1:
#     k += isPowerS(n)
#     n -= 1
# print(k)

#10-masala 5ning darajalari uchun yechim
# def isPowerS(k):
#     while k >= 5:
#         k /= 5
#     if k == 1:
#         return 1
#     else:
#         return 0
# n = int(input("n = "))
# k = 0
# while n >= 1:
#     k += isPowerS(n)
#     n -= 1
# print(k)

#11-masala
# def IsPowerN(k, n):
#     while n >= k:
#         n /= k
#     if n == 1:
#         return 1
#     else:
#         return 0
# n = int(input("n = "))
# k = int(input("k = "))
# s = 0
# for i in range(1,n+1):
#     s += IsPowerN(k, i)
# print(s)

#12-masala
# def IsPrime(n):
#     k = 0
#     while n > 0:
#         s = 0
#         for i in range(2, n + 1):
#             if n % i == 0:
#                 s += 1
#         if s == 1:
#             k += 1
#         n -= 1
#     return k
# n = int(input('n = '))
# print(IsPrime(n))

#13-masala
# def Digit_Count(k):
#     s = 0
#     while k > 0:
#         k //= 10
#         s += 1
#     return s
# k1, k2, k3, k4, k5 = 12, 1, 36, 121, 3723748
# print(Digit_Count(k1), Digit_Count(k2), Digit_Count(k3), Digit_Count(k4), Digit_Count(k5))

#14-masala
# def Digit(k, n):
#     s = k
#     p = 0
#     while s > 0:
#         s //= 10
#         p += 1
#     if p >= n:
#         while n > 1:
#             k //= 10
#             n -= 1
#         return k % 10
#     else:
#         return -1
# b = int(input('b = '))
# for i in range(5):
#     k = int(input('k = '))
#     print(Digit(k, b))

#15-masala
# def Ispalindron(k):
#     a = k
#     s = 0
#     while a > 0:
#         s *= 10
#         s += a % 10
#         a //= 10
#     if s == k:
#         return 1
#     else:
#         return 0
# k = int(input('k = '))
# print(Ispalindron(k))

#16-masala
# from math import pi
# def DegToRad(d):
#     return d / 180 *pi
# for i in range(4):
#     a = float(input('a = '))
#     print(DegToRad(a))

#17-masala
# from math import pi
# def DRadtodeg(r):
#     return r / pi * 180
# b = [0, 0, 0, 0]
# for i in range(4):
#     b[i] = float(input('r = '))
# for i in range(4):
#     print(DRadtodeg(b[i]))

#18-masala
# def Fact(n):
#     s = 1
#     while n > 0:
#         s *= n
#         n -= 1
#     return s
# a = [0, 0, 0, 0, 0]
# for i in range(5):
#     a[i] = int(input('a = '))
# for i in range(5):
#     print(Fact(a[i]))

#19-masala
# def Fact2(n):
#     s = 1
#     while n > 0:
#         s *= n
#         n -= 2
#     return s
# a = [0, 0, 0, 0, 0]
# for i in range(5):
#     a[i] = int(input('a = '))
# for i in range(5):
#     print(Fact2(a[i]), end = " ")

#20-masala
# def Fib(n):
#     f1, f2 = 1, 1
#     f = f2
#     while n >= 2:
#         f = f1 + f2
#         f1, f2 = f2, f
#         n -= 1
#     if n == 1 or n == 2:
#         return f1
#     else:
#         return f
# n1, n2, n3, n4, n5 = int(input('n1=')),int(input('n2=')),int(input('n3=')),int(input('n4=')),int(input('n5='))
# print(Fib(n1))
# print(Fib(n2))
# print(Fib(n3))
# print(Fib(n4))
# print(Fib(n5))