import numpy as np


def rowInterchange(A, m, i):
    tmp = np.copy(A[i])
    A[i] = A[m]
    A[m] = tmp


def backSubstitute(A, x):
    sysSize = len(A)
    varSize = len(x)
    for i in reversed(range(sysSize)):
        x[i] = 1 / A[i, i] * (A[i, varSize] - A[i, i + 1:varSize] @ x[i + 1:varSize])


def gaussElimination(A, x, b):
    print("\nGauss Elimination Method:")
    A = np.array(A)
    x = np.array(x)
    b = np.array(b)
    A = np.concatenate((A, b), axis=1)
    sysSize = len(A)
    for i in range(sysSize):
        m = i
        for k in range(i + 1, sysSize):
            if abs(A[k, i]) > abs(A[m, i]):
                m = k
        if A[m, i] == 0:
            return "No unique solution"
        rowInterchange(A, m, i)
        for k in range(i + 1, sysSize):
            m_ki = A[k, i] / A[i, i]
            A[k] = A[k] - m_ki * A[i]
    backSubstitute(A, x)
    print(x.reshape(1, -1))
    return list(x)


def gaussSeidel(A, x, b, epsilon, iterNums):
    print("\nGauss-Seidel Method:")
    A = np.array(A)
    x = np.array(x)
    b = np.array(b)
    xSize = len(x)
    for i in range(iterNums):
        x_old = np.array(x)
        for j in range(xSize):
            x[j] = 1.0 / A[j, j] * (b[j, 0] - (A[j] @ x - A[j, j] * x[j, 0]))
        print(x.reshape((1, -1)))
        if np.max(np.abs(x_old - x)) < epsilon:
            print(np.max(np.abs(x_old - x)))
            return list(x)

    return list(x)


def jacobi(A, x, b, epsilon, iterNums):
    print("\nJacobi Method:")
    A = np.array(A)
    x = np.array(x)
    b = np.array(b)
    xSize = len(x)
    for i in range(iterNums):
        x_old = np.array(x)
        for j in range(xSize):
            x[j] = 1.0 / A[j, j] * (b[j, 0] - (A[j] @ x_old - A[j, j] * x_old[j, 0]))
        print(x.reshape((1, -1)))
        if np.max(np.abs(x - x_old)) < epsilon:
            print(np.max(np.abs(x - x_old)))
            return list(x)
    return list(x)


if __name__ == '__main__':
    A = [[-3., 6., -9.],
         [1., -4., 3.],
         [2., 5., -7.]]
    x = [[0.],
         [0.],
         [0.]]
    b = [[-46.725],
         [19.571],
         [-20.073]]
    gaussElimination(A, x, b)
    gaussSeidel(A, x, b, 0, 10)
    jacobi(A, x, b, 0, 10)
