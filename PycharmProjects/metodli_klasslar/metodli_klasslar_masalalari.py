#1-masala
# class Numbers:
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
#     def summ(self):
#         return self.num1 + self.num2
#     def sepa(self):
#         return self.num1 - self.num2
#     def kopy(self):
#         return self.num1 * self.num2
#     def boln(self):
#         return self.num1 / self.num2
#     def arif(self):
#         return (self.num1 + self.num2) / 2
#     def geom(self):
#         return (self.num1 * self.num2) ** 0.5
#     def __str__(self):
#         return f"{self.summ()}, {self.sepa()}, {self. kopy()},\
#     {self.boln()}, {self.arif()}, {self.geom()}"
# numbers = Numbers(123, 456)
# print(numbers)


#2-masala
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def perimeter(self):
#         return self.a + self.b + self.c
#     def face(self):
#         p = self.perimeter() / 2
#         return (p*(p-self.a)*(p-self.b)*(p-self.c)) ** 0.5
# tringle = Triangle(3, 4, 5)
# print(tringle.perimeter())
# print(tringle.face())


#3-masala
# class Numbers:
#     def __init__(self, a, b):
#         self.one = a
#         self.two = b
#     def max(self):
#         return self.one if self.one > self.two else self.two
#     def min(self):
#         return self.one if self.one != self.max() else self.two
# a, b, c = 12, 99, 50
# num1 = Numbers(a, b)
# if a == num1.max():
#     num2 = Numbers(b, c)
#     if c == num2.min():
#         print(f'minimum:{c}')
#     else:
#         num3 = Numbers(a, c)
#         print(f'minimum:{b}')
#         print(f'maxsimum:{num3.max()}')
# else:
#     num2 = Numbers(a, c)
#     if c == num2.min():
#         print(f'minimum:{c}')
#     else:
#         num3 = Numbers(b, c)
#         print(f'minimum:{a}')
#         print(f'maxsimum:{num3.max()}')


#4-masala
# 6.1 va 6.2- bo'limlarni qayerdan topaman


#5-masala
# class Rekursiya:
#     def __init__(self, n):
#         self.n = n
#     def collected(self):
#         a = self.n
#         s = 0
#         for i in range(a+1):
#             s += i
#         return s
#     def factorial(self):
#         a = self.n
#         p = 1
#         for i in range(1, a+1):
#             p *= i
#         return p
# number = Rekursiya(5)
# print(number.collected())
# print(number.factorial())


#6-masala
# class Collected:
#     def __init__(self, n):
#         self.n = n
#     def collec(self):
#         a = self.n
#         s = 0
#         for i in range(1, a+1):
#             s += i**2
#         return s
# num = Collected(5)
# print(num.collec())


#7-masala
# class Collected:
#     def __init__(self, n):
#         self.n = n
#     def collec(self):
#         a = self.n
#         s = 0
#         for i in range(1, a+1):
#             s += i*(a+1-i)
#         return s
# num = Collected(5)
# print(num.collec())


#8-masala
# class Fibon:
#     def __init__(self, n):
#         self.n = n
#     def fib_sum(self):
#         m = self.n
#         a = [1, 1]
#         for i in range(2, m):
#             a.append(a[i-1]+a[i-2])
#         return sum(a)
# num = Fibon(10)
# print(num.fib_sum())


#9-masala
# class Karra:
#     def __init__(self, k, n):
#         self.k = k
#         self.n = n
#     def top(self):
#         a = self.k
#         n = self.n
#         s = 0
#         b = []
#         for i in range(1, a+1):
#             if s < n:
#                 b.append(i*a)
#                 s += 1
#         return b
# k, n = 108, 6
# num = Karra(k, n)
# print(f'{k} soniga {n} ta karrali sonlar ro\'yxati:\n{num.top()}')


#10-masala
# class Qoldiqsiz:
#     def __init__(self, k, n):
#         self.k = k
#         self.n = n
#     def top(self):
#         a = self.k
#         n = self.n
#         s = 0
#         b = []
#         for i in range(1, a+1):
#             if a % i == 0 and s < n:
#                 b.append(i)
#                 s += 1
#         return b
# k, n = 108, 6
# num = Qoldiqsiz(k, n)
# print(f'{k} soniga {n} ta qoldiqsiz bo\'linadigan sonlar ro\'yxati:\n{num.top()}')


#11-masala
class Switch:
    def __init__(self, n, m, k):
        self.n = n
        self.m = m
        self.k = k
    def raqam(self):
        a = {0:'nol', 1:'bir', 2:'ikki', 3:'uch', 4:'to\'rt', 5:'besh', 6:'olti', 7:'yetti', 8:'sakkiz', 9:'to\'qqiz'}
        return a[self.n] if self.n in a.values() else 'siz raqam kiritmadingiz.'
    def hafta(self):
        a = {1:'dushanba', 2:'seshanba', 3:'chorshanba', 4:'payshanba', 5:'juma', 6:'shanba', 7:'yakshanba'}
        return a[self.m] if self.m in a.values() else 'chegara bo\'yicha kiriting.'
    def oy(self):
        a = {1:'yanvar', 2:'fevral', 3:'mart', 4:'aprel', 5:'may', 6:'iyun', 7:'iyul', 8:'avgust', 9:'sentabr', 10:'oktabr', 11:'noyabr', 12:'dekabr'}
        return a[self.k] if self.k in a.values() else 'chegara bo\'yicha kiriting.'
n = int(input('Raqamni kiriting: n(0<=n<=9) = '))
k = int(input('Haftani kiriting: kun(1<=k<=7) = '))
oy = int(input('Oyni kiriting: oy(1<=oy<=12) = '))
switch1 = Switch(n, k, oy)
print()
print(f'Raqamni so\'zdagi ifodasi: {switch1.raqam().title()}')
print(f'Hafta kuni: {switch1.hafta().title()}')
print(f'Oy: {switch1.oy().title()}')