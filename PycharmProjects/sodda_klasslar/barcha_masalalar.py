#1-masala
# class Numbers:
# 	def __init__(self, a, b):
# 		self.a = a
# 		self.b = b
# 	def qosh(self):
# 		return self.a+self.b
# 	def ayir(self):
# 		return self.a-self.b
# 	def kop(self):
# 		return self.a*self.b
# 	def nis(self):
# 		return self.a/self.b
# num = Numbers(10, 26)
# print(num.qosh())
# print(num.ayir())
# print(num.kop())
# print(num.nis())

#2-masala
# class Uchbur:
# 	def __init__(self, a, b):
# 		self.a = a
# 		self.b = b
# 	def yuza(self):
# 		return self.a * self.b / 2
# 	def peri(self):
# 		c = (self.a**2 + self.b**2)**0.5
# 		return self.a + self.b + c
# uchburchak = Uchbur(4, 3)
# print(uchburchak.yuza())
# print(uchburchak.peri())

#3-masala
# from math import  pi
# class Circle:
# 	def __init__(self, r):
# 		self.r = r
# 	def length(self):
# 		return 2 * pi * self.r
# 	def face(self):
# 		return pi * self.r**2
# 	def __str__(self):
# 		return f'{self.length()} {self.face()}'
# circle1 = Circle(5)
# print(circle1)

#4-masala
# from math import pi
# class Circle:
# 	def __init__(self, face):
# 		self.face = face
# 	def radius(self):
# 		return (self.face / pi) ** 0.5
# circle1 = Circle(100)
# print(circle1.radius())

#5-masala
# class Distance:
# 	def __init__(self, x1, y1, x2, y2):
# 		self.x1 = x1
# 		self.y1 = y1
# 		self.x2 = x2
# 		self.y2 = y2
# 	def dis(self):
# 		return ((self.x1-self.x2)**2 + (self.y1-self.y2)**2)**0.5
# points1 = Distance(5, 6, 2, 10)
# print(points1.dis())

#6-masala
# class Circle:
#     def __init__(self,x1,y1,x2,y2,x3,y3):
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2
#         self.x3 = x3
#         self.y3 = y3
#     def a_side(self):
#         return ((self.x1-self.x2)**2+(self.y1-self.y2)**2)**0.5
#     def b_side(self):
#         return ((self.x1-self.x3)**2+(self.y1-self.y3)**2)**0.5
#     def c_side(self):
#         return ((self.x3-self.x2)**2+(self.y3-self.y2)**2)**0.5
#     def face(self):
#         p = (self.a_side() + self.b_side() + self.c_side()) / 2
#         return (p * (p-self.a_side()) * (p-self.b_side()) * (p-self.c_side()))**0.5
# points1 = Circle(0, 0, 0, 4, 3, 0)
# print(points1.a_side())
# print(points1.b_side())
# print(points1.c_side())
# print(points1.face())

#7-masala
# class Numbers:
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
#     def arifmetic(self):
#         return (self.num1 + self.num2) / 2
#     def geometric(self):
#         return (self.num1 * self.num2) ** 0.5
# numbers = Numbers(10, 40)
# print(numbers.arifmetic())
# print(numbers.geometric())

#8-masala
# class Rectangle:
#     def __init__(self, x1, y1, x2, y2):
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2
#     def face(self):
#         a = self.x1 - self.x2
#         b = self.y1 - self.y2
#         return abs(a * b)
# rectangle = Rectangle(45, 65, 10, 99)
# print(rectangle.face())

#9-masala
class Number:
    def __init__(self, num):
        self.number = num
    def collec(self):
        s = 0
        a = self.number
        while a > 0:
            s += a % 10
            a //= 10
        return s
    def multic(self):
        p = 1
        b = self.number
        while b > 0:
            p *= (b % 10)
            b //= 10
        return p
number1 = Number(1236)
print(number1.collec())
print(number1.multic())