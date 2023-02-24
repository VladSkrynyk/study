
def find_res(li_len, mid):
    count = 0
    for i in li_len:
        count += i // mid
        #print(count)
    return count

def solve():
    n, m = map(int, input().split())
    li_len = []
    for i in range(n):
        li = int(input())
        li_len.append(li)

    left = 0
    right = 100_000
    mid = (left + right) // 2
    while (right - left) > 1:

        if find_res(li_len, mid) < m:
            right = mid
        else:
            left = mid
        mid = (left + right) // 2
    print(left)

solve()