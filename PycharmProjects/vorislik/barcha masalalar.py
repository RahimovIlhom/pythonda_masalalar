#1-masala
# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __str__(self):
#         return f'x = {self.x}, y = {self.y}'
# class Vector_amal(Vector):
#     def __add__(self, other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Vector(x, y)
#     def __sub__(self, other):
#         x = self.x - other.x
#         y = self.y - other.y
#         return Vector(x, y)
#     def __mul__(self, other):
#         x = self.x * other.x
#         y = self.y * other.y
#         return x + y
#     @property
#     def length(self):
#         length = (self.x ** 2 + self.y ** 2) ** 0.5
#         return length
#     def burchar_cos(self, other):
#         cos = (self*other) / (self.length*other.length)
#         return cos
# vec = Vector_amal(2, 3)
# vec1 = Vector_amal(9, 10)
# # print(vec * vec1)
# # print(vec.length)
# print(vec.burchar_cos(vec1))


#2-masala
# class Kop_had:
#     def __init__(self, daraja, koef):
#         self.daraja = daraja
#         self.koef = koef
#     def __str__(self):
#         return f'{self.koef}*x^{self.daraja}'
# class Kop_had_amal(Kop_had):
#     def __init__(self, daraja, koef, x):
#         super(Kop_had_amal, self).__init__(daraja, koef)
#         self.x = x
#     @property
#     def hisob(self):
#         javob = self.koef * self.x ** self.daraja
#         return javob
# kophad1 = Kop_had_amal(3, 5, 2)
# print(kophad1)
# print(kophad1.hisob)


#3-masala
# class Kitob:
#     def __init__(self, nom, mual, nash, chop):
#         self.nomi = nom
#         self.muallifi = mual
#         self.nashrioti = nash
#         self.chop_yil = chop
#     def __str__(self):
#         return f'Nomi: {self.nomi}\n' \
#                f'Muallifi: {self.muallifi}\n' \
#                f'Nashrioti: {self.nashrioti}\n' \
#                f'Chop qilingan yili: {self.chop_yil}'
# class Uy_kutubxona(Kitob):
#     def __init__(self, nom, mual, nash, chop, man, ega):
#         super(Uy_kutubxona, self).__init__(nom, mual, nash, chop)
#         self.mazili = man
#         self.egasi = ega
#     def __str__(self):
#         return f'{super().__str__()}\n' \
#                f'Manzili: {self.mazili}\n' \
#                f'Egasi: {self.egasi}'
# kitob = Uy_kutubxona('Dasturlash', 'Ilhomjon', 'Toshkent', 2021, 'Farg\'ona', 'Rahimov')
# print(kitob)


# 4-masala
# class Satr:
#     def __init__(self, satr):
#         self.satr = satr
#     def __str__(self):
#         return self.satr
# class Arif_amal(Satr):
#     def __add__(self, other):
#         a = int(self.satr)
#         b = int(other.satr)
#         return a + b
#     def __sub__(self, other):
#         a = int(self.satr)
#         b = int(other.satr)
#         return a - b
#     def __mul__(self, other):
#         a = int(self.satr)
#         b = int(other.satr)
#         return a * b
#     def __truediv__(self, other):
#         a = int(self.satr)
#         b = int(other.satr)
#         return a / b
# amal = Arif_amal('10')
# amal1 = Arif_amal('12')
# print(amal + amal1)
# print(amal / amal1)


#5-masala
# class Shaxs:
#     def __init__(self, fi, ty, jins, man, tel):
#         self.fi = fi
#         self.t_yil = ty
#         self.jins = jins
#         self.manzil = man
#         self.tel = tel
#     def __str__(self):
#         return f'familiyasi va ismi: {self.fi}\n' \
#                f'tug\'ilgan yili: {self.t_yil}\n' \
#                f'jinsi: {self.jins}\n' \
#                f'manzili: {self.manzil}\n' \
#                f'telefon raqami: {self.tel}'
# class Talaba(Shaxs):
#     def __init__(self, fi, ty, jins, man, tel, gur, kurs):
#         super().__init__(fi, ty, jins, man, tel)
#         self.guruh = gur
#         self.kurs = kurs
#     def search(self, value_ty):
#         return value_ty == self.t_yil
#     def __lt__(self, other):
#         return self.fi < other.fi
#     def __str__(self):
#         return f'{super().__str__()}\n' \
#                f'guruhi: {self.guruh}\n' \
#                f'kursi: {self.kurs}'
# talaba1 = Talaba('Rahimov Ilhomjon', 2002, 'erkak', 'Farg\'ona', 6589340, '315-20', 2)
# talaba2 = Talaba('Miraxmedov Xusanboy', 1997, 'erkak', 'Namangan', 5146663, '315-20', 2)
# talaba3 = Talaba('Yo\'ldashev Iqboljon', 2003, 'erkak', 'Andijon', 6492631, '317-20', 2)
# a = [talaba1, talaba2, talaba3]
# a.sort()
# for i in a:
#     print(i)
#     if i.search(2002) == True:
#         print(i.fi, 'qidirayotgan yilda tug\'ilgan')


