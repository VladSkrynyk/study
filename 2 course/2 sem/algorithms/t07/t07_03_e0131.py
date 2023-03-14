"""
https://www.eolymp.com/uk/submissions/13175631
"""

SIZE = 11
keys = []
values = []

def _hash(strng):
    global SIZE
    n = 13
    h = 0

    for l in range(len(strng)):
        h = n * h + ord(strng[l])
    return h % SIZE

def init():
    global keys, values, SIZE
    keys = [None for i in range(SIZE)]
    values = [None for i in range(SIZE)]

def addLetter(letter):
    global SIZE

    letter = letter.lower()
    cur = _hash(letter)
    while keys[cur] is not None:
        if  keys[cur] == letter:
            values[cur] += 1
            return
        cur = (1 + cur) % SIZE
    keys[cur] = letter
    values[cur] = 1

def getLetter(letter):
    global SIZE

    letter = letter.lower()
    cur = _hash(letter)
    while keys[cur] is not None:
        if keys[cur] == letter:
            return values[cur]
        cur = (cur + 1) % SIZE
    return 0

word = input()
n = int(input())

lib = []
for i in range(n):
    lib.append(input())

init()
count = 0
for letter in word:
    addLetter(letter)

for i in lib:
    uniq = list(set(i))
    check = True
    for j in uniq:
        if i.count(j) > getLetter(j):
            check = False
    if check:
        count += 1
print(count)