import math


def f(x):
    return math.sin(x)


def newton_interpolation(x, y, target):
    n = len(x)
    coefficients = []

    for i in range(n):
        coefficients.append(y[i])

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coefficients[i] = (coefficients[i] - coefficients[i - 1]) / (x[i] - x[i - j])

    print("Các hệ số phương trình nội suy:")
    for i, coef in enumerate(coefficients):
        print(f"a[{i}] = {coef}")

    result = coefficients[-1]

    for i in range(n - 2, -1, -1):
        result = result * (target - x[i]) + coefficients[i]

    return result


x = [0, math.pi / 6, math.pi / 3, math.pi / 2]
y = [f(val) for val in x]
target = math.pi / 4

interpolated_value = newton_interpolation(x, y, target)
print("The interpolated value at x = pi/34 is:", interpolated_value)
