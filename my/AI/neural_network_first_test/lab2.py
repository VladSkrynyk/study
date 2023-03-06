from matplotlib import pyplot as plt # підключаємо необхідні бібліотеки
import numpy as np
from sympy.solvers import solve
from sympy import Symbol
import warnings

warnings.filterwarnings("ignore")


def g(y0):
    return y0, 0, 2 - y0 - y0 ** 2 + y0, 0


X, Y, U, V = g(0)
plt.quiver(X, Y, U, V, color='b', units='xy', scale=1.2)

X, Y, U, V = g(1)
Y += 0.15
plt.quiver(X, Y, U, V, color='r', units='xy', scale=3)

X, Y, U, V = g(-1)
Y += 0.25
plt.quiver(X, Y, U, V, color='r', units='xy', scale=0.65)

X, Y, U, V = g(2)
Y -= 0.15
plt.quiver(X, Y, U, V, color='g', units='xy', scale=0.6)

X, Y, U, V = g(-2)
Y -= 0.25
plt.quiver(X, Y, U, V, color='g', units='xy', scale=5)

X, Y, U, V = g(3)
Y += 0.5
plt.quiver(X, Y, U, V, color='y', units='xy', scale=0.6)

X, Y, U, V = g(-3)
Y += 0.35
plt.quiver(X, Y, U, V, color='y', units='xy', scale=1)

X, Y, U, V = g(4)
Y -= 0.55
plt.quiver(X, Y, U, V, color='black', units='xy', scale=0.6)

X, Y, U, V = g(-4)
Y -= 0.65
plt.quiver(X, Y, U, V, color='black', units='xy', scale=1)

# 0  -> 2
# 1  -> 1
# -1 -> 1
# 2  -> -2
# -2 -> -2
# 3  -> -7
# -3 -> -7
# 4  -> -14
# -4 -> -14

plt.xlim(-6, 6)
plt.ylim(-1, 1)
plt.grid()
plt.show()


from sympy import *

y = Symbol("y")
g = 2 - y**2 - y
print(diff(g, y))
print(f"Екстремуми : {solve(g, y, dict=True)}")
print(f"Функція зростає : {solve(g > 0, y, dict=True)}")
print(f"Функція спадає : {solve(g < 0, y, dict=True)}")
dots = solve(simplify(diff(g, y) * g))
print(f"Множини точок перегину : {dots}")

plt.rcParams["figure.figsize"] = (9,7)

y1 = np.linspace(-2, 1-np.e, 400)
y2 = np.linspace(-6, -2-np.e, 400)
y3 = np.linspace(1, 6, 400)

def f(p):
    return 2-p**2-p

plt.plot(y1,f(y1),'b', label = "Зростає")
plt.plot(y2,f(y2),'orange', label = "Спадає")
plt.plot(y3,f(y3),color='orange', label = "Спадає")
plt.plot([-2],[f(-2)],'go',[1/2],[f(1/2)],'go',[1],[f(1)],'go', label = 'Точка перегину')

plt.grid(True)
plt.legend()
plt.show()

from sympy import *
from sympy.abc import y
g =2 -y**2 -y
integrate(1/g, y)

def axes():
    plt.axhline(0, alpha=.1)
    plt.axvline(0, alpha=.1)
axes()

x = np.linspace(-12, 12, 400)
y = np.linspace(-12, 12, 400)

e = 10**(-10)

def f(y):
    return (np.log(np.abs(y+2)/np.abs(y-1)))/3
axes()
y = np.linspace(-3,1-e, 400)
plt.plot(f(y), y)
y = np.linspace(1+e, -2-e, 400)
plt.plot(f(y), y,)
y = np.linspace(-2+e,6, 400)
plt.plot(f(y), y,)
x = np.linspace(-6, 6, 400)
y = np.linspace(-2, -2, 400)
plt.plot(x, y,'k--')
x = np.linspace(-6, 6, 400)
y = np.linspace(1, 1, 400)
plt.plot(x, y,'k--')
x = np.linspace(0, 0, 400)
y1 = np.linspace(-3, 1, 400)
y2 = np.linspace(-2, 6, 400)
plt.plot(x, y1,'r--',x, y2,'r--')
plt.plot([f(-2)],[-2],'go',[f(-1/2)],[-1/2],'go',[f(1)],[1],'go', label = 'Точка перегину')

plt.grid(True)
plt.show()

x = np.linspace(0, 2, 400)
y = np.linspace(-1/2, -1/2, 400)

def f1(x):
    return (np.exp(3*x)+2)/(np.exp(3*x)-1)

x = np.linspace(0, 2, 400)
y = np.linspace(-1-1/2, -1-1/2, 400)

def f(y):
    return ((np.log(np.abs(y+2)/np.abs(y-1)))/3)
axes()
e = 10**(-5)
y = np.linspace(-3,1-e, 1000)
plt.plot(f(y), y)
y = np.linspace(1,-1+e, 1000)
plt.plot(f(y), y)

res = np.abs(f(np.linspace(-3,1-e, 1000))-f(np.linspace(1,1+e, 1000))) < 10**(-3)
plt.plot(f(y)[res],y[res],'ro')
y = np.linspace(-3,1-e, 1000)
plt.plot(f(y)[res],y[res],'ro')
plt.show()
np.any(res)
