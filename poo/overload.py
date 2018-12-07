def func(*args):
    for arg in args:
        print(arg)


def func2(arg=10):
    print(arg)


def func3(**kwargs):
    for chave in kwargs:
        print(kwargs[chave])


func3(meu_nome='Marcos', seu_nome='José')
