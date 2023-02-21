"""
https://www.eolymp.com/uk/submissions/12977046
"""

def get_the_biggest(n):
    num = bin(n)[2:]
    check = []
    for i in range(len(bin(n)[2:])):
        first = num[0]
        res = num[1:] + first
        num = res
        check.append(int(res, 2))
    return max(check)


if __name__ == "__main__":
    n = int(input())
    res = get_the_biggest(n)
    print(res)