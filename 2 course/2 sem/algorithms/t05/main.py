"""
https://www.eolymp.com/uk/submissions/13026392
"""


def count(li_len, mid):
    count = 0
    for li in li_len:
        count += li // mid
    return count

def solve():
    n, m = map(int, input().split())
    li_len = []

    for i in range(n):
        li = int(input())
        li_len.append(li)

    left = 0
    right = max(li_len) + 100
    mid = (left + right) // 2
    while (right - left) > 1:
        cnt = count(li_len, mid)
        #print(left, right, mid, cnt)
        if cnt < m:
            right = mid
        else:
            left = mid
        mid = (left + right) // 2
    return left

print(solve())