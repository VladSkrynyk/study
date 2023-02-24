from matplotlib import pyplot as plt
import numpy as np
import math

def f1(x):
    return math.sin(x)

def f2(x):
    return (x / 3.0)

def f(x):
    return math.sin(x) - (x / 3.0)

def solve():
    left = 1.6
    right = 3.0
    mid = (left + right) / 2.0
    while left != mid and mid != right:
        if f(mid) > 0:
            left = mid
        else:
            right = mid
        mid = (left + right) / 2.0
    return right
print(solve())

f11 = np.vectorize(f1)
f22 = np.vectorize(f2)
x = np.arange(1, 4, 0.1)
y1 = f11(x)
y2 = f22(x)

plt.plot(x, y1, color="r")
plt.plot(x, y2, color="g")

plt.grid()
plt.show()
