"""
K1 = f(x_i, y_i)
K2 = f(x_i + h/2, y_i + h/2*K1)
K3 = f(x_i + h/2, y_i + h/2*K2)
K4 = f(x_i + h, y_i + h*K3)

y_i+1 = y_i + h/6 * (K1 + 2K2 + 2K3 + K4)
"""


def f(x_i, y_i):
    return 1 + y_i + x_i ** 2


def RK4(n, h, x_0, y_0):
    for i in range(n):
        K1 = f(x_0, y_0)
        K2 = f(x_0 + h / 2, y_0 + K1 * h / 2)
        K3 = f(x_0 + h / 2, y_0 + K2 * h / 2)
        K4 = f(x_0 + h, y_0 + K3 * h)
        y_0 = y_0 + h / 6 * (K1 + 2 * K2 + 2 * K3 + K4)
        x_0 = x_0 + h
        print(f"y_{i + 1} = {y_0} tại x_{i + 1} = {x_0}")


if __name__ == "__main__":
    n = int(input("Nhập số nghiệm cần tìm: n = "))
    h = float(input("Nhập khoảng cách giữa các điểm: h = "))
    x, y = map(float, input("Nhập điểm ban đầu (cách nhau bởi dấu cách): x_0, y_0 = ").split())
    RK4(n, h, x, y)
