a1,b1,c1, a2,b2,c2 = 1,1,5, 2,-1,4
k = a1 / a2
y = (c1 - c2 * k) / (b1 - k * b2)
x = (c1 - b1 * y) / a1
print("x = ", x)
print("y = ", y)