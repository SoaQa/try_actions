from time import sleep


def foo(a, b):
    return a + b


if __name__ == '__main__':
    while True:
        print(foo(1, 2))
        sleep(3)
