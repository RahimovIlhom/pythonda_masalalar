#1-masala
# n = 20
# s = 'Salom Ilhomjon'
# if len(s) > n:
#     print(s[:n])
# else:
#     print(s+'.'*(n-len(s)))

#2-masala
# n1, n2 = 8, 12
# s1 = "Ilhomjon Rahimov"
# s2 = "Iqboljon Xojibolayev"
# print(s1[:n1]+s2[-n2:-1]+s2[len(s2)-1])

#3-masala
# s = 'computer'
# c = 'c'
# for i in s:
#     if i == c:
#         s = s.replace(c, 2*c)
# print(s)

#4-masala
# s = 'salom dunyo'
# s0 = "qo'shimcha"
# c = 'o'
# s = s.replace(c, s0+c)
# print(s)

#5-masala
# s = 'salom dunyo'
# s0 = "qo'shimcha"
# c = 'o'
# s = s.replace(c, c+s0)
# print(s)

#6-masala
# s = 'Assalomu alaykum'
# s0 = 'salom'
# print(s0 in s)

#7-masala
# s = 'Assalomu alaykum, salom, salom, salom'
# s0 = 'salom'
# k = 0
# for i in range(len(s)-len(s0)+1):
#     if s[i: i+len(s0)] == s0:
#         k += 1
# print(k)

#8-masala
# s = 'Assalomu alaykum salom'
# s0 = 'salom'
# print(s.replace(s0, "", 1))

# 9-masala
# s = 'Assalomu alaykum, salom, salom, salom'
# s0 = 'salom'
# k = 0
# for i in range(len(s)-len(s0)+1):
#     if s[i: i+len(s0)] == s0:
#         k += 1
# s = s.replace(s0, 'kalit')
# s = s.replace('kalit', s0, k-1)
# s = s.replace('kalit', '')
# print(s)

#10-masala
# s = 'Assalomu alaykum, salom, salom, salom'
# s0 = 'salom'
# print(s.replace(s0, ''))

#11-masala
# s = 'Assalomu alaykum, salom, salom, salom'
# s1 = 'salom'
# s2 = 'tugadi'
# print(s.replace(s1, s2, 1))

#12-masala
# s = 'Assalomu alaykum, salom, salom, salom'
# s0 = 'salom'
# s1 = 'tugadi'
# k = 0
# for i in range(len(s)-len(s0)+1):
#     if s[i: i+len(s0)] == s0:
#         k += 1
# s = s.replace(s0, 'kalit')
# s = s.replace('kalit', s0, k-1)
# s = s.replace('kalit', s1)
# print(s)

#13-masala
# s = 'Assalomu alaykum, salom, salom, salom'
# s1 = 'salom'
# s2 = 'tugadi'
# print(s.replace(s1, s2))

#14-masala
# s = 'Assalomu alaykum, salom, salom, salom'
# s1 = 'salom'
# s2 = 'tugadi'
# k = 0
# a = []
# for i in range(len(s)):
#     if s[i] == ' ':
#         k += 1
#         a.append(i)
#         if k == 2:
#             break
# if k > 1:
#     print(s[a[0]:a[1]])
# else:
#     print()

#15-masala
s = 'Assalomu alaykum, salom, salom, salom'
s1 = 'salom'
s2 = 'tugadi'
k = 0
a = []
for i in range(len(s)):
    if s[i] == ' ':
        k += 1
        a.append(i)
print(s[a[0]:a[-1]])