from matplotlib import pyplot as plt # підключаємо необхідні бібліотеки
import numpy as np
from sympy.solvers import solve
from sympy import Symbol
import warnings

warnings.filterwarnings("ignore")

def task1():
    xmax = 6.0
    xmin = -xmax
    D = 13
    ymax = 3.0
    ymin = -ymax
    x = np.linspace(xmin, xmax, D)
    y = np.linspace(ymin, ymax, D)
    X, Y = np.meshgrid(x, y)
    deg = np.arctan(Y**2 + X - 2)
    QP = plt.quiver(X,Y,np.cos(deg),np.sin(deg))
    # plt.grid()
    #plt.axhline(y=0, c='black')
    #plt.axvline(x=0, c='black')
    plt.show()

#task1()

def task2():
    x = np.arange(-6, 6, 0.01)

    y1 = np.sqrt(2 - x)
    y2 = -1 * np.sqrt(2 - x)

    plt.plot(x, y1, color="r")
    plt.plot(x, y2, color="r")

    task1()
    plt.show()

#task2()

def task3():
    x = np.arange(-6, 6, 0.01)
    print(x)
    k = [[1, -1], [0.5, -0.5], [1.5, -1.5]]

    for ki in k:
        y1 = np.sqrt(2 + ki[0] - x)
        y2 = -1 * np.sqrt(2 + ki[0] - x)

        plt.plot(x, y1, color="b", label=f"x = {2 + ki[0]} - x", alpha=0.5)
        plt.plot(x, y2, color="b", label=f"x = {2 + ki[0]} - x", alpha=0.5)

        y1 = np.sqrt(2 + ki[1] - x)
        y2 = -1 * np.sqrt(2 + ki[1] - x)

        plt.plot(x, y1, color="b", label=f"x = {2 + ki[1]} - x", alpha=0.5)
        plt.plot(x, y2, color="b", label=f"x = {2 + ki[1]} - x", alpha=0.5)

    task2()
    plt.show()


#task3()

def task4():
    x = np.arange(-6, 6, 0.01)

    y1 = np.sqrt(2 - x)
    y2 = -1 * np.sqrt(2 - x)

    plt.plot(x, y1, color="r")
    plt.plot(x, y2, color="r")

    plt.fill_between(x, y1, color="b", alpha=.4)
    plt.fill_between(x, y2, color="b", alpha=.4)

    plt.fill_between(x, y1, y2=2.83, color="g", alpha=.4)
    plt.fill_between(x, y2, y2=-2.83, color="g", alpha=.4)

    plt.fill_betweenx(y1, x1=2,x2=6, color="g", alpha=.4, )
    plt.fill_betweenx(y2, x1=2,x2=6, color="g", alpha=.4, )

    task3()
    plt.show()

#task4()

def task5():
    y1 = np.arange(-3, -0.1, 0.01)
    y2 = np.arange(0.06, 3, 0.01)

    plt.plot(2 - y1 * y1 - 1 / (2 * y1), y1, color="magenta")
    plt.plot(2 - y2 * y2 - 1 / (2 * y2), y2, color="magenta")

    task4()
    plt.show()


#task5()

def task6():
    y1 = np.arange(-3, -0.06, 0.01)
    y2 = np.arange(0.01, 2.8, 0.01)

    plt.plot(2 - y1 * y1 - 1 / (2 * y1), y1, color="magenta")
    plt.plot(2 - y2 * y2 - 1 / (2 * y2), y2, color="magenta")

    # plt.fill_between(x, 2 - y1*y1 - 1 / (2*y1), color="black", alpha=.4)
    # plt.fill_between(x, y2, color="b", alpha=.4)
    # y = np.arange(0.01, 2.8, 0.01)
    plt.fill_between(2 - y2 * y2 - 1 / (2 * y2), y2, color='none', hatch="o", edgecolor="g")
    plt.xlim([-7, 7])

    task5()


task6()


points = [[0, -2], [0, 0], [0, 1]]
colors = ["b", "g", "r"]
di = 0

for point in points:
    plt.scatter(point[0], point[1], color=colors[di])
    di += 1

# y(x + delta_x) ~ y^2 + delta_x - x * delta_x - 2 * delta_x + y

###1
x1 = np.arange(0, 4, 0.1)
y1 = []
#print(x1)

prev_x = 0
prev_y = -2
y1.append(prev_y)

dx = 0.1

for i in x1[1:]:
    delta_y = (prev_y**2) * dx - prev_x * dx - 2 * dx + prev_y
    y1.append(delta_y)
    prev_y = delta_y
    prev_x = i

#print(len(y1))
plt.plot(x1, y1, color="b")

x2 = np.arange(0, -4, -0.1)
y2 = []
print(x2)

prev_x = 0
prev_y = -2
y2.append(prev_y)

dx = -0.1

for i in x2[1:]:
    delta_y = (prev_y**2) * dx - prev_x * dx - 2 * dx + prev_y
    y2.append(delta_y)
    prev_y = delta_y
    prev_x = i

plt.plot(x2, y2, color="b")

plt.xlim([-6, 6])
plt.ylim([-3, 3])
###1

###2
x1 = np.arange(0, 4, 0.1)
y1 = []
#print(x1)

prev_x = 0
prev_y = 0
y1.append(prev_y)

dx = 0.1

for i in x1[1:]:
    delta_y = (prev_y**2) * dx - prev_x * dx - 2 * dx + prev_y
    y1.append(delta_y)
    prev_y = delta_y
    prev_x = i

#print(len(y1))
plt.plot(x1, y1, color="g")

x2 = np.arange(0, -4, -0.1)
y2 = []
print(x2)

prev_x = 0
prev_y = 0
y2.append(prev_y)

dx = -0.1

for i in x2[1:]:
    delta_y = (prev_y**2) * dx - prev_x * dx - 2 * dx + prev_y
    y2.append(delta_y)
    prev_y = delta_y
    prev_x = i

plt.plot(x2, y2, color="g")

plt.xlim([-6, 6])
plt.ylim([-3, 3])
###2

###3
x1 = np.arange(0, 4, 0.1)
y1 = []
#print(x1)

prev_x = 0
prev_y = 1
y1.append(prev_y)

dx = 0.1

for i in x1[1:]:
    delta_y = (prev_y**2) * dx - prev_x * dx - 2 * dx + prev_y
    y1.append(delta_y)
    prev_y = delta_y
    prev_x = i

#print(len(y1))
plt.plot(x1, y1, color="r")

x2 = np.arange(0, -4, -0.1)
y2 = []
print(x2)

prev_x = 0
prev_y = 1
y2.append(prev_y)

dx = -0.1

for i in x2[1:]:
    delta_y = (prev_y**2) * dx - prev_x * dx - 2 * dx + prev_y
    y2.append(delta_y)
    prev_y = delta_y
    prev_x = i

plt.plot(x2, y2, color="r")

plt.xlim([-6, 6])
plt.ylim([-3, 3])
###3

task6()
plt.show()