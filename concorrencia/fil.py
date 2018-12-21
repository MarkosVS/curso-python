from threading import (Thread, Semaphore)
from time import sleep
from random import randint as rand

garfos = []


def filosofo(id):
    while(True):
        # tenta pegar os garfos
        garfos[id].acquire()
        garfos[(id + 1) % len(garfos)].acquire()
        # pegou os garfos e vai comer
        print('Filosofo {} comendo'.format(id))
        t = rand(3, 7)
        sleep(t)
        # comeu
        print('Filosofo {} comeu por {}s'.format(id, t))
        # libera os garfos
        garfos[id].release()
        garfos[(id + 1) % len(garfos)].release()
        # terminou de comer, vai pensar
        print('Filosofo {} pensando'.format(id))
        t = rand(2, 6)
        sleep(t)
        # pensou
        print('Filosofo {} pensou por {}s'.format(id, t))


def main():
    for i in range(5):
        garfos.append(Semaphore(1))

    for i in range(5):
        f = Thread(target=filosofo, args=(i, ))
        f.start()


if(__name__ == '__main__'):
    main()
