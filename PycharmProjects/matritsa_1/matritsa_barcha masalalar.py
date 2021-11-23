#1-masala
# m = int(input("m = "))
# n = int(input("n = "))
# a = []
# for i in range(m):
#     b = []
#     for j in range(n):
#         if i == 1:
#             b.append(j * 10)
#         else:
#             b.append(0)
#     a.append(b)
# print(a)

#2-masala
# m = int(input("m = "))
# n = int(input("n = "))
# a = []
# for i in range(m):
#     b = []
#     for j in range(n):
#         if j == 1:
#             b.append(5 * i)
#         else:
#             b.append(0)
#     a.append(b)
# print(a)

#3-masala
# m = int(input("m = "))
# n = int(input("n = "))
# a = []
# for i in range(m):
#     b = []
#     for j in range(n):
#         b.append(i)
#     a.append(b)
# from def_matrix import Print
# Print(a)

#4-masala
# m = int(input("m = "))
# n = int(input("n = "))
# a = []
# for i in range(m):
#     b = []
#     for j in range(n):
#         b.append(j)
#     a.append(b)
# from def_matrix import Print
# Print(a)

#5-masala
# m = int(input("m = "))
# n = int(input("n = "))
# d = int(input("d = "))
# a = []
# for i in range(m):
#     b = []
#     for j in range(n):
#         if j == 1:
#             b.append(i)
#         else:
#             b.append(j+d)
#     a.append(b)
# from def_matrix import Print
# Print(a)

#6-masala
# m = int(input("m = "))
# n = int(input("n = "))
# q = int(input("q = "))
# a = []
# for i in range(m):
#     b = []
#     for j in range(n):
#         if i == 1:
#             b.append(i)
#         else:
#             b.append((10*i+j)*q)
#     a.append(b)
# from def_matrix import Print
# Print(a)

#7-misol
# m = int(input("m = "))
# n = int(input("n = "))
# k = int(input("k = "))
# a = []
# for i in range(m):
#     b = []
#     for j in range(n):
#         b.append(10*i+j)
#     a.append(b)
# from def_matrix import Print
# Print(a)
# if 1 <= k <= m:
#     print(a[k])

#8-masala
# m = int(input("m = "))
# n = int(input("n = "))
# k = int(input("k = "))
# a = []
# for i in range(m):
#     b = []
#     for j in range(n):
#         b.append(10*i+j)
#     a.append(b)
# if 1 <= k <= n:
#     for i in range(m):
#         print(a[i][k])

#9-masala
# a = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20]]
# for i in range(0,len(a),2):
#     print(a[i])

#10-masaal
# a = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20]]
# for i in a:
#     for j in range(1, len(i), 2):
#         print(i[j], end="\t")
#     print()

#11-masala
# a = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20]]
# k = 0
# for i in a:
#     if k % 2 == 1:
#         i.reverse()
#         print(i)
#     else:
#         print(i)
#     k += 1

#12-masala
# a = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20]]
# from def_matrix import Print
# Print(a)
# print()
# b = len(a) - 1
# for i in a:
#     for j in range(len(i)):
#         if j % 2 == 0:
#             print(i[j], end="\t")
#         else:
#             print(a[b][j], end="\t")
#     b -= 1
#     print()

#13-masala
# a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
# from def_matrix import Print
# Print(a)
# print()
# for i in range(len(a)):
#     for j in range(len(a[0])-i):
#         print(a[i][j], end=" ")
#     for k in range(len(a)-1-i):
#         print(a[len(a)-1-k][len(a[0])-1-i], end=" ")

#14-masala
# a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
# from def_matrix import Print
# Print(a)
# print()
# for i in range(len(a)):
#     for j in range(len(a[0])-1-i):
#         print(a[j][i], end=" ")
#     for k in range(i, len(a[0])):
#         print(a[len(a)-1-i][k], end=" ")

#15-masala
# a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
# from def_matrix import Print
# Print(a)
# print()
# for i in range(len(a)):
#     for j in range(i, len(a[0])-i):
#         print(a[i][j], end=" ")
#     for k in range(i+1, len(a[0])-i):
#         print(a[k][len(a[0])-1-i], end=" ")
#     for l in range(i+1, len(a[0])-i):
#         print(a[len(a)-1-i][len(a[0])-1-l], end=" ")
#     for m in range(i+1, len(a)-1-i):
#         print(a[len(a)-1-m][i], end=" ")

