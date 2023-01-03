
def func(x: float) -> 'int':
    return x


def main():
    a = 0
    for b in range(0, 10, 2):
        a += b + 1
    print(a)
    test = [1, 2, 3, 4]
    for i in test:
        index = test.index(i)
        print(index)
        test[index] = index
    print(test)
    print(len(test))

    test1 = func('12')
    print(test1)
    print(type(test1))
    print(func.__annotations__)


if __name__ == "__main__":
    main()
