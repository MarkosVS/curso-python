class A:
    def __init__(self):
        self.__a = 'a'
        self.b = 'b'


class B(A):
    def __init__(self):
        self.c = 'c'
        super().__init__()

    def __str__(self):
        return "Objeto da classe B"


b = B()
print(b)
a = A()
print(a)
