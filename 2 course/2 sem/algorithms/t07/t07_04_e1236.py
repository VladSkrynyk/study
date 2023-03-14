"""
https://www.eolymp.com/uk/submissions/13175631
"""

SIZE2 = 100001
keys2 = []
values2 = []

def _hash(strng):
    global SIZE2
    n = 13
    h = 0

    for l in range(len(strng)):
        h = n * h + ord(strng[l])
    return h % SIZE2

def init2():
    global keys2, values2, SIZE2
    keys2 = [None for i in range(SIZE2)]
    values2 = [None for i in range(SIZE2)]

def addLetter2(letter):
    global SIZE2

    letter = letter.lower()
    cur = _hash(letter)
    while keys2[cur] is not None:
        if  keys2[cur] == letter:
            values2[cur] += 1
            return
        cur = (1 + cur) % SIZE2
    keys2[cur] = letter
    values2[cur] = 1

def getLetter2(letter):
    global SIZE2

    letter = letter.lower()
    cur = _hash(letter)
    while keys2[cur] is not None:
        if keys2[cur] == letter:
            return values2[cur]
        cur = (cur + 1) % SIZE2
    return 0


def solve():
    n = int(input())
    lib = []
    for i in range(n):
        lib.append(input())

    text = input()

    for word in lib:
        init2()

        check1 = True
        for letter in word:
            addLetter2(letter)
            if letter not in text:
                check1 = False
                break
        if not check1:
            continue

        check = True
        for let in set(word):
            if getLetter2(let) > text.count(let):
                check = False
                break
        if not check:
            continue

        if check:
            text = text[::-1]
            print("YES", len(text) - text.index(word[-1]))
            return

    print("NO")
    return

solve()