#1-masala
# n = int(input('n = '))
# a = []
# b = 1
# while n > 0:
#     a.append(b)
#     n -= 1
#     b += 2
# print(a)

#2-masala
# n = int(input('n = '))
# a = []
# b = 2
# while n > 0:
#     a.append(b)
#     n -= 1
#     b *= 2
# print(a)

#3-masala
# n = int(input('n = '))
# a = int(input('a = '))
# d = int(input('d = '))
# b = [a]
# while n > 1:
#     a += d
#     b.append(a)
#     n -= 1
# print(b)

#4-masala
# n = int(input('n = '))
# b = int(input('b = '))
# q = int(input('q = '))
# a = [b]
# while n > 1:
#     b *= q
#     a.append(b)
#     n -= 1
# print(a)

#5-masala
# n = int(input('n = '))
# a = [1, 1]
# for i in range(2, n):
#     b = a[i-1] + a[i-2]
#     a.append(b)
# print(a)

#6-masala
# n = int(input('n = '))
# a = int(input('a = '))
# b = int(input('b = '))
# s = [a, b]
# c = a + b
# while n > 2:
#     s.append(c)
#     c *= 2
#     n -= 1
# print(s)

#7-masala
# n = int(input('n = '))
# a = []
# while n > 0:
#     b = int(input('sonni kiriting:'))
#     a.append(b)
#     n -= 1
# a.reverse()
# print(a)

#8-masala
# n =int(input('n = '))
# a = []
# m = n - 1
# while n > 0:
#     b = int(input())
#     a.append(b)
#     n -= 1
# k = 0
# while m >= 0:
#     if a[m] % 2 == 0:
#         print(a[m])
#         k += 1
#     m -= 1
# print(k)

#9-masala
# n =int(input('n = '))
# a = []
# m = n - 1
# while n > 0:
#     b = int(input())
#     a.append(b)
#     n -= 1
# k = 0
# c = []
# while m >= 0:
#     if a[m] % 2 == 1:
#         c.append(a[m])
#         k += 1
#     m -= 1
# c.sort()
# print(c, k)

#10-masala
# n =int(input('n = '))
# a = []
# m = n
# c = []
# d = []
# while n > 0:
#     b = int(input())
#     a.append(b)
#     n -= 1
# for i in range(m):
#     if a[i] % 2 == 0:
#         c.append(a[i])
#     else:
#         d.append(a[i])
# d.reverse()
# print(c)
# print(d)

#11-masala
# n =int(input('n = '))
# a = []
# k = int(input('k = '))
# for i in range(n):
#     b = int(input())
#     a.append(b)
# while k > 0:
#     k -= 1
#     print(a[k])

#12-masala
# n =int(input('n = '))
# a = []
# for i in range(n):
#     b = int(input())
#     a.append(b)
# for i in range(1, n, 2):
#     print(a[i])

#13-masala
# n = int(input('n = '))
# a = []
# for i in range(n):
#     b = int(input())
#     a.append(b)
# print(a[::-2])

#14-masala
# n = int(input('n = '))
# a = []
# for i in range(n):
#     b = int(input())
#     a.append(b)
# for i in range(1, n+1, 2):
#     print(a[i], end = " ")
# print(" ")
# for i in range(0, n, 2):
#     print(a[i], end = " ")

#15-masala
# n = int(input('n = '))
# a = []
# m = n - 1
# for i in range(n):
#     b = int(input())
#     a.append(b)
# if m % 2 == 0:
#     while m > 0:
#         print(a[m], end = " ")
#         m -= 2
# else:
#     while m > 0:
#         print(a[m-1], end = " ")
#         m -= 2
# print("")
# if n % 2 == 0:
#     while n > 0:
#         print(a[n-1], end = " ")
#         n -= 2
# else:
#     while n > 0:
#         print(a[n-2], end = " ")
#         n -= 2

#16-masala
# n = int(input('n = '))
# a = []
# for i in range(n):
#     b = int(input())
#     a.append(b)
# for i in range(n):
#     if i % 2 == 0:
#         j = i // 2
#         print(a[j], end=" ")
#     else:
#         j = n-1-(i-1)//2
#         print(a[j], end=" ")

#17-masala
# n = int(input('n = '))
# a = []
# for i in range(n):
#     b = int(input())
#     a.append(b)
# for i in range(n):
#     if i % 4 == 0 or i % 4 == 1:
#         j = (i+1)//2
#         print(a[j], end=" ")
#     else:
#         j = n-1-(i-1)//2
#         print(a[j], end=" ")

