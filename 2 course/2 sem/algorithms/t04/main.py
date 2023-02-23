from matplotlib import pyplot as plt
import numpy as np
import math

def binary_continuous(f, c, a, b):
     """ Для монотонної на відрізку [a, b] функції f розв'язує рівняння
     f(x) = c
     :param f: Монотонна функція
     :param c: Шукане значення
     :param a: Ліва межа проміжку на якому здійснюється пошук
     :param b: Права межа проміжку на якому здійснюється пошук
     :return: Розв'язок рівняння
     """
     left = a # лівий кінець відрізка
     right = b # правий кінець відрізка
     m = (left + right) / 2.0 # середина відрізка [left,right]
     while left != m and m != right:
        if f(m) < c:
            left = m # [left,right] = [x,right]
        else:
            right = m # [left,right] = [left,x]
        m = (left + right) / 2.0 # середина відрізка [left,right]
     return left

def f(x):
    return x**2 + math.sqrt(x)

#print(binary_continuous(lambda x: math.tan(x) - 2.0 * x, 0, 0.5, 1.5))

f2 = np.vectorize(f)
x = np.arange(0.5, 15, 0.1)
y = f2(x)

plt.plot(x, y)
plt.grid()
plt.show()