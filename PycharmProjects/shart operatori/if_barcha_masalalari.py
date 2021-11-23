#1-masala
#a = int(input("a = "))
#if a > 0:
#    a += 1
#print(a)

#2-masala
# a = int(input("a = "))
# if a < 0:
#     print(a + 1)
# else: print(a - 2)

#3-masala
# a = int(input("a = "))
# if a < 0:
#     a -= 2
# elif a == 0:
#     a = 10
# print(a)

#4-masala
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# d = 0
# if a > 0:
#     d += 1
# if b > 0:
#     d += 1
# if c > 0:
#     d += 1
# print(d)

#5-masala
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# d, f = 0, 0
# if a > 0:
#     d += 1
# else: f += 1
# if b > 0:
#     d += 1
# else: f += 1
# if c > 0:
#     d += 1
# else: f += 1
# print(d)
# print(f)

#6-masala
# a = int(input("a = "))
# b = int(input("b = "))
# if a > b:
#     print(a)
# else: print(b)

#9-masala
# x = float(input("x = "))
# y = float(input("y = "))
# if(x > y):
#     a = x
#     b = y
# else:
#     a = y
#     b = x
# print(a,b)

#10-masala
# x = float(input("x = "))
# y = float(input("y = "))
# if x != y:
#     x = x + y
#     y = x
# else:
#     x, y = 0, 0
# print(x, y)

#11-masala
# a = int(input("a = "))
# b = int(input("b = "))
# if a != b:
#     if a > b:
#         b = a
#     else: a = b
# else: a, b = 0, 0
# print(a, b)

#12-masala
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# if a > b:
#     if b > c:
#         print(c)
#     else: print(b)
# elif a > c:
#     if b > c:
#         print(c)
#     else: print(b)
# else: print(a)

#13-masala
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# if a > b > c or a < b < c:
#     print(b)
# elif a > c > b or a < c < b:
#     print(c)
# elif b > a > c or b < a < c:
#     print(a)

#14-masala
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# if a > b > c:
#     print(c, a)
# elif a < b < c:
#     print(a, c)
# elif a > c > b:
#     print(b, a)
# elif a < c < b:
#     print(a, b)
# elif b > a > c:
#     print(c, b)
# elif b < a < c:
#     print(b, c)

#15-masala
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# if a > b > c:
#     print(a + b)
# elif a < b < c:
#     print(b + c)
# elif a > c > b:
#     print(a + c)
# elif a < c < b:
#     print(b + c)
# elif b > a > c:
#     print(a + b)
# elif b < a < c:
#     print(a + c)

#16-masala
# a = float(input("a = "))
# b = float(input("b = "))
# c = float(input("c = "))
# if a < b < c:
#     a *= 2
#     b *= 2
#     c *= 2
# else:
#     a = 1 / a
#     b = 1 / b
#     c = 1 / c
# print(a, b, c)


#17-masala
# a = float(input("a = "))
# b = float(input("b = "))
# c = float(input("c = "))
# if a < b < c or a > b > c:
#     a *= 2
#     b *= 2
#     c *= 2
# else:
#     a = -a
#     b = -b
#     c = -c
# print(a, b, c)

#18-masala
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# if (a < 0 and b > 0 and c > 0) or (a > 0 and b < 0 and c < 0):
#     print(1)
# if (a < 0 and b > 0 and c < 0) or (a > 0 and b < 0 and c > 0):
#     print(2)
# if (a > 0 and b > 0 and c < 0) or (a < 0 and b < 0 and c > 0):
#     print(3)

#19-masala
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# d = int(input("d = "))
# if a % 2 != b % 2 == c % 2 == d % 2:
#     print(1)
# if b % 2 != a % 2 == c % 2 == d % 2:
#     print(2)
# if c % 2 != a % 2 == b % 2 ==  d % 2:
#     print(3)
# if d % 2 != a % 2 == b % 2 == c % 2 :
#     print(4)

#20-masala
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# if abs(a - b) > abs(a - c):
#     print(c, abs(a - c))
# else:
#     print(b, abs(a - b))

#21-masala
# x = float(input("x = "))
# y = float(input("y = "))
# if x == y == 0:
#     print(0)
# elif x == 0:
#     print(2)
# elif y == 0:
#     print(1)
# else: print(3)

#22-masala
# x = float(input("x = "))
# y = float(input("y = "))
# if x > 0:
#     if y > 0:
#       print(1)
#     else:
#         print(4)
# elif x < 0:
#     if y > 0:
#         print(2)
#     else:
#         print(3)

#23-masala
# x1 = int(input('x1 = '))
# y1 = int(input('y1 = '))
# x2 = int(input('x2 = '))
# y2 = int(input('y2 = '))
# x3 = int(input('x3 = '))
# y3 = int(input('y3 = '))
# x4, y4 = 0, 0
# if x1 == x2 and y1 == y3:
#     x4 = x3
#     y4 = y2
# elif x1 == x3 and y1 == y2:
#     x4 = x2
#     y4 = y3
# elif x2 == x3 and y2 == y1:
#     x4 = x1
#     y4 = y3
# else:
#     x4 = x3
#     y4 = y1
# print(x4, y4)

#24-masala
# x = float(input('x = '))
# y = 0
# if x > 0:
#     y = 2 * sin(x)
# else:
#     y = 6 – x
# print(y)

# 25-masala
# x = int(input('x = '))
# y = 0
# if x < -2 or x > 2:
#     y = 2 * x
# else:
#     y = -3 * x
# print(y)

# 26-masala
# x = float(input('x = '))
# y = 0
# if x <= 0:
#     y = -x
# elif x >= 2:
#     y = 4
# else:
#     y = x ** 2
# print(y)

# 27-masala
# x = float(input('x = '))
# y = 0
# if x < 0 or x >= 4:
#     y = 0
# elif 0 <= x < 1 or 2 <= x < 3:
#     y = 1
# else:
#     y = -1
# print(y)

# 28-masala
# x = int(input('x = '))
# if x % 4 == 0 and (x % 100 != 0 or x % 400 == 0):
#     print(366)
# else:
#     print(365)

# 29-masala
# a = int(input('a = '))
# if a > 0:
#     if a % 2 ==0:
#         print('musbat juft son')
#     else:
#         print('musbat toq son')
# elif(a < 0):
#     if a % 2 == 0:
#         print('manfiy juft son')
#     else:
#         print('manfiy toq son')
# else:
#     print('nol soni')


# 30-masala
a = int(input('a = '))
if a // 100 > 0:
    if a % 2 == 0:
        print('3 xonali juft son')
    else: print('3 xonali toq son')
elif a // 10 > 0:
    if a % 2 == 0:
        print('2 xonali juft son')
    else:
        print('2 xonali toq son')
else:
    if a % 2 == 0:
        print("1 xonali juft son")
    else: print("1 xonali toq son")
