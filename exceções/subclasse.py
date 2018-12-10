from subclasse import MinhaExcecao

class MinhaExcecao(Exception):
    def __init__(self, *args):
        if(len(args) > 0):
            super().__init__(args[0])
        else:
            super().__init__('Você quebrou o meu ovo')


raise MinhaExcecao('Oloco bixo')
