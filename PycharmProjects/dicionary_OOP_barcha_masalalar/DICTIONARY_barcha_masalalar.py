#1-masala
# diction = {1:2, 2:40, 3:9, 4:10, 5:23, 6:56, 7:12}
# for dict in sorted(diction.values()):
#     print(dict)

#2-masala
# diction = {7:12, 2:40, 3:9, 1:2, 6:56, 4:10, 5:23}
# for dict in sorted(diction):
#     print(f"Kalit:{dict}\tvalue:{diction[dict]}")

#3-masala
# diction = {7:12, 2:40, 3:9, 1:2, 6:56, 4:10, 5:23}
# diction[8] = 50
# diction[9] = 100
# print(diction)

#4-masala
# dic1 = {1:50, 2:100, 3:150}
# dic2 = {4:200, 5:250, 6:300}
# dic3 = {7:350, 8:400, 9:450}
# dic1.update(dic2)
# dic1.update(dic3)
# print(dic1)

#5-masala
# diction = {7:12, 2:40, 3:9, 1:2, 6:56, 4:10, 5:23}
# valu = int(input('value = '))
# if valu in diction.values():
#     print('yes')
# else: print('no')

#6-masala
# diction = {}
# n = int(input('n = '))
# for i in range(1,n+1):
#     diction[i] = i**2
# print(diction)

#7-masala
# diction = {7:12, 2:40, 3:9, 1:2, 6:56, 4:10, 5:23}
# summ = 0
# for value in diction.values():
#     summ += value
# print(summ)

#8-masala
# diction = {7:12, 2:40, 3:9, 1:2, 6:56, 4:10, 5:23}
# del diction[7]
# diction.pop(4)
# print(diction)

#9-masala
# diction = {7:12, 2:40, 3:9, 1:2, 6:56, 4:10, 5:23}
# diction1 = {}
# a, b = [], []
# a, b = list(diction.values()), list(diction1.values())
# print('diction nomli lug\'at bo\'sh emas' if len(a)>0 else 'diction nomli lug\'at bo\'sh')
# print('diction1 nomli lug\'at bo\'sh emas' if len(b)>0 else 'diction1 nomli lug\'at bo\'sh')

#10-masala
d = {}
s = 'assalom'
a = list(set(s))
b = []
for i in a:
    b.append(s.count(i))
for i in range(len(a)):
    d[a[i]] = b[i]
print(d)