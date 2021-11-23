#1-masala
# a = int(input("a = "))
# b = int(input("b = "))
# while a > b:
#     a -= b
# print(a)

#2-masala
# a = int(input("a = "))
# b = int(input("b = "))
# k = 0
# while a > b:
#     a -= b
#     k += 1
# print(k)

#3-masala
# n = int(input("n = "))
# k = int(input("k = "))
# a = 0
# while n > k:
#     n -= k
#     a += 1
# print(k, n)

#4-masala
# n = int(input("n = "))
# a = bool
# while n > 1 :
#     a = n % 3 == 0
#     n = n / 3
# print(a)

#5-masala
# n = int(input("n = "))
# k = 0
# while n > 1 and n % 2 == 0:
#     n /= 2
#     k += 1
# print(k)

#6-masala
# n = int(input("n = "))
# f = 1
# while n > 1:
#     f *= n
#     n -= 2
# print(f)

#7-masala
# n = int(input("n = "))
# k = 1
# while k <= n / k:
#     k += 1
# print(k)

#8-masala
# n = int(input("n = "))
# k = n
# while k >= n / k:
#     k -= 1
# print(k)

#9-masala
# n = int(input("n = "))
# k = 0
# while n > 1:
#     n /= 3
#     k += 1
# print(k)

#10-masala
# n = int(input("n = "))
# k = 0
# while n > 1:
#     n /= 3
#     k += 1
# print(k-1)

#11-masala
# n = int(input("n = "))
# s = 0
# k = 0
# while s < n:
#     k += 1
#     s += k
# print(k, s)

#12-masala
# n = int(input("n = "))
# s = 0
# k = 0
# while s < n - k:
#     k += 1
#     s += k
# print(k, s)

#13-masala
# a = float(input("a = "))
# k = 0
# s = 0
# while s <= a:
#     k += 1
#     s += 1 / k
# print(k, s)

#14-masala
# a = float(input("a = "))
# k = 1
# s = 0
# while s < a - 1 / k:
#     s += 1 / k
#     k += 1
# print(k-1, s)

#15-masala
# a = 1000
# p = float(input("p = "))
# k = 0
# while a <= 1100:
#     a *= (p + 100) / 100
#     k += 1
# print(k, a)

#16-masala
# a = 10
# p = float(input("p = "))
# k = 1
# s = a
# while s < 40:
#     a *= (p +100) / 100
#     s += a
#     k += 1
# print(k, s)

#17-masala
# n = int(input("n = "))
# while n > 0:
#     print(n % 10, end = " ")
#     n //= 10

#18-masala
# n = int(input("n = "))
# k, s = 0, 0
# while n > 0:
#     s += n % 10
#     n //= 10
#     k += 1
# print(s, k)

#19-masala
# n = int(input("n = "))
# s = 0
# while n > 0:
#     s = 10*s
#     s += n % 10
#     n //= 10
# print(s)

#20-masala
# n = int(input("n = "))
# a = bool
# while n > 0:
#     a = n % 10 == 2
#     n //= 10
#     break
# print(a)

#21-masala
# n = int(input("n = "))
# while n > 0:
#     a = n % 2 == 1
#     if (n % 2 == 1):
#         break
#     else:
#         n //= 10
# print(a)

#22-masala
# n = int(input("n = "))
# k = 2
# a = bool
# while k < n:
#     a = n % k != 0
#     if n % k == 0:
#         break
#     k += 1
# print(a)

#23-masala
# a = int(input("a = "))
# b = int(input("b = "))
# s = 0
# if a > b:
#     s = b
# else:
#     s = a
# while s > 0:
#     if a % s == 0 and b % s == 0:
#         break
#     else:
#         s -= 1
# print(s)

#24-masala
# n = int(input('n = '))
# f1, f2 = 1, 1
# f = f2
# while f < n:
#     f = f1 + f2
#     f1, f2 = f2, f
# print(n == f)

#25-masala
# n = int(input('n = '))
# f1, f2 = 1, 1
# f = 0
# while f <= n:
#     f = f1 + f2
#     f1, f2 = f2, f
# print(f)

#26-masala
# n = int(input('n = '))
# f1, f2 = 1, 1
# f = 0
# while f < n:
#     f = f1 + f2
#     f1, f2 = f2, f
# if f == n:
#     print(f1, f1 + f2)
# else:
#     print(0)

#27-masala
# n = int(input("n = "))
# f1, f2 = 1, 1
# k = 2
# f = 0
# while f < n:
#     f = f1 + f2
#     f1, f2 = f2, f
#     k += 1
# if n == f:
#     print(k)
# else:
#     print(0)

#28-masala
# e = float(input("e = "))
# k = 2
# a1 = 2
# a2 = 2 + 1 / a1
# while abs(a2 - a1) >= e:
#     a1 = a2
#     a2 = 2 + 1 / a1
#     k += 1
# print(k, a1, a2)

#29-masala
# e = float(input("e = "))
# a1, a2 = 1, 2
# a = (a1 + 2 * a2) / 3
# k = 3
# while abs(a - a2) > e:
#     a1, a2 = a2, a
#     a = (a1 + 2 * a2) / 3
#     k += 1
# print(k, a2, a)

#30-masala
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# n = 0
# while a >= c:
#     b1 = b
#     while b1 >= c:
#         b1 -= c
#         n += 1
#     a -= c
# print(n)