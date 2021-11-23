#1-masala
# class Sanoq_sis:
#     def __init__(self, on):
#         self.on = on
#     def ikkilik(self):
#         return bin(self.on)
#     def sakkizlik(self):
#         return oct(self.on)
#     def on_olti(self):
#         return hex(self.on)
#     def __str__(self):
#         return str(self.on)
# a = Sanoq_sis(400)
# print(a.ikkilik())
# print(a.sakkizlik())
# print(a.on_olti())


#2-masala
# class Complex:
#     def __init__(self, a, b):
#         self.real = a
#         self.imag = b
#     def __add__(self, other):
#         if self.imag + other.imag > 0:
#             return f'{self.real + other.real}+{self.imag + other.imag}j'
#         else:
#             return f'{self.real + other.real}-{abs(self.imag + other.imag)}j'
#     def __sub__(self, other):
#         if self.imag > other.imag:
#             return f'{self.real - other.real}+{self.imag-other.imag}j'
#         else:
#             return f'{self.real - other.real}-{other.imag - self.imag}j'
#     def __mul__(self, other):
#         real = self.real * other.real - self.imag * other.imag
#         imag = self.real * other.imag + self.imag * other.real
#         if imag > 0:
#             return f'{real}+{imag}j'
#         else:
#             return f'{real}-{abs(imag)}j'
#     def __truediv__(self, other):
#         maxraj = other.real**2 + other.imag**2
#         real = self.real / maxraj
#         imag = self.imag / maxraj
#         if imag > 0:
#             return f'{real}+{imag}j'
#         else:
#             return f'{real}-{abs(imag)}j'
# comp = Complex(4, 2)
# comp2 = Complex(6, -8)
# print(comp + comp2)
# print(comp - comp2)
# print(comp * comp2)
# print(comp / comp2)


#3-masala
# class Matrix:
#     def __init__(self, a):
#         self.matrix = a
#     def cout(self):
#         for i in range(len(self.matrix)):
#             print(self.matrix[i])
#     def max(self):
#         a = []
#         for i in range(len(self.matrix)):
#             a.append(max(self.matrix[i]))
#         return max(a)
#     def min(self):
#         a = []
#         for i in range(len(self.matrix)):
#             a.append(min(self.matrix[i]))
#         return min(a)
#     def transponir(self):
#         for i in range(len(self.matrix[0])):
#             for j in range(len(self.matrix)-1, -1, -1):
#                 print(self.matrix[j][i], end=' ')
#             print()
#     def __str__(self):
#         return str(self.matrix)
# from random_matrix import matrix
# a = Matrix(matrix(3))
# a.cout()
# print(a.max())
# print(a.min())
# a.transponir()


#4-masala
# class Vector2_3D:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#     def __add__(self, other):
#         return f'x={self.x+other.x}, y={self.y+other.y}, z={self.z+other.z}.'
#     def __sub__(self, other):
#         return f'x={self.x-other.x}, y={self.y-other.y}, z={self.z-other.z}.'
#     def __mul__(self, other):
#         return self.x*other.x + self.y*other.y + self.z*other.z
#     def length(self):
#         return (self.x**2 + self.y**2 + self.z**2)**0.5
#     def cos_a(self, other):
#         return (self.__mul__(other)) / (self.length()*other.length())
#     def __str__(self):
#         return f'{(self.x)} {self.y} {self.z}'
#
# vec1 = Vector2_3D(3, 4, 0)
# vec2 = Vector2_3D(2, 8, 9)
# print(vec1+vec2)
# print(vec1-vec2)
# print(vec1*vec2)
# print(vec1.length())
# print(vec2.length())
# print(vec1.cos_a(vec2))


#5-masala
# class Ko_phad:
#     def __init__(self, d, k):
#         self.level = d
#         self.koef = k
#     def arg(self, x):
#         return x**(self.level) * self.koef
#     def hosila(self, a):
#         if self.level > 0:
#             d = self.level
#             p = 1
#             while a > 0:
#                 p *= d
#                 if d == 0:
#                     return 0
#                 d -= 1
#                 a -= 1
#             return f'{self.koef*p}x^{d}'
#         elif self.level == 0:
#             return 0
#         else:
#             d = self.level
#             p = 1
#             while a > 0:
#                 p *= d
#                 d -= 1
#                 a -= 1
#             return f'{self.koef * p}x^{d}'
#     def __str__(self):
#         return f'{self.koef}x^{self.level}'
# x = Ko_phad(-2, 5)
# print(x)
# print(x.arg(5))
# print(x.hosila(2))


