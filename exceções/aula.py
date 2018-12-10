from subclasse import MinhaExcecao


def menu():
    print('Selecione uma opção:')
    print('(1) - Opção x')
    print('(2) - Opção y')
    print('(3) - Opção z')
    while(True):
        try:
            resposta = int(input())
        except ValueError:
            resposta = -1
        finally:
            if(resposta in (1, 2, 3)):
                return resposta
            else:
                raise MinhaExcecao
            print('Digite um valor válido')
