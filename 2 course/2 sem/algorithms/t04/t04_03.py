def f(x):
    return x**3 + x + 1

def solve():
    left = 0.0
    right = 10.0
    m = (left + right) / 2.0
    while left != m and m != right:
        if f(m) < 5:
            left = m
        else:
            right = m
        m = (left + right) / 2.0
    return right

print(solve())