#6-masala
# class Uy_kutubxona:
#     def __init__(self, d):
#         self.dict = d
#     def search(self, key):
#         if key in self.dict:
#             return self.dict[key]
#         else: return 'Bunday kitob yo\'q'
#     def qoshish(self, a, b):
#         self.dict[a] = b
#         return str(self.dict)
#     def deleted(self, a):
#         del self.dict[a]
#         return str(self.dict)
#     def __str__(self):
#         return str(self.dict)
# kitob = Uy_kutubxona({1991:'fizika', 2014:'informaika', 2012:'matematika', 2002:'c++'})
# print(kitob)
# print(kitob.search(2002))
# print(kitob.qoshish(2003, 'dasturlash'))
# print(kitob.deleted(2014))


#7-masala
# class Yon_daftar:
#     def __init__(self, a):
#         self.matrix = a
#     def search(self, soz):
#         k = 0
#         for i in range(len(self.matrix)):
#             if soz in self.matrix[i]:
#                 print(f'Siz qidirgan ma\'lumot topildi: {self.matrix[i]}')
#                 k += 1
#         if k ==0: print(f'Siz qidirgan ma\'mumot topilmadi.')
#     def insert(self, list):
#         self.matrix.append(list)
#         return self.matrix
#     def __str__(self):
#         return str(self.matrix)
# royxat = Yon_daftar([['Raximov', '2002', '916589340'], ['Iqboljon', '2003', '944450980'], ['Abbosbek', '2001', '900446979']])
# print(royxat)
# a = ['Dilshod', '2002', '914568932']
# print(royxat.insert(a))
# royxat.search('2002')
# royxat.search('Iqboljon')
# royxat.search('900446979')


#8-masala
# class Talaba_guruh:
#     def __init__(self, royxat):
#         self.royxat = royxat
#     def search(self, value):
#         if value in self.royxat.values():
#             print(self.royxat.items())
#         else:
#             print('Bunday talaba yo\'q')
#     def add(self, n, fam, tyil, tel):
#         self.royxat[n] = [fam, tyil, tel]
#     def delete_tartib(self, n):
#         del self.royxat[n]
#     def delete_malumot(self, value):
#         for i in self.royxat:
#             if value in self.royxat[i]:
#                 self.royxat[i].pop()
#     def sort(self):
#         for i in sorted(self.royxat):
#             print(i,':', self.royxat[i])
#     def __str__(self):
#         return str(self.royxat)
# talabalar = Talaba_guruh({3:['Abbosbek', '2001', '900446979'], 1:['Raximov', '2002', '916589340'], 2:['Iqboljon', '2003', '944450980']})
# talabalar.add(4, 'Dilshod', '2002', '985234565')
# talabalar.delete_malumot('2003')
# talabalar.sort()
# print(talabalar)


#9-masala
# class Populyatsiya:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def display(self):
#         x = self.x
#         y = self.y
#         while x > 0 and y > 0:
#             x, y = (2 * x - y), (-x + 2 * y)
#             if x <= 0:
#                 print(0, y)
#             elif y <= 0:
#                 print(x, 0)
#             else:
#                 print(x, y)
#     def __str__(self):
#         return f'{str(self.x)} {str(self.y)}'
# popul = Populyatsiya(499, 498)
# print(popul)
# popul.display()


#10-masala
# class Labr:
#     def __init__(self,m):
#         self.mass = m
#     def to_top(self,x,y):
#         if y <= 0:
#             return False
#         else:
#             return self.mass[y-1][x] == 0
#     def to_bottom(self,x,y):
#         if y >= len(self.mass)-1:
#             return False
#         else:
#             return self.mass[y + 1][x] == 0
#     def to_left(self,x,y):
#         if x<=0:
#             return False
#         else:
#             return self.mass[y][x-1] == 0
#     def to_right(self,x,y):
#         if x >= len(self.mass[0])-1:
#             return False
#         else:
#             return self.mass[y][x + 1] == 0
#     def find_path(self,x,y):
#         paths = []
#         if self.to_top(x,y):
#             paths.append((x,y-1))
#         if self.to_bottom(x,y):
#             paths.append((x,y+1))
#         if self.to_left(x,y):
#             paths.append((x-1,y))
#         if self.to_right(x,y):
#             paths.append((x+1,y))
#         return paths
#
#
#
# labirint = Labr([
#     [0,1,1,0,0,0],
#     [0,0,0,0,1,0],
#     [1,0,1,1,1,0],
#     [0,0,0,0,1,0]
# ])


