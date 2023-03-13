arr = [56, 12, 66, 20, 33, 95, 32, 13, 10]

def bubble_sort(arr):
    n = len(arr)
    for pass_num in range(n - 1, 0, -1):
        _sorted = True
        for i in range(pass_num):
            if arr[i] > arr[i + 1]:
                arr[i + 1], arr[i] = arr[i], arr[i + 1]
                _sorted = False

        if _sorted:
            return
        #print(arr)
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1, 0, -1):
        maxpos = 0
        for j in range(1, i + 1):
            if arr[maxpos] < arr[j]:
                maxpos = j
        arr[i], arr[maxpos] = arr[maxpos], arr[i]
    return arr

#print(bubble_sort(arr))
print(selection_sort(arr))
