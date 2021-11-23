#1-masala
# exept = "\/:*?<>|"
# fayl = "new_file.txt"
# a = bool
# for i in exept:
#     if i in fayl:
#         a = 0
#     else:
#         a = 1
# if a == 1:
#     file = open(fayl, 'w')
#     file.close()

#2-masala
# n = int(input())
# s = 'new_file1.txt'
# file = open(s, 'w')
# for i in range(2, n+1, 2):
#     file.write(str(i)+' ')
# file.close()
# file = open(s)
# for fi in file:
#     print(fi, end=' ')

#3-masala
# a = 2
# d = 4
# s = 'file.txt'
# with open(s, 'w') as file:
#     for i in range(10):
#         file.write(str(a)+' ')
#         a += d
# with open(s) as fil:
#     print(fil.read())

#4-masala
# s = 'new_file2.txt'
# with open(s, 'r') as fayl:
#     if fayl.read() == FileNotFoundError:
#         print(0)
#     else:
#         print(1) ????

#5-masala
# s = 'new_file.txt'
# with open(s, 'r') as file:
#     a = file.read().split()
#     print(len(a))

#6-masala
# k = 7
# s = 'new_file.txt'
# b = []
# with open(s, 'r') as file:
#     a = file.read().split()
#     for i in range(len(a)):
#         b.append(int(a[i]))
# print(b[k] if k < len(b) else -1)

#9-masala
# s, s1 = 'new_file.txt', 'new_file2.txt'
# a = ''
# with open(s, 'r') as file:
#     b = file.read().split()
#     a += (b[-1])+' '+(b[0])
# with open(s1, 'w') as file:
#     file.write(a)

#10-masala
# s, s1 = 'new_file.txt', 'new_file2.txt'
# a = ''
# with open(s, 'r') as file:
#     b = file.read().split()
#     for i in range(len(b)-1,-1,-1):
#         a += b[i]+' '
#     print(a)
# with open(s1, 'w') as file:
#     file.write(a)

#13-masala
# s, s1, s2 = 'new_file.txt', 'new_file3.txt', 'new_file4.txt'
# a = []
# with open(s,'r') as file:
#     b = file.read().strip()
#     for i in range(len(b)):
#         a.append(int(b[i]))
# f = open(s1, 'w')
# g = open(s2, 'w')
# for i in a:
#     if i > 0:
#         f.write(str(i)+" ")
#     else:
#         g.write(str(i)+' ')
# f.close()
# g.close()

#16-masala
# s = 'new_file.txt'
# with open(s, 'r') as file:
#     b = file.read()
#     b = b.rstrip()
#     b = b.replace(' ', '')
#     print(len(b))

#23-masala
# s = 'new_file.txt'
# a = []
# with open(s) as file:
#     b = file.read().split()
#     for i in b:
#         a.append(int(i))
# c = []
# k = 0
# for i in range(len(a)-1):
#     if a[i]>a[i+1]:
#         k += 1
#     else:
#         if k > 0:
#             c.append(k)
#         k = 0
# print(c)

#24-masala
# s = 'new_file.txt'
# a = []
# with open(s) as file:
#     b = file.read().split()
#     for i in b:
#         a.append(int(i))
# c = []
# k, p = 0, 0
# for i in range(len(a)-1):
#     if a[i]>a[i+1] and p == 0:
#         k += 1
#     elif a[i]<a[i+1]:
#         p += 1
#         if k > 0:
#             c.append(k)
#         k = 0
#     else:
#         if p > 0:
#             c.append(p)
#         p = 0
# print(c)

#27-masala 1-qism
# a = [2, 4, -6, 8, -10, -12, -14, 16, 18, 20]
# import pickle
# with open('file', 'wb') as file:
#     pickle.dump(a, file)
# with open('file', 'rb') as file:
#     b = pickle.load(file)
#     print(b)
#2-qism
# import pickle
# a = []
# with open('file', 'rb') as file:
#     b = pickle.load(file)
#     print(b)
#     for i in range(len(b)-1, -1, -1):
#         a.append(b[i])
# print(a)
# with open('file1', 'wb') as file1:
#     pickle.dump(a, file1)

#36-masala
# s = 'new_file1.txt'
# a = []
# with open(s, 'r+') as file:
#     b = file.read().split()
#     for i in range(len(b)):
#         file.write(' ' + str(b[i]))
# with open(s, 'r') as file2:
#     print(file2.read())

#37-masala
# s = 'new_file1.txt'
# a = []
# with open(s, 'r+') as file:
#     b = file.read().split()
#     for i in range(len(b)-1, -1, -1):
#         file.write(' ' + str(b[i]))
# with open(s, 'r') as file2:
#     print(file2.read())

#39-masala
# s = 'new_file2.txt'
# a = []
# with open(s, 'r') as file:
#     b = file.read().split()
#     a = b
#
# with open(s, 'w') as file2:
#     for i in range(len(a)):
#         if 3 <= i <= 5:
#             file2.write(str(a[i]+' '+a[i]+' '))
#         else:
#             file2.write(str(a[i])+' ')

#40-masala
# s = 'new_file3.txt'
# a = []
# with open(s, 'r') as file:
#     b = file.read().split()
#     a = b
#     print(a)
# with open(s, 'w+') as file2:
#     for i in range(len(a)):
#         if i % 2== 0:
#             file2.write('00 ')
#         else:
#             file2.write(str(a[i])+' ')

#41-masala
a = []
with open('new_file.txt', 'r') as file:
    b = file.read().split()
    a = b
with open('new_file.txt', 'w') as file2:
    for i in range(len(a)):
        if int(a[i]) > 0:
            file2.write('000 ')
        else:
            file2.write(str(a[i])+' ')