#11-masala
# class Yuguruvchi:
#     def __init__(self, malum):
#         self.malumot = malum
#     def sort_time(self):
#         a = sorted([self.malumot[i][2] for i in range(len(self.malumot))], reverse=True)
#         for i in range(len(self.malumot)):
#             for j in range(len(self.malumot)):
#                 if a[i] in self.malumot[j]:
#                     print(self.malumot[j])
#     def jamoa_orta(self):
#         a = sum([self.malumot[i][2] for i in range(len(self.malumot))])
#         return a / len(self.malumot)
#     def orin(self, other, other1):
#         if self.jamoa_orta() < other.jamoa_orta() and self.jamoa_orta() < other1.jamoa_orta():
#             print(f'{self.malumot[0][1]} jamoa 1-o\'rin')
#             if other.jamoa_orta() < other1.jamoa_orta():
#                 print(f'{other.malumot[0][1]} jamoa 2-o\'rin')
#                 print(f'{other1.malumot[0][1]} jamoa 3-o\'rin')
#             else:
#                 print(f'{other1.malumot[0][1]} jamoa 2-o\'rin')
#                 print(f'{other.malumot[0][1]} jamoa 3-o\'rin')
#         elif self.jamoa_orta() > other.jamoa_orta() and other.jamoa_orta() < other1.jamoa_orta():
#             print(f'{other.malumot[0][1]} jamoa 1-o\'rin')
#             if self.jamoa_orta() < other1.jamoa_orta():
#                 print(f'{self.malumot[0][1]} jamoa 2-o\'rin')
#                 print(f'{other1.malumot[0][1]} jamoa 3-o\'rin')
#             else:
#                 print(f'{other1.malumot[0][1]} jamoa 2-o\'rin')
#                 print(f'{self.malumot[0][1]} jamoa 3-o\'rin')
#         else:
#             print(f'{other1.malumot[0][1]} jamoa 1-o\'rin')
#             if other.jamoa_orta() < self.jamoa_orta():
#                 print(f'{other.malumot[0][1]} jamoa 2-o\'rin')
#                 print(f'{self.malumot[0][1]} jamoa 3-o\'rin')
#             else:
#                 print(f'{self.malumot[0][1]} jamoa 2-o\'rin')
#                 print(f'{other.malumot[0][1]} jamoa 3-o\'rin')
#     def __str__(self):
#         return str(self.malumot)
# a_jamoa = Yuguruvchi([['a', 'a', 11.2], ['b', 'a', 10.9], ['c', 'a', 10.8]])
# b_jamoa = Yuguruvchi([['d', 'b', 10.2], ['e', 'b', 11.9], ['f', 'b', 10.5]])
# c_jamoa = Yuguruvchi([['g', 'c', 9.9], ['h', 'c', 12.7], ['i', 'c', 10.7]])
# a_jamoa.sort_time()
# print(f'A jamoaning o\'rtacha yugurush vaqti:{a_jamoa.jamoa_orta()}')
# print(f'A jamoaning o\'rtacha yugurush vaqti:{b_jamoa.jamoa_orta()}')
# print(f'A jamoaning o\'rtacha yugurush vaqti:{c_jamoa.jamoa_orta()}')
# a_jamoa.orin(b_jamoa, c_jamoa)


#12-masala
# class Futbol:
#     def __init__(self, jamoa):
#         self.jamoa = jamoa
#     def __add__(self, other):
#         if type(self.jamoa[0]) == list:
#             a = self.jamoa
#             a.append(other.jamoa)
#             return Futbol(a)
#         else:
#             a = [self.jamoa]
#             a.append(other.jamoa)
#             return Futbol(a)
#     def reyting(self):
#         print('Reyting jadvali bilan tanishing:')
#         a = []
#         for i in self.jamoa:
#             a.append([i[1]*3+i[2]*1, i[4]-i[5], i[0]])
#         a = sorted(a[i] for i in range(len(a)))
#         a = reversed(a)
#         k = 1
#         for i in a:
#             print(f'{k}\t{i[2]}\t{i[1]}\t{i[0]}')
#             k += 1
#     def __str__(self):
#         return str(self.jamoa)
# a = Futbol(['MYu', 10, 1, 0, 35, 2])
# b = Futbol(['Tot', 7, 2, 2, 24, 15])
# c = Futbol(['MCi', 9, 0, 2, 29, 6])
# d = Futbol(['Che', 8, 2, 1, 26, 8])
# e = Futbol(['liv', 9, 1, 1, 30, 6])
# f = Futbol(['Ars', 8, 1, 2, 22, 13])
# g = Futbol(['Lei', 7, 2, 2, 21, 12])
# massiv = [a, b, c, d, e, f, g]
# for i in range(len(massiv)-1):
#     a += massiv[i+1]
# a.reyting()


