from numpy.ma import exp


def sigmoid(x):
    return 1 / (1 + exp(-x))


if __name__ == '__main__':
    print("a[{}]".format(sigmoid(2 * 0.4 + 6 * 0.6 - 2)))
    print("b[{}]".format(sigmoid(3 * 0.4 + 5 * 0.6 - 2.2)))
    print("a[{}]".format(sigmoid(5 * 0.4 + 4 * 0.6 - 3)))
