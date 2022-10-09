#  Homework 1 Problem 2(D)
import numpy as np


# D1 - implement mean squared error
def mean_squared_error(yhat, y):
    return np.square(np.subtract(yhat, y)).mean()

# D2 - implement mean absolute error
def mean_absolute_error(yhat,y):
    return np.absolute(np.subtract(yhat, y)).mean()

# D3 - implement hinge error
# guess what? Do it on your own time so u got practice.

if __name__ == "__main__":
    predicted = np.array([0.79, 0.03, 0.031, 0.14, 0.009])
    predicted = np.array([0.031, 0.03, 0.79, 0.14, 0.009])
    actual = np.array([0, 0, 1, 0, 0])

    print("Output layer values:", predicted)
    print("One-Hot Encoded values:", actual)

    print("mean_squared_error loss:", mean_squared_error(predicted, actual))
    print("mean_absolute_error loss:", mean_absolute_error(predicted, actual))