#6-masala
# class Tuplam:
#     def __init__(self, a):
#         self.a = a
#     def __str__(self):
#         return f'{self.a}'
# class Tuplam_amal(Tuplam):
#     def __add__(self, other):
#         b = list(self.a) + list(other.a)
#         return set(b)
#     def push(self, value):
#         b = list(self.a)
#         b = b + [value]
#         return set(b)
#     def pop(self, value):
#         h = []
#         for i in self.a:
#             if i != value:
#                 h.append(i)
#         return set(h)
#     def __and__(self, other):
#         return self.a & other.a
#     def __sub__(self, other):
#         return set(self.a - other.a)
# tup = Tuplam_amal({22,4,3,5,546,23,4,3,24,2,23,43,2,65,4,56,34,3})
# top = Tuplam_amal({3,4,45,7,5,67,8,6,5,5,33,3,1,2,3,45,5,7,9})
# print(tup)
# # print(top)
# print(tup.push(1))
# # print(tup.pop(24))
# # print(tup + top)
# # print(tup & top)
# # print(tup - top)


#8-masala
# from def_matrix import Print
# class Taxta:
#     def __init__(self, son, harf):
#         self.sonlar = son
#         self.harflar = harf
#     @property
#     def matrix(self):
#         a = []
#         b = self.harflar
#         c = self.sonlar
#         for i in b:
#             b = []
#             for j in c:
#                 b.append(i+f'{j}')
#             a.append(b)
#         return a
#     def print(self):
#         Print(self.matrix)
#     def __str__(self):
#         return f'{self.matrix}'
# class Farzin(Taxta):
#     def yonalish_top(self, i, j):
#         a = self.harflar
#         b = self.sonlar
#         c, e = [], []
#         e.append(" ")
#         e.extend(b)
#         c.append(e)
#         for k in range(len(a)):
#             d = [a[k]]
#             for p in range(len(b)):
#                 if abs(i - k) == abs(j - p) or k == i or p == j:
#                     d.append('X')
#                 else:
#                     d.append('0')
#             c.append(d)
#         Print(c)
# taxta = Farzin([1, 2, 3, 4, 5, 6, 7, 8], ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
# taxta.print()
# taxta.yonalish_top(1, 4)


#10-masala
# class Uchburchak:
#     def __init__(self, x1, y1, x2, y2, x3, y3):
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2
#         self.x3 = x3
#         self.y3 = y3
#         self.a = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
#         self.b = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
#         self.c = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
#     def turi(self):
#         if self.a == self.b == self.c:
#             return f'Teng tomonli uchburchak'
#         elif self.a == self.b or self.a == self.c or self.b == self.c:
#             return f'Teng yonli uchburchak'
#         else:
#             if self.a ** 2 + self.b ** 2 == self.c ** 2:
#                 return f'To\'g\'ri burchakli uchburchak'
#             elif self.a ** 2 + self.c ** 2 == self.b ** 2:
#                 return f'To\'g\'ri burchakli uchburchak'
#             elif self.b ** 2 + self.c ** 2 == self.a ** 2:
#                 return f'To\'g\'ri burchakli uchburchak'
#             else:
#                 return f'Shunchaki uchburchak'
#     def perimetr(self):
#         if self.turi() == f'Teng tomonli uchburchak':
#             return self.a * 3
#         else:
#             return self.a + self.b + self.c
#     def yuzasi(self):
#         if self.turi() == f'Teng tomonli uchburchak':
#             return self.a ** 2 * 3 ** 0.5 / 4
#         else:
#             p = self.perimetr() / 2
#             s = (p * (p-self.a) * (p-self.b) * (p-self.c)) ** 0.5
#             return s
#     def __str__(self):
#         return f'a = {self.a}, b = {self.b}, c = {self.c}'
# uch = Uchburchak(5,6,9,8,2,3)
# print(uch.yuzasi())


#11-masala
class To_rtbuchak:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.a = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        self.b = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
        self.c = ((x3 - x4) ** 2 + (y3 - y4) ** 2) ** 0.5
        self.d = ((x1 - x4) ** 2 + (y1 - y4) ** 2) ** 0.5
        self.diog = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
    def mavjud(self):
        if self.a == 0 or self.b == 0 or self.c == 0 or self.d == 0:
            return False
        else: return True
    def yuzasi(self):
        p1 = (self.a + self.b + self.diog) / 2
        p2 = (self.c + self.d + self.diog) / 2
        s1 = (p1 * (p1 - self.a) * (p1 - self.b) * (p1 - self.diog)) ** 0.5
        s2 = (p2 * (p2 - self.c) * (p2 - self.d) * (p2 - self.diog)) ** 0.5
        return s1 + s2
    def perimetr(self):
        p = self.a + self.b + self.c + self.d
        return p
    def __str__(self):
        return f'a = {self.a}, b = {self.b}, c = {self.c}, d = {self.d}'
tort = To_rtbuchak(5, 2, 3, 6, 4, 8, 9, 6)
print(tort.yuzasi())