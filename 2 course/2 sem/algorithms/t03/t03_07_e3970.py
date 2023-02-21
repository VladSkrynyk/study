"""
https://www.eolymp.com/uk/submissions/12985522
"""

def bsearch_leftmost(array, x):
    left = 0
    right = len(array)
    while left < right:
        mid = left +(right - left) // 2
        if (x > array[mid]):
            left = mid + 1
        else:
            right = mid
    return left

def bsearch_rightmost(array, x):
    left = 0
    right = len(array)
    while left < right:
        m = left + (right - left) // 2
        if (array[m] <= x):
            left = m + 1
        else:
            right = m
    return left - 1

if __name__ == "__main__":
    with open("input.txt") as f:
        line = f.readline().strip()
        while line:
            n = int(line)
            array1 = list(map(int, f.readline().split()))
            a = f.readline().strip()
            array2 = list(map(int, f.readline().split()))
            for i in array2:
                left = bsearch_leftmost(array1, i)
                right = bsearch_rightmost(array1, i)
                print(right - left + 1)    
            line = f.readline().strip()

    