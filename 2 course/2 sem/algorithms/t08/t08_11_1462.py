"""
https://www.eolymp.com/uk/submissions/13207257
"""

def sort(arr):
    n = len(arr)
    for pass_num in range(n - 1, 0, -1):
        _sorted = True
        for i in range(pass_num):
            if int(str(arr[i])[-1]) > int(str(arr[i + 1])[-1]):
                arr[i + 1], arr[i] = arr[i], arr[i + 1]
                _sorted = False
            elif int(str(arr[i])[-1]) == int(str(arr[i + 1])[-1]):
                if arr[i] > arr[i + 1]:
                    arr[i + 1], arr[i] = arr[i], arr[i + 1]
                    _sorted = False

        if _sorted:
            return

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

sort(arr)
print(*arr)