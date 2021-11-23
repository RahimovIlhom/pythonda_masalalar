#1-masala
# class Progress:
#     def __init__(self):
#         pass
#     def n_hadi(self, n):
#         '''
#         Progressiyaning n-hadini topish funksiyasi
#
#         :param n:
#         :return:
#         '''
#         pass
#     def n_summ(self, n):
#         '''
#         Progressiyaning n ta hadi yig'indisi funksiyasi
#
#         :param n:
#         :return:
#         '''
#         pass
# class Arif_prog(Progress):
#     def __init__(self, a, d):
#         super().__init__()
#         self.a = a
#         self.d = d
#     def n_hadi(self, n):
#         an = self.a + (n - 1) * self.d
#         return an
#     def n_summ(self, n):
#         s = (self.a + (n - 1) * self.d / 2) * n
#         return s
#     def __str__(self):
#         return f'a0 = {self.a}\n' \
#                f'd = {self.d}\n'
# class Geom_prog(Progress):
#     def __init__(self, b, q):
#         super().__init__()
#         self.b = b
#         self.q = q
#     def n_hadi(self, n):
#         bn = self.b * (self.q) ** (n - 1)
#         return bn
#     def n_summ(self, n):
#         s = self.b * (1 - self.q ** n) / (1 - self.q)
#         return s
#     def __str__(self):
#         return f'b0 = {self.b}\n' \
#                f'q = {self.q}\n'
# arif = Arif_prog(5, 3)
# print(arif.n_hadi(10))


#2-masala
class Sanoq_sistema:
    def __init__(self, son):
        self.son = son
    def __str__(self):
        return self.son
class Sanoq_2(Sanoq_sistema):
    def ikkilik(self):
        ikki = self.son
        a = ''
        while ikki > 0:
            a += f'{ikki % 2}'
            ikki //= 2
        return (f'{reversed(a)}')
    def __str__(self):
        return f'ikkilik = {self.ikkilik()}'
sanoq2 = Sanoq_2(4)
print(sanoq2)