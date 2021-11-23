def matrix(n):
    import random
    a = []
    for i in range(n):
        b = []
        for j in range(n):
            b.append(random.randint(1, 100))
        a.append(b)
    return a

# print(matrix(5))