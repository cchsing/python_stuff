import random


def make_data():
    x1 = random.randint(0, 1)
    x2 = random.randint(0, 1)
    yy = 0 if (x1 == x2) else 1

    # centered at zero
    x1 = 2. * (x1 - 0.5)
    x2 = 2. * (x2 - 0.5)
    yy = 2. * (yy - 0.5)

    # add noise
    x1 += 0.1 * random.random()
    x2 += 0.1 * random.random()
    yy += 0.1 * random.random()

    return [x1, x2, ], yy


def main():
    for i in range(0, 6, 1):
        print(i)
    var1 = "test1"
    var2 = "test2"
    var3 = "test3 test4 test5"
    var3 = var3.split()
    test = []
    test.append(var1)
    test.append(var2)
    test = test + var3
    print(test)
    test2 = []
    test2 = var3
    print(test2)

    data_1 = make_data()
    xx, yy = data_1
    print(yy)


if __name__ == "__main__":
    main()
