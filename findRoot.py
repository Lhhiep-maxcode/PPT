import math


def bisection(left, right, iternums, tol):
    mid = (left + right) / 2
    f_left = f(left)
    f_right = f(right)
    f_mid = f(mid)
    if f_left * f_right > 0:
        print("Left and right are not chosen appropriately, f(left) * f(right) should be less than 0")
        return

    print(mid)
    if ((right - left) / 2) <= tol or iternums == 1:
        return mid
    elif f_left * f_mid > 0:
        return bisection(mid, right, iternums - 1, tol)
    elif f_mid * f_right > 0:
        return bisection(left, mid, iternums - 1, tol)
    return mid


def fixedPoint(iternums, tol, p0):
    for i in range(iternums):
        p = g(p0)
        if abs(p - p0) < tol:
            return p
        p0 = p
        print(p)

    return p0


def newtonMethod(iternums, tol, p0):
    p = p0 - f(p0) / df(p0)
    print(p)
    if abs(p - p0) < tol or iternums == 1:
        return p
    return newtonMethod(iternums - 1, tol, p)


def secantMethod(iternums, tol, p0, p1):
    p = p1 - f(p1) * (p1 - p0) / (f(p1) - f(p0))
    print(p)
    if abs(p - p1) < tol or iternums == 1:
        return p
    return secantMethod(iternums - 1, tol, p1, p)


def falsePosition(iternums, tol, p0, p1):
    p = p1 - f(p1) * (p1 - p0) / (f(p1) - f(p0))
    f_p0 = f(p0)
    f_p1 = f(p1)
    f_p = f(p)
    print(p)
    if abs(p - p1) < tol or iternums == 1:
        return p
    elif f_p0 * f_p < 0:
        return falsePosition(iternums - 1, tol, p0, p)
    elif f_p1 * f_p < 0:
        return falsePosition(iternums - 1, tol, p1, p)
    return p


def choice():
    return int(input("Choose a method to compute:\n"
                     "1. Bisection Method\n"
                     "2. Fixed Point Method\n"
                     "3. Newton Method\n"
                     "4. Secant Method\n"
                     "5. False Position Method\n"))


if __name__ == "__main__":
    f = lambda x: math.e ** x + 2 ** (-x) + 2 * math.cos(x) - 6

    selection = choice()
    iternums = int(input("Number of iterations: "))
    tol = float(input("Tolerance: "))
    if selection == 1:
        print("You have chosen Bisection method!")
        left = float(input("left Point: "))
        right = float(input("right Point: "))
        bisection(left, right, iternums, tol)
    elif selection == 2:
        g = lambda x: (3 * x ** 2 + 3) ** (1 / 4)
        print("You have chosen fixed Point method! Make sure you have defined g(x)")
        p0 = float(input())
        fixedPoint(iternums, tol, p0)
    elif selection == 3:
        df = lambda x: 2 + 6 * x ** 2 / x ** 6 - 4 * x / x ** 4
        print("You have chosen Newton method! Make sure you have defined df(x)")
        p0 = float(input())
        newtonMethod(iternums, tol, p0)
    elif selection == 4:
        print("You have chosen Secant method!")
        p0 = float(input("p0: "))
        p1 = float(input("p1: "))
        secantMethod(iternums, tol, p0, p1)
    elif selection == 5:
        print("You have chosen False Position method!")
        p0 = float(input("p0: "))
        p1 = float(input("p1: "))
        falsePosition(iternums, tol, p0, p1)
