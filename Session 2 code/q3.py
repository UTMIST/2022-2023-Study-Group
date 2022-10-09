#  Homework 1 Problem 2(C)
import math
import matplotlib.pyplot as plt
import numpy as np


# part C1
def relu(x):
    g = 1
    if x < 0:
        return 0
    else:
        return g * x


# part C2
def sigmoid(x):
    return 1 / (1 + math.e ** (-1 * x))


# part C3
def soft_max(x):
    return np.exp(x - np.max(x)) / np.sum(np.exp(x - np.max(x)), axis=0)


if __name__ == "__main__":
    x = np.linspace(-5, 5, num=5000)
    y = sigmoid(x)
    # y = np.linspace(-5, 5, num=5000)
    # for i in range(len(x)):
    #     y[i] = relu(x[i])
    plt.scatter(x, y)
    plt.show()
