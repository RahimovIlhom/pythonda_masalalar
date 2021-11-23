class Array:
    def __init__(self, ar):
        self.ar = ar
    def sum(self):
        s = 0
        for i in self.ar:
            s += i
        return f'The sum of the elements of the array:{s}'
    def multi(self):
        p = 1
        for i in self.ar:
            p *= i
        return f'Multiplication of array elements:{p}'
    def max(self):
        return f'The maximum of the array:{max(self.ar)}'
    def max_index(self):
        s = 0
        a = max(self.ar)
        for i in range(len(self.ar)):
            if self.ar[i] == a:
                s = i
        return f'The maximum index of the array:{s}'
    def min(self):
        return f'The minimum of the array:{min(self.ar)}'
    def min_index(self):
        s = 0
        a = min(self.ar)
        for i in range(len(self.ar)):
            if self.ar[i] == a:
                s = i
        return f'The minimum index of the array:{s}'
    def sort(self):
        return f'Massif selected: {sorted(self.ar)}'
    def date(self):
        a = sorted(self.ar)
        i = 0
        while(a[i] < 0):
            i += 1
        return f'Number of positive elements: {len(a) - i}\n' \
               f'The number of negative elements: {i}'
    def probel_rigth(self, k):
        a = []
        for i in range(-k,len(self.ar)-k):
            a.append(self.ar[i])
        return Array(a)
    def probel_left(self, k):
        a = []
        for i in range(k,len(self.ar)):
            a.append(self.ar[i])
        for i in range(0, -k, -1):
            a.append(self.ar[i])
        return Array(a)
    def __add__(self, other):
        a = []
        if len(self.ar) < len(other.ar):
            for i in range(len(self.ar)):
                a.append(self.ar[i] + other.ar[i])
        else:
            for i in range(len(other.ar)):
                a.append(self.ar[i] + other.ar[i])
        return Array(a)
    def __sub__(self, other):
        a = []
        if len(self.ar) < len(other.ar):
            for i in range(len(self.ar)):
                a.append(self.ar[i] - other.ar[i])
        else:
            for i in range(len(other.ar)):
                a.append(self.ar[i] - other.ar[i])
        return Array(a)
    def __mul__(self, other):
        a = []
        if type(other) != int:
            if len(self.ar) < len(other.ar):
                for i in range(len(self.ar)):
                    a.append(self.ar[i] * other.ar[i])
            else:
                for i in range(len(other.ar)):
                    a.append(self.ar[i] * other.ar[i])
            return Array(a)
        else:
            for i in range(len(self.ar)):
                a.append(self.ar[i] * other)
            return Array(a)
    def __truediv__(self, other):
        a = []
        if type(other) != int:
            if len(self.ar) < len(other.ar):
                for i in range(len(self.ar)):
                    a.append(self.ar[i] / other.ar[i])
            else:
                for i in range(len(other.ar)):
                    a.append(self.ar[i] / other.ar[i])
            return Array(a)
        elif other != 0:
            for i in range(len(self.ar)):
                a.append(self.ar[i] / other)
            return Array(a)
        else:
            return 'The array is not divisible by zero.'
    def __pow__(self, power, modulo=None):
        a = []
        for i in range(len(self.ar)):
            a.append(self.ar[i] ** power)
        return Array(a)
    def bank_profit(self, other):
        if len(self.ar) == len(other.ar):
            summ = 0
            for i in range(len(self.ar)):
                summ += (self.ar[i] * (1 + other.ar[i] / 100))
            return f'Annual profit of the bank: {summ}'
        else:
            return 'The elements of the arrays are not equal'
    def super_market(self, price, count):
        l = len(self.ar)
        if l == len(price.ar) and l == len(count.ar):
            summ = 0
            a = []
            for i in range(l):
                summ += price.ar[i] * count.ar[i]
                a.append(self.ar[i] - count.ar[i])
            return f'One day trade:{summ}\n' \
                   f'Grain of the remaining goods:{Array(a)}'
        else:
            return 'The elements of the arrays are not equal'
    def circle_game(self, k):
        a = self.ar
        b = a.copy()
        p = k
        while len(a) != 1:
            k = p
            if k == len(a):
                a.pop(k-1)
            else:
                k = k % (len(a))
                if k == 0:
                    a.pop(len(a)-1)
                else:
                    a.pop(k-1)
        return f'{b.index(a[0])+1} players win'
    def reverse(self):
        a = []
        l = len(self.ar)
        for i in range(l-1, -1, -1):
            a.append(self.ar[i])
        return Array(a)
    def __str__(self):
        return str(self.ar)