def f(n):                      # O(n)
    sum = 0                    # O(1)
    for i in range(1, n + 1):  # O(n)
        sum = sum + i          # O(n)
    return sum                 # O(1)

def g(n):                      # O(n^2)
    sum = 0                    # O(1)
    for i in range(1, n + 1):  # O(n)
        sum = sum + i + f(i)   # O(n^2)
    return sum                 # O(1)

def g1(n):                                            # O(1)
    return 5 * n**3 / 6 - 5 * n**2 + 109 * n / 6 - 16 # 0(1)

# результатом виконання наведоної функції для заданого натурального числа n буде сума чисел від 1 до n
# арифметичних прогресія від 1 до n, і відповідні числа від 1 до n