#18-masala
# a = [6, 8, 3, 2, 4]
# for i in range(4):
#     if a[i] < a[4]:
#         print(a[i])
#         break

#19-masala
# a = [6, 8, 3, 2, 4, 25, 25, 14, 36, 45, 9, 78, 25, 8, 89]
# x = None
# for i in range(len(a)):
#     if a[0] < a[i] < a[-1]:
#         x = i
# print(x)

#20-masala
# a = [7, 9, 3, 1, 5, 8]
# k = 3
# l = 4
# s = 0
# for i in range(k-1, l):
#     s += a[i]
# print(s)

#21-masala
# a = [7, 9, 3, 1, 5, 8]
# k = 3
# l = 4
# s = 0
# for i in range(k-1, l):
#     s += a[i]
# print(s/(l-k+1))

#22-masala
# a = [7, 9, 3, 1, 5, 8]
# k = 3
# l = 4
# s = 0
# for i in range(6):
#     if i < k-1 or i >= l:
#         s += a[i]
# print(s)

#23-masala 1-usul
# a = [7, 9, 3, 1, 5, 8]
# k = 3
# l = 4
# s = 0
# for i in range(len(a)):
#     if i < k-1 or i > l-1:
#         s += a[i]
# print(s/(len(a)-(l-k+1)))

#23-misol 2-usul
# a = [7, 9, 3, 1, 5, 8]
# k, l = 2, 4
# a = a[:k] + a[l+1:]
# print(sum(a) / len(a))

#24-masala
# a = [3, 8, 13, 18, 23, 28]
# d = a[1] - a[0]
# for i in range(5):
#     if a[i+1] - a[i] != d:
#         d = 0
# print(d)

#25-masala
# a = [16, 8, 4, 2]
# d = a[1] / a[0]
# for i in range(3):
#     if a[i+1] / a[i] != d:
#         d = 0
# print(d)

#26-masala
# a = [12, 9, 18, 3, 6]
# b = bool
# for i in range(4):
#     if a[i] % 2 == 0 and a[i+1] % 2 != 0:
#         b = b and 1
#     elif a[i] % 2 != 0 and a[i+1] % 2 == 0:
#         b = b and 1
#     else:
#         b = 0
#         print(i+1)
#         break
# if b == 1:
#     print(0)

#27-masala
# a = [7, -3, 1, -9, 3]
# b = bool
# for i in range(4):
#     if a[i] > 0 and a[i+1] < 0:
#         b = b and 1
#     elif a[i] < 0 and a[i+1] > 0:
#         b = b and 1
#     else:
#         b = 0
#         print(i+1)
#         break
# if b == 1:
#     print(0)

#28-masala
# a = [1, 6, 5, 3, 4, 5]
# b = a[0]
# for i in range(0, 5, 2):
#     if b > a[i]:
#         b = a[i]
# print(b)

#29-masala
# a = [1, 6, 5, 3, 4, 5]
# b = a[1]
# for i in range(1, 5, 2):
#     if b < a[i]:
#         b = a[i]
# print(b)

#30-masala
# a = [1, 6, 5, 3, 4, 5]
# k = 0
# for i in range(5):
#     if a[i] > a[i+1]:
#         print(i, end=" ")
#         k += 1
# print("\n", k)

#31-masala
# a = [1, 6, 5, 3, 4, 5]
# k = 0
# for i in range(1, 6):
#     if a[i-1] < a[i]:
#         print(i, end=" ")
#         k += 1
# print("\n", k)

#32-masala
# a = [1, 6, 5, 3, 4, 5, 6, 1, 3, 2, 4, 3]
# for i in range(1, len(a)-1):
#     if a[i-1] > a[i] and a[i] < a[i+1]:
#         print(i)
#         break

#33-masala
# a = [1, 6, 5, 3, 4, 5]
# for i in range(1, 5):
#     if a[i-1] < a[i] and a[i] > a[i+1]:
#         print(i, end=" ")

#34-masala
# a = [1, 6, 5, 3, 4, 5, 5, 96, 32, 21, 45, 89, 65, 75, 12]
# b = []
# k = 0
# for i in range(1, 14):
#     if a[i-1] > a[i] and a[i] < a[i+1]:
#         b.append(a[i])
#         k += 1
# c = b[0]
# for i in range(k):
#     if c < b[i]:
#         c = b[i]
# print(c)

