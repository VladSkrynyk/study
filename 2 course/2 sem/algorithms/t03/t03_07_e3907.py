"""

"""

def bsearch_leftmost(array, x):
    left = 0
    right = len(array)
    while left < right:
        mid = left + (right - left) // 2
        if x > array[mid]:
            left = mid + 1
        else:
            right = mid
    return left

def bsearch_rightmost(array, x):
    left = 0
    right = len(array)
    while left < right:
        m = left + (right - left) // 2
        if array[m] <= x:
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
            #array2 = [1, 16, 17, 22]
            #print(n, array1, a, array2)
            for i in array2:
                left = bsearch_leftmost(array1, i)
                right = bsearch_rightmost(array1, i)
                #print(i, left, right, array1[right])
                #if i == array1[right]:
                #    print(right - left + 1)
                #else:
                #    print(0)
                c = 0
                for j in array2:
                    if i == j:
                        c+=1
                if c == 0:
                    print(0)
                else:
                    print(right - left + 1)
            line = f.readline().strip()