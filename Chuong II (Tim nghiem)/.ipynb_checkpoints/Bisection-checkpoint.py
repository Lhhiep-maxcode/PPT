import math

def bisection(left, right, tol, iternums=1e5):
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
        return bisection(mid, right, tol, iternums - 1)
    elif f_mid * f_right > 0:
        return bisection(left, mid, tol, iternums - 1)
    return mid


if __name__ == '__main__':
    f = lambda x: x - 2 ** (-x)
    tol = 10 ** -5
    bisection(left=0, right=1, tol=tol)

math.e