#13-masala
# class Avtomobilchi:
#     def __init__(self, f, r, n):
#         self.familiya = f
#         self.rusum = r
#         self.nomer = n
#     def __lt__(self, other):
#         return self.familiya[0] < other.familiya[0]
#     def avtorusum(self, element):
#         if element == self.rusum:
#             print(f'Avtomobilchi familiyasi: {self.familiya};\n\
# Avtomobil rusumi: {self.rusum};\nAvtomobil nomeri: {self.nomer}.')
#     def search(self, avtorusum, avtonomer):
#         if avtorusum == self.rusum and avtonomer == self.nomer:
#             print(self.familiya)
#     def __str__(self):
#         return f'Avtomobilchi familiyasi: {self.familiya};\n\
# Avtomobil rusumi: {self.rusum};\nAvtomobil nomeri: {self.nomer}.'
#
# avto1 = Avtomobilchi('Yo\'ldashev', 'Malibu', '60 Z 777 ZZ')
# avto2 = Avtomobilchi('Ustaboyev', 'Tracker', '01 Z 777 ZZ')
# avto3 = Avtomobilchi('Rahimov', 'Tahoe', '40 A 777 AA')
# avto4 = Avtomobilchi('Miraxmedov', 'Jentira', '50 A 111 AA')
# massiv = [avto1, avto2, avto3, avto4]
# for i in massiv:
#     i.avtorusum('Tahoe')
# print()
# for i in massiv:
#     i.search('Malibu', '60 Z 777 ZZ')
# print('\nAvtomobil egalari saralandi:\n')
# massiv = sorted(massiv)
# for avto in massiv:
#     print(avto, end='\n\n')


#14-masala
# class Formula:
#     def __init__(self, raqam, form1, belgi, form2):
#         self.raqam = raqam
#         self.form1 = form1
#         self.form2 = form2
#         self.belgi = belgi
#     @property
#     def hisoblash(self):
#         a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#         b = ['+', '-', '*']
#         if self.raqam in a and self.belgi in b:
#             if type(self.form1) == int and type(self.form2) == int:
#                 if self.belgi == b[0]:
#                     return self.raqam*(self.form1+self.form2)
#                 elif self.belgi == b[1]:
#                     return self.raqam * (self.form1 - self.form2)
#                 else:
#                     return self.raqam * (self.form1 * self.form2)
#             else:
#                 return False
#         else:
#             return False
# form = Formula(3, 78, '-', 75)
# print(form.hisoblash)


#16-masala
# class Tortburchak:
#     def __init__(self, a, b, c, d):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d
#     @property
#     def mavjudligi(self):
#         if self.a > 0 and self.b > 0 and self.c > 0 and self.d > 0:
#             return True
#         else:
#             return False
#     def turi(self):
#         if self.mavjudligi == True:
#             if self.a == self.c and self.b == self.d:
#                 return f'To\'g\'ri burchakli to\'rtburchak yoki paralelogram'
#             elif self.a == self.c == self.b == self.d:
#                 return f'Kvadrat'
#             else:
#                 return f'To\'rtburchak'
#         else:
#             return 'To\'rtburchak mavjud emas!'
#     def perimetri(self):
#         if self.mavjudligi == True:
#             return f'Perimetri:{self.a+self.b+self.c+self.d}'
#         else:
#             return 'To\'rtburchak mavjud emas!'
#     def yuzasi(self):
#         if self.mavjudligi == True:
#             if self.turi() == 'To\'g\'ri burchakli to\'rtburchak yoki paralelogram':
#                 return f'Yuzasi:{self.a*self.b}'
#             elif self.turi() == 'Kvadrat':
#                 return f'Yuzasi:{self.a**2}'
#             else:
#                 return f'To\'rtburchak yuzasini hisoblash uchun yetarli ma\'lumotlar yo\'q!'
#         else:
#             return 'To\'rtburchak mavjud emas!'
#     def __str__(self):
#         return f'a={self.a}, b={self.b}, c={self.c}, d={self.d}'
# tort = Tortburchak(4, 5, 2, 9)
# tort1 = Tortburchak(2, 4, 2, 4)
# print(tort.turi())
# print(tort.yuzasi())
# print(tort1.perimetri())
# print(tort1.yuzasi())


#17-masala
class Rational:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    @property
    def tekshirish(self):
        return self.a == self.b
    @property
    def summ(self):
        return self.a + self.b
    def __lt__(self, other):
        return self.summ < other.summ
    def __str__(self):
        return f'a={self.a}, b={self.b}'
rat = Rational(12.3, 56.51)
rat1 = Rational(19.12, 98.03)
rat2 = Rational(54, 23.4)
rat3 = Rational(7.77, 7.77)
rat4 = Rational(89.5, 10.5)
massiv = [rat.summ, rat1.summ, rat2.summ, rat3.summ, rat4.summ]
print(max(massiv))