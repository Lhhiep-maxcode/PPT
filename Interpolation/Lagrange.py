import math


# Tính giá trị đa thức nội suy Lagrange tại một điểm x
def lagrange_interpolation(x_values, y_values, x):
    result = 0.0

    for i in range(len(x_values)):
        term = y_values[i]
        for j in range(len(x_values)):
            if j != i:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term

    return result


# Xây dựng đa thức nội suy Lagrange
def interpolate_polynomial(x_values, y_values):
    n = len(x_values)
    interpolated_polynomial = ""

    for i in range(n):
        term = f'{y_values[i]}'
        for j in range(n):
            if j != i:
                term += f' * (x - {x_values[j]}) / ({x_values[i]} - {x_values[j]})'
        interpolated_polynomial += term

    return interpolated_polynomial


# Tính giá trị của hàm số f(x) = sin(x)
def f(x):
    return math.sin(x)


# Tính giá trị đạo hàm thứ hai f''(x) cho hàm số f(x) = sin(x) trên khoảng [0, pi/2]
def f_double_prime(x):
    if x == 0:
        return 0
    elif x == math.pi / 2:
        return -1
    else:
        return -f(x)


# Các điểm mốc và giá trị tương ứng
x_values = [0, math.pi / 6, math.pi / 3, math.pi / 2]
y_values = [f(x) for x in x_values]
y_double_prime_values = [f_double_prime(x) for x in x_values]

# Xây dựng đa thức nội suy
interpolated_polynomial = interpolate_polynomial(x_values, y_values)

# Tính giá trị đa thức nội suy tại một điểm x_input bất kỳ
x_input = math.pi / 4
interpolated_value = lagrange_interpolation(x_values, y_values, x_input)

# In kết quả
print(f"Đa thức nội suy: f(x) ≈ {interpolated_polynomial}")
print(f"Giá trị đa thức nội suy tại x = {x_input}: {interpolated_value}")