#16-masala
# a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
# from def_matrix import Print
# Print(a)
# print()
# for i in range(len(a)):
#     for k in range(i, len(a[0])-i):
#         print(a[i][len(a[0])-1-k], end=" ")
#     for j in range(i+1, len(a)-i):
#         print(a[j][i], end=" ")
#     for l in range(i+1, len(a[0])-i):
#         print(a[len(a)-1-i][l], end=" ")
#     for m in range(i+1, len(a)-1-i):
#         print(a[len(a)-1-m][len(a[0])-1-i], end=" ")

#2. Matritsa elementlarini tahlil qilish
#17-masala
# a = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20]]
# k = int(input("k = "))
# p, s = 1, 0
# if 0 <= k <= len(a):
#     for i in a[k]:
#         s += i
#         p *= i
# print(s, p)

#18-masala
# a = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20]]
# k = int(input("k = "))
# p, s = 1, 0
# if 0 <= k <= len(a):
#     for i in range(len(a)):
#         s += a[i][k]
#         p *= a[i][k]
# print(s, p)

#19-masala
# a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
# for i in a:
#     b = 0
#     for j in i:
#         b += j
#     print(b)

#20-masala
# a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
# from def_matrix import Print
# Print(a)
# print()
# for i in range(len(a[0])):
#     s = 0
#     for j in range(len(a)):
#         s += a[j][i]
#     print(s, end='\t')

#21-masala
# a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
# d = (len(a[0])//2)
# from def_matrix import Print
# Print(a)
# print()
# for i in a:
#     s = 0
#     for j in range(1, len(i), 2):
#         s += i[j]
#     print(s/d)

#22-masala
# a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
# d = (len(a)+1)//2
# from def_matrix import Print
# Print(a)
# print()
# for i in range(len(a[0])):
#     s = 0
#     for j in range(0, len(a), 2):
#         s += a[j][i]
#     print(s/d, end="\t")

#23-masala
# a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
# for i in a:
#     print(min(i))

#24-masala
# a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
# for i in range(len(a[0])):
#     max = a[0][i]
#     for j in range(len(a)):
#         if max < a[j][i]:
#             max = a[j][i]
#     print(max)

#25-masala
# a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
# b = []
# for i in a:
#     c = 0
#     for j in i:
#         c += j
#     b.append(c)
# print(b.index(max(b)), max(b))

#26-masala
# a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
# b = []
# for i in range(len(a[0])):
#     p = 1
#     for j in range(len(a)):
#         p *= a[j][i]
#     b.append(p)
# print(b.index(min(b)), min(b))

#27-masala
# a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
# b = []
# for i in range(len(a[0])):
#     c = a[0][i]
#     for j in range(1, len(a)):
#         if c < a[j][i]:
#             c = a[j][i]
#     b.append(c)
# print(min(b))

#28-masala
# a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
# b = []
# for i in a:
#     b.append(min(i))
# print(max(b))

#29-masala
# a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
# for i in a:
#     b = sum(i) / len(i)
#     for j in i:
#         if j < b:
#             print(j, end=" ")
#     print()

#30-masala
# a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
# b = []
# for i in range(len(a[0])):
#     s = 0
#     for j in range(len(a)):
#         s += a[j][i]
#     s /= len(a)
#     k = 0
#     for p in range(len(a)):
#         if a[p][i] > s:
#             k += 1
#     print(k, end=" ")

#31-masala
# a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
# b = []
# for i in a:
#     b.append(sum(i))
# c = sum(b) / (len(a) * len(a[0]))
# print(c)
# x = abs(c - a[0][0])
# z, y = 0, 0
# for i in range(len(a)):
#     for j in range(len(a[0])):
#         d = abs(c - a[i][j])
#         if x > d:
#             x, z, y = d, i, j
# print(a[z][y])
# print("ustuni:", y)
# print("satri:", z)

#32-masala
# a = [[1, 2, 3, 4, 5, 0], [6, 7, -8, -9, 10, -2], [11, 12, 13, 14, 15, 6], [16, -17, 18, -19, 20, -1]]
# for i in a:
#     k, l = 0, 0
#     for j in i:
#         if j > 0: k += 1
#         else: l += 1
#     if k == l:
#         print(i)
#         break

#33-masala
