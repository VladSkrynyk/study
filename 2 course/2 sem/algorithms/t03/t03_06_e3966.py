"""
https://www.eolymp.com/uk/submissions/12977813
"""

if __name__ == "__main__":
    with open("input.txt") as f:
        line = f.readline().strip()
        while line:
            n = int(line)
            array1 = list(map(int, f.readline().split()))
            a = f.readline().strip()
            array2 = list(map(int, f.readline().split()))
            for i in array2:
                left = 0
                right = n - 1
                while left <= right:
                    mid = left + (right - left) // 2
                    if i > array1[mid]:
                        left = mid + 1
                    elif i < array1[mid]:
                        right = mid - 1
                    else:
                        print("YES")
                        break
                if i != array1[mid]:
                    print("NO")

            line = f.readline().strip()
