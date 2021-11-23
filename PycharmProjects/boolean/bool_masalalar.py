#1-masala
#a = int(input("a = "))
#print(a > 0)

#8-masala
#a = int(input("a = "))
#b = int(input("b = "))
#r = a % 2 == 0 and b % 2 == 0
#print(r)

#12-masala
#a = int(input("a = "))
#b = int(input("b = "))
#c = int(input("c = "))
#r = a > 0 and b > 0 and c > 0
#print(r)

#13-masala
#a = int(input("a = "))
#b = int(input("b = "))
#c = int(input("c = "))
#r = a > 0 or b > 0 or c > 0
#print(r)

#17-masala
#a = int(input("a = "))
#r = a % 2 == 1 and a // 100 > 0 and a // 1000 == 0
#print(r)

#19-masala
#a = int(input("a = "))
#b = int(input("b = "))
#c = int(input("c = "))
#r = a == -b or b == -c or a == -c
#print(r)

#23-masala
#a = int(input("a = "))
#b = a % 10
#c = a // 10 % 10
#d = a // 100 % 10
#e = a // 1000
#r = b == e and c == d
#print(r)

#24-masala
#a = int(input("a = "))
#b = int(input("b = "))
#c = int(input("c = "))
#r = b * b - 4 * a * c >= 0
#print(r)

#27-masala
#x = int(input("x = "))
#y = int(input("y = "))
#r = x < 0 < y or x < 0 > y
#print(r)

#29-masala
#x1 = int(input("x1 = "))
#y1 = int(input("y1 = "))
#x2 = int(input("x2 = "))
#y2 = int(input("y2 = "))
#x = int(input("x = "))
#y = int(input("y = "))
#r = x1 < x < x2 and y1 > y > y2
#print(r)

#30-masala
#a = int(input("a = "))
#b = int(input("b = "))
#c = int(input("c = "))
#r = a == b == c
#print(r)

#32-masala
#a = int(input("a = "))
#b = int(input("b = "))
#c = int(input("c = "))
#r = a*a == b*b + c*c or a*a + b*b == c*c or b*b == c*c ++ a*a
#print(r)

#34-masala
#a = int(input("a = "))
#b = int(input("b = "))
#r = (a % 2 == 1 and b % 2 == 1) or (a % 2 == 0 and b % 2 == 0)
#print(r)

#35-masala
#x1 = int(input("x1 = "))
#y1 = int(input("y1 = "))
#x2 = int(input("x2 = "))
#y2 = int(input("y2 = "))
#r1 = x1 % 2 == y1 % 2 and x2 % 2 == y2 % 2
#r2 = x1 % 2 != y1 % 2 and x2 % 2 != y2 % 2
#r = r1 or r2
#print(r)

#36-masala
#x1 = int(input("x1 = "))
#y1 = int(input("y1 = "))
#x2 = int(input("x2 = "))
#y2 = int(input("y2 = "))
#r = (x1 != x2) and (y1 == 4 and y2 == 5) or (y1 ==5 and y2 ==4)
#print(r)

#37-masala
#x1 = int(input("x1 = "))
#y1 = int(input("y1 = "))
#x2 = int(input("x2 = "))
#y2 = int(input("y2 = "))
#r = (abs(x1 - x2) == 1 or abs(x1 - x2) == 0) and (abs(y1 - y2) == 1 or abs(y1 - y2) == 0)
#print(r)

#38-masala
#x1 = int(input("x1 = "))
#y1 = int(input("y1 = "))
#x2 = int(input("x2 = "))
#y2 = int(input("y2 = "))
#r = (x1 + abs(4 - y1)) > 0 and (x2 - abs(4 - y2)) > 0
#print(r)

#40-masala
x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))
r = abs(y1 - 4) <= 2 and abs(y2 - 4) <= 2
print(r)