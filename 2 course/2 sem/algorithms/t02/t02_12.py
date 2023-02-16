def f(n):                      # O(n)
    sum = 0                    # O(1)
    for i in range(1, n + 1):  # O(n)
        sum = sum + i          # O(n)
    return sum                 # O(1)

def f1(n):                      # O(1)
    return n * (1 + n) / 2      # O(1)

def g(n):                      # O(n^2)
    sum = 0                    # O(1)
    for i in range(1, n + 1):  # O(n)
        sum = sum + i + f(i)   # O(n^2)
    return sum                 # O(1)

def g1(n):                                            # O(1)
    return 5 * n**3 / 6 - 5 * n**2 + 109 * n / 6 - 16 # 0(1)

def h(n):              # O(n^2)
    return f(n) + g(n) # O(n^2)

def h1(n):               # O(1)
    return f1(n) + g1(n) # O(1)

# результатом буде арифметична прогресія від заданого числа n, а також сума арифметичних прогресій від 1 до n
# додавши відповідні числа від 1 до n
