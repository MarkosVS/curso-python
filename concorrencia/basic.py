from threading import Thread


def func(arg):
    for i in range(15):
        print(arg)


def main():
    t = Thread(target=func, args=('oi', ))
    t.start()
    t.join()
    print('hahaha')


if(__name__ == '__main__'):
    main()
