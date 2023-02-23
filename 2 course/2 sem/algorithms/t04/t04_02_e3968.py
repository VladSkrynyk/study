"""
https://www.eolymp.com/uk/submissions/13006589
"""

def f(x):
    return x**2 + x**(0.5)
def solve():
    c = float(input())

    eps = 0.0000001
    left = 0.0
    right = 100000.0
    while abs(left - right) > eps:
        mid = (right + left) / 2.0
        if f(mid) <= c:
            left = mid
        else:
            right = mid

    print(float("%.9f" % right))

solve()

