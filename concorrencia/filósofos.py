from threading import (Thread, Semaphore)
from time import sleep
from random import randint as rand
garfos = []


def filosofo(num):
    print('Filosofo {} iniciado'.format(num))

    while(True):
        # tentativas de pegar os garfos
        # caso seja o último filósofo
        if(num == len(garfos) - 1):
            # pega o garfo à direita
            garfos[(num - 1) % len(garfos)].acquire()
            # pega o garfo à esquerda
            garfos[num].acquire()
        # caso não seja o ultimo
        else:
            # pega o garfo à esquerda
            garfos[num].acquire()
            # pega o garfo à direita
            garfos[(num - 1) % len(garfos)].acquire()

        # filosofo pega os garfos e come
        print('Filosofo {} comendo'.format(num))
        t_comida = rand(3, 7)
        sleep(t_comida)
        print('Filosofo {} comeu em {}s'.format(num, t_comida))

        # liberação dos garfos
        # caso seja o último filósofo
        if(num == len(garfos) - 1):
            # libera o garfo à direita
            garfos[(num - 1) % len(garfos)].release()
            # libera o garfo à esquerda
            garfos[num].release()
        # caso não seja o ultimo
        else:
            # libera o garfo à esquerda
            garfos[num].release()
            # libera o garfo à direita
            garfos[(num - 1) % len(garfos)].release()

        # filosofo libera os garfos e vai pensar
        print('Filosofo {} pensando'.format(num))
        t_pensar = rand(2, 6)
        sleep(t_pensar)
        print('Filosofo {} pensou por {}s'.format(num, t_pensar))


def main():
    for i in range(5):
        garfos.append(Semaphore(1))

    for i in range(5):
        t = Thread(target=filosofo, args=(i, ))
        t.start()


if(__name__ == '__main__'):
    main()
