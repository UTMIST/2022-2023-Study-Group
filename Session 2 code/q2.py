# Homework 1 Problem 1

def indicator_fcn(x):
    if x <= 0:
        return 0
    else:
        return 1


def NOR(x1, x2):
    return indicator_fcn(1 + x1 * -1 + x2 * -1)


def AND(x1, x2):
    return indicator_fcn(-1 + x1 * 1 + x2 * 1)


def OR(x1, x2):
    return indicator_fcn(-1 + 2 * x1 + 2 * x2)


def XNOR(x1, x2):
    and_r = AND(x1, x2)
    nor_r = NOR(x1, x2)
    return OR(and_r, nor_r)


def NOT(x1):
    w = -1
    b = 1
    return indicator_fcn(x1 * w + b)


if __name__ == "__main__":

    test_not = [1, 1.4, 0, -0.5]
    test = [[0, 0], [0, 1], [1, 0], [1, 1]]

    # for i in range(len(test_not)):
    #     print( NOT(test_not[i]))

    for i in range(len(test)):
        print(XNOR(test[i][0], test[i][1]))
