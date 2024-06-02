import numpy as np
from scipy.integrate import odeint
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

# Define the system of ODEs
def f(y, x):
    dy1dx = y[1]
    dy2dx = 2 * (y[1] ** 2) * (x ** -3) - 9 * (y[0] ** 2) * (x ** -5) + 4 * x
    return [dy1dx, dy2dx]

# Define the shooting method function
def shooting(guess):
    y0 = [0, guess]  # initial condition with guess for y'(1)
    odesolver = odeint(f, y0, x)
    return odesolver[:, 0][-1] - y_target

# Define target boundary condition
y_target = np.log(256)
x = np.arange(1, 2 + 0.05, 0.05)  # using step size h = 0.05

# Initial guess for y'(1)
initial_guess = 2

# Solve for the correct initial slope
# y1_initial = fsolve(shooting, initial_guess)[0]

# Solve the ODE with the found initial slope
y0 = [0, 0.05]
solution = odeint(f, y0, x)

# Plot the results
plt.plot(x, solution[:, 0], label='Numerical solution y(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solution of the BVP using Shooting Method')
plt.legend()
plt.grid(True)
plt.show()

# Compare with the actual solution y(x) = x^3 * ln(x)
actual_solution = x**3 * np.log(x)
plt.plot(x, actual_solution, 'r--', label='Actual solution y(x) = x^3 ln(x)')
plt.plot(x, solution[:, 0], 'b-', label='Numerical solution y(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Comparison of Numerical and Actual Solution')
plt.legend()
plt.grid(True)
plt.show()
