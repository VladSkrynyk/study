test = [1, 12, 34, 35, 56, 65, 65, 65, 77, 79, 81, 83, 88, 99, 101]
#print(len(test))

def linear_search(array, x):
    """ Лінійний пошук у масиві
     :param array: Список елементів
     :param x: Шуканий елемент
     :return: True, якщо шуканий елемент знайдено
     """
    for el in array:
        if el == x:
            return True
    return False

#print(linear_search(test, 65))
#print(linear_search(test, 45))

def binary_search(array, x):
    """ Бінарний пошук у масиві
     :param array: Список елементів
     :param x: Шуканий елемент
     :return: True, якщо шуканий елемент знайдено
    """
    left = 0
    right = len(array) - 1
    while left < right:
        mid = left + (right - left) // 2
        if x > array[mid]:
            left = mid + 1
        else:
            right = mid
    return array[right] == x

#print(binary_search(test, 34))


def binary_search(array, x):
    """ Бінарний пошук у масиві
    :param array: Список елементів
    :param x: Шуканий елемент
    :return: Індекс шуканого елементу
    """
    left = 0  # Індекс лівого елементу
    right = len(array) - 1  # Індекс правого елементу

    while left <= right:
        m = left + (right - left) // 2  # Середина відрізка
        if x > array[m]:
            left = m + 1
        elif x < array[m]:
            right = m - 1
        else:
            return m
    return None

def bsearch_leftmost(array, x):
    """ Бінарний пошук для відшукання найпершого входження заданого числа
    :param array: Відсортований за неспаданням масив цілих чисел
    :param x: Шукане число
    :return: Номер шуканого елемента у масиві
    """
    left = 0
    right = len(array)
    while left < right:
        mid = left + (right - left) // 2
        #print(f"l={left}; r={right}; mid={mid}")
        if x > array[mid]:
            left = mid + 1
        else:
            right = mid
    return left


def bsearch_rightmost(array, x):
    """ Бінарний пошук для відшукання останнього входження заданого числа
    :param array: Відсортований за неспаданням масив цілих чисел
    :param x: Шукане число
    :return: Номер шуканого елемента у масиві
    """
    left = 0 # ліва границя пошуку
    right = len(array) # права границя пошуку
    while left < right:
        m = left + (right - left) // 2 # Середина
        if array[m] <= x:
            left = m + 1
        else:
            right = m
    return left - 1

print(bsearch_rightmost(test, 130))