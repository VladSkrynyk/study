#---------------a---------------
def a(n):                   # O(n)
    s = 0                   # O(1)
    for i in range(n + 1):  # O(n)
        s += i              # O(n)
    return s                # O(1)

#---------------b---------------
def b(n):                   # O(n)
    s = 0                   # O(1)
    for i in range(n + 1):  # O(n)
        s += i * i          # O(n)
    return s                # O(1)

#---------------c---------------
def c(n, a):                # O(n)
    s = 0                   # O(1)
    for i in range(n + 1):  # O(n)
        s += a ** i         # O(log(n))
    return s                # O(1)

#---------------d---------------
def d(n):                   # O(n^2)
    s = 0                   # O(1)
    for i in range(n + 1):  # O(n)
        s += i ** i         # O(n*n) => O(n^2)
    return s                # O(1)

#---------------e---------------
def e(n):                      # O(n)
    p = 1                      # O(1)
    for i in range(1, n + 1):  # O(n)
        p *= 1 / (1 + i)       # O(n)
    return p                   # O(1)

#---------------f---------------
def f(n):                           # O(n)
    p = 1                           # O(1)
    factorial_i = 1                 # O(1)
    for i in range(1, n + 1):       # O(n)
        factorial_i *= i            # O(n)
        p *= 1 / (1 + factorial_i)  # O(n)
    return p                        # O(1)

#---------------g---------------
def g(n, a):                            # O(n)
    p = 1                               # O(1)
    factorial_i = 1                     # O(1)
    exp = a                             # O(1)
    for i in range(1, n + 1):           # O(n)
        factorial_i *= i                # O(n)
        l = 1 + factorial_i             # O(n)
        p *= exp / l                    # O(n)
        exp *= a                        # O(n)
    return p                            # O(1)

#---------------h---------------
def h(n, m):                      # O(nm)
    p = 1                         # O(1)
    for i in range(1, n + 1):     # O(n)
        power_i = 1               # O(n)
        for j in range(1, m + 1): # O(nm)
            power_i *= i          # O(nm)
        p *= 1 / (1 + power_i)    # O(n)
    return p                      # O(1)

#---------------i---------------
def i(n):                          # O(n^2)
    p = 1                          # O(1)
    for i in range(1, n + 1):      # O(n)
        power_i = 1                # O(n)
        for j in range(1, i + 1):  # O(n^2)
            power_i *= i           # O(n^2)
        p *= 1 / (1 + power_i)     # O(n)
    return p                       # O(1)