#35-masala
# a = [1, 6, 5, 3, 4, 5, 5, 96, 32, 21, 45, 89, 65, 75, 12]
# b = []
# for i in range(1, len(a)-1):
#     if a[i-1] < a[i] and a[i] > a[i+1]:
#         b.append(a[i])
# print(min(b))


#36-masala
# a = [1, 6, 5, 3, 4, 5, 5, 96, 32, 21, 45, 89, 65, 75, 12]
# b = []
# k = 0
# for i in range(1, 14):
#     if a[i-1] < a[i] and a[i] > a[i+1]:
#         pass
#     elif a[i - 1] > a[i] and a[i] < a[i + 1]:
#         pass
#     else:
#         b.append(a[i])
#         k += 1
# c = b[0]
# for i in range(k):
#     if c < b[i]:
#         c = b[i]
# print(c)

#37-masala
# a = [1, 6, 5, 3, 4, 5, 96, 32, 21, 45, 89, 65, 75, 12]
# k, s = 0, 0
# for i in range(13):
#     if a[i] < a[i+1]:
#         k += 1
#     else:
#         if k > 0:
#             s += 1
#         k = 0
# if k > 0:
#     print(s+1)
# else:
#     print(s)

#38-masala
# a = [1, 6, 5, 3, 4, 5, 96, 32, 21, 45, 89, 65, 75, 12, 96, 32, 21, 45, 89, 65, 75, 12]
# k, s = 0, 0
# for i in range(len(a)-1):
#     if a[i] > a[i+1]:
#         k += 1
#     elif k > 0:
#         s += 1
#         k = 0
# if k > 0:
#     print(s+1)
# else:
#     print(s)

#39-masala
# a = [1, 6, 5, 3, 4, 5, 96, 32, 21, 45, 89, 65, 75, 12]
# k, s = 0, 0
# for i in range(13):
#     if a[i] > a[i+1]:
#         k += 1
#     else:
#         if k > 0:
#             s += 1
#         k = 0
# if k > 0:
#     s += 1
# k = 0
# for i in range(13):
#     if a[i] < a[i+1]:
#         k += 1
#     else:
#         if k > 0:
#             s += 1
#         k = 0
# if k > 0:
#     print(s+1)
# else:
#     print(s)

#40-masala
# r = float(input("r = "))
# a = [6, 1, 3, 2, 4, 3]
# d = abs(r - a[0])
# s = a[0]
# for i in range(5):
#     if d > abs(r - a[i]):
#         d = abs(r-a[i])
#         s = a[i]
# print(s)

#41-masala
# a = [6, 1, 3, 2, 4, 3]
# s = a[0] + a[1]
# b, c = 0, 1
# for i in range(1,5):
#     if s <= (a[i] + a[i+1]):
#         s += (a[i] + a[i + 1])
#         b, c = i, i+1
# print(b, c)

#42-masala
# r = float(input('r = '))
# a = [5, 1, 2, 1, 3, 7]
# b, c = 0, 1
# d = abs(a[0]+a[1]-r)
# for i in range(1,len(a)-1):
#     x = abs(a[i] + a[i+1] - r)
#     if d >= x:
#         d = x
#         b, c = i, i+1
# print(b, c)

#43-masala
# a = [1, 3, 4, 6, 7, 9]
# if a == sorted(a) or a == sorted(a,reverse=true):
#     print(a[::2])

#44-masala
# a = [5, 1, 2, 1, 3, 7]
# for i in range(5):
#     for k in range(i+1, 6):
#         if a[i] == a[k]:
#             print(i, k)

#45-masala
# a = [5, 1, 2, 1, 3, 7]
# d = abs(a[0] - a[1])
# b, c = 0, 1
# for i in range(5):
#     for k in range(i+1, 6):
#         if d >= abs(a[i] - a[k]):
#             d = abs(a[i] - a[k])
#             b, c = i, k
# print(b, c)

#46-masala
# r = float(input('r = '))
# a = [5, 1, 2, 1, 3, 7]
# d = abs(r - (a[0] + a[1]))
# b, c = 0, 1
# for i in range(5):
#     for k in range(i+1, 6):
#         if d >= abs(r - (a[i] + a[k])):
#             d = abs(r - (a[i] + a[k]))
#             b, c = i, k
# print(b, c)

#47-masala
# a = [5, 1, 2, 4, 3, 7, 1, 5, 10]
# b = set(a)
# b = list(b)
# print(len(b))

