import numpy as np


def f(x, y):
    # derivative of y according to x
    return x * np.exp(3 * x) - 2 * y


def y(x):
    return 1 / 5 * x * np.exp(3 * x) - 1 / 25 * np.exp(3 * x) + 1 / 25 * np.exp(-2 * x)


if __name__ == "__main__":
    n = int(input("Nhập số nghiệm cần tìm: "))
    y0 = float(input("y0 = "))
    x0 = float(input("x0 = "))
    h = float(input("h = "))
    for i in range(n):
        y_tmp = y0 + h * f(x0, y0)
        x_tmp = x0 + h
        y0 = y0 + h * (f(x0, y0) + f(x_tmp, y_tmp)) / 2
        x0 = x0 + h
        print(f"y{i + 1} = {y0: 20} - actual value = {y(x0): 20} với x{i + 1} = {x0}")
