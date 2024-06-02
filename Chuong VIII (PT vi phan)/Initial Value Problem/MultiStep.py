def f(x_i, y_i):
    return 1 + y_i + x_i ** 2


def twostep():
    pass


if __name__ == "__main__":
    n = int(input("Nhập số nghiệm cần tìm: n = "))
    h = float(input("Nhập khoảng cách giữa các điểm: h = "))
    x, y = map(float, input("Nhập điểm ban đầu (cách nhau bởi dấu cách): x_0, y_0 = ").split())
    
