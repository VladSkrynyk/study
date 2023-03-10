def f(n):                      # O(n)
    sum = 0                    # O(1)
    for i in range(1, n + 1):  # O(n)
        sum = sum + i          # O(n)
    return sum                 # O(1)

def f1(n):                      # O(1)
    return n * (1 + n) / 2      # O(1)

# результатом виконання наведоної функції для заданого натурального числа n буде сума чисел від 1 до n
# арифметична прогресія