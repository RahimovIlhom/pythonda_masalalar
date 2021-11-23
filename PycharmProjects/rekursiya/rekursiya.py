# def ekub_top(a, b):
#     if b == 0:
#         return a
#     else:
#         return ekub_top(b,a%b)
# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# x = a**b - c
# print(ekub_top(x, d))


# def raq_yig(a):
#     if a == 0:
#         return 0
#     else:
#         return a%10+raq_yig(a//10)
# print(raq_yig(666))

# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# n = 15
# for i in range(1,n+1):
#     print(fib(i), end = " ")

# def fac(a,k):
#     if a == 0 or k==0 or k==a:
#         return 1
#     else:
#         return fac(a-1,k)+fac(a-1,k-1)
# m, n = 5, 3
# print(fac(m,n))

