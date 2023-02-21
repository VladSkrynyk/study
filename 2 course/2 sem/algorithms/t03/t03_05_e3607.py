"""
https://www.eolymp.com/uk/submissions/12977189
"""

if __name__ == "__main__":
    with open("input.txt") as f:
        line = f.readline().strip()
        while line:
            n = int(line)
            array = list(map(int, f.readline().split()))
            a, b = [int(s) for s in f.readline().split()]
            # print(n, array, a, b)
            count = 0
            for i in array:
                if a <= i <= b:
                    count += 1
            print(count)
            line = f.readline().strip()