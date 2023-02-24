from matplotlib import pyplot as plt
import numpy as np
import math

def f(x):
    return x**3 + 4 * x**2 + x - 6

def solve():
    left = 0.0
    right = 2.0
    m = (left + right) / 2.0
    while left != m and m != right:
        if f(m) < 0:
            left = m
        else:
            right = m
        m = (left + right) / 2.0
    return right

print(solve())

f2 = np.vectorize(f)
x = np.arange(0, 2, 0.01)
y = f2(x)

plt.plot(x, y)
plt.grid()
plt.show()
