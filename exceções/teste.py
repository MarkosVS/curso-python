from random import choice

try:
    a = choice((0, 1))
    print(10 / a)
    print(a + '1')
except ZeroDivisionError:
    print('10 / 0 não dá')
else:
    print('10 / 1 dá')
finally:
    print('Cabou')
