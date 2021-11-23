class Person:
    __height = None
    __weight = 70
    __age = 22
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self,h):
        if h < 300:
            self.__height = h
        else:
            print('unaqa inson yo\'q')
    @property
    def weight(self):
        return self.__weight
    @weight.setter
    def weight(self,h):
        if h <500:
            self.__weight = h
        else:
            print('unaqa inson yo\'q')
p = Person()
p.height = 174
print(p.height)