#48-masala 1-usul
# a = [3, 1, 2, 2, 2, 1, 2, 2]
# n = 0
# for i in range(len(a)-1):
#     m = 0
#     for k in range(i+1, len(a)):
#         if a[i] == a[k]:
#             m += 1
#     if n < m:
#         n = m
# print(n+1)

#48-masala 2-usul
# a = [3, 1, 2, 2, 2, 1]
# z = list(set(a))
# b = []
# for i in z:
#     b.append(a.count(i))
# print(max(b))

#49-masala
# a = [5, 2, 1, 4, 3, 6, 1]
# b = 0
# for i in range(len(a)-1):
#     if a[i] <= len(a):
#         for k in range(i+1, len(a)):
#             if a[i] == a[k] or a[k] > len(a):
#                 b = k
#                 break
#     else:
#         b = k
#         break
# print(0 if b == 0 else b)

#50-masala
# n = int(input('n = '))
# a = []
# s = 0
# for i in range(n):
#     b = int(input())
#     a.append(b)
# for i in range(n-1):
#     for k in range(i+1, n):
#         if a[i] > a[k]:
#             s += 1
# print(s)

#51-masala
# a = [3, 5, 9, 6, 1]
# b = [2, 5, 7, 4, 9]
# for i in range(5):
#     if a[i] != b[i]:
#         a[i], b[i] = b[i], a[i]
#         print(a[i], end=" ")
# print()
# for i in range(5):
#     if a[i] != b[i]:
#         print(b[i], end=" ")

#52-masala
# a = [3, 5, 9, 6, 1]
# b = []
# for i in range(5):
#     if a[i] < 5:
#         b.append(2*a[i])
#     else:
#         b.append(a[i]/2)
# print(b)

#53-masala
# a = [3, 5, 9, 6, 1]
# b = [2, 5, 7, 4, 9]
# c = []
# for i in range(5):
#     if a[i] > b[i]:
#         c.append(a[i])
#     else:
#         c.append(b[i])
# print(c)

#54-masala
# a = [8, 5, 9, 6, 1]
# b = []
# k = 0
# for i in range(5):
#     if a[i] % 2 == 0:
#         b.append(a[i])
#         k += 1
# print(k, b)

#55-masala
# a = [8, 5, 9, 6, 1]
# b = []
# k = 0
# for i in range(0,5,2):
#     b.append(a[i])
#     k += 1
# print(k, b)

#56-masala
# a = [1, 3, 7, 4, 5, 8, 6, 9, 2]
# b = []
# k = 0
# for i in range(2,9,3):
#     b.append(a[i])
#     k += 1
# print(k, b)

#57-masala
# a = [2, 4, 8, 7, 3, 9]
# b = []
# for i in range(1, 6, 2):
#     b.append(a[i])
# for i in range(0,6,2):
#     b.append(a[i])
# print(b)

#58-masala
# a = [2, 4, 8, 7, 3, 9]
# b = []
# s = 0
# for i in range(6):
#     s += a[i]
#     b.append(s)
# print(b)

#59-masala
# a = [2, 4, 6, 8, 10, 12]
# b = []
# s = 0
# for i in range(6):
#     s += a[i]
#     b.append(s/(i+1))
# print(b)

#60-masala
# a = [2, 4, 6, 8, 10, 12]
# b = []
# s = 0
# for i in range(6):
#     s += a[i]
# for i in range(6):
#     b.append(s)
#     s -= a[i]
# print(b)

#61-masala
# a = [2, 4, 6, 8, 10, 12]
# b = []
# s = 0
# for i in range(6):
#     s += a[i]
# for i in range(6):
#     b.append(s/(6-i))
#     s -= a[i]
# print(b)

# 62-masala
# a = [-2, 8, -4, 3, 7]
# b, c = [], []
# k, l =0, 0
# for i in range(5):
#     if a[i] > 0:
#         b.append(a[i])
#         k += 1
#     else:
#         c.append(a[i])
#         l += 1
# print(k, b)
# print(l, c)

#63-masala
# a = [0, 2, 4, 6, 8]
# b = [1, 3, 5, 7, 9]
# c = []
# c.extend(a)
# c.extend(b)
# c.sort()
# print(c)

#64-masala
# n = int(input("n = "))
# a, b, c = [], [], []
# for i in range(n):
#     x = int(input("a = "))
#     y = int(input("b = "))
#     z = int(input("c = "))
#     a.append(x)
#     b.append(y)
#     c.append(z)
# d = []
# d.extend(a)
# d.extend(b)
# d.extend(c)
# d.sort(reverse = bool(1))
# print(d)