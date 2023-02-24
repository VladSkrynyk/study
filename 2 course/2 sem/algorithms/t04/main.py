from matplotlib import pyplot as plt
import numpy as np
import math


def f1(x):
    return math.sin(x)

def f2(x):
    return (x / 3.0)


f11 = np.vectorize(f1)
f22 = np.vectorize(f2)
x = np.arange(1, 4, 0.1)
y1 = f11(x)
y2 = f22(x)

plt.plot(x, y1, color="r")
plt.plot(x, y2, color="g")
#print(f(1.378796700129551))
#plt.scatter([1.3787967001295507], [f(1.3787967001295507)], color="red") # plotting single point
plt.grid()
plt.show()
