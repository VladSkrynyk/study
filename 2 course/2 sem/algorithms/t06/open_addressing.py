import math

size = 11
keys = []
values = []
count = 0

def is_prime(n):
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def _hask(key: int) -> int:
    return key % size

def rehash():
    global size
    _size = size
    _keys = keys
    _values = values

    size = 2 * size + 1
    while not is_prime(size):
        size += 2

    init()
    for i in range(_size):
        if _keys[i] is not None:
            set(_keys[i], _values[i])


def init():
    global count, keys, values
    count = 0
    keys = [None for _ in range(size)]
    values = [None for _ in range(size)]

def set(key: int, value: str) -> None:
    global count

    if count / size > 0.7:
        rehash()

    curr = _hask(key)
    while keys[curr] is not None:
        if keys[curr] == key:
            values[curr] = value
            return
        curr = (curr + 1) % size

    keys[curr] = key
    values[curr] = value
    count += 1
    print(count, size)

def get(key: int):
    curr = _hask(key)
    while keys[curr] is not None:
        if keys[curr] == key:
            return values[curr]
        curr = (curr + 1) % size
    return None


def delete(key: int) -> None:
    global count

    curr = _hask(key)
    items = []
    while keys[curr] is not None:
        #print(curr)
        if keys[curr] != key:
            items.append((keys[curr], values[curr]))
        else:
            count -= 1
        keys[curr] = None
        values[curr] = None
        curr = (curr + 1) % size

    #print(items)
    for k, v in items:
        set(k, v)

init()
set(3, "3")
print(keys)
print(values)
set(4, "4")
print(keys)
print(values)
set(14, "14")
print(keys)
print(values)
#set(10, "10")
#print(keys)
#print(values)
#set(21, "21")
#print(keys)
#print(values)
#print(get(25))
#delete(3)
#print(keys)

#for i in range(20):
#    set(i, f"{i}")







