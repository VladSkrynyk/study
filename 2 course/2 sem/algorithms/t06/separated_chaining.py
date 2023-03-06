size = 13
items = []

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

def _hask(key: int) -> int:
    return key % size

def init():
    global items
    items = [None for _ in range(size)]

def set(key: int, value: str) -> None:
    curr = _hask(key)
    node = items[curr]
    while node is not None:
        if node.key == key:
            node.value = value
            return
        node = node.next

    node = Node(key, value)
    node.next = items[curr]
    items[curr] = node

def get(key: int):
    curr = _hask(key)
    node = items[curr]
    while node is not None:
        if node.key == key:
            return node.value
        node = node.next
    return None

def delete(key: int) -> None:
    curr = _hask(key)
    node = items[curr]
    if node is not None:
        if node.key == key:
            items[curr] = node.next
            return

        prev = node
        node = node.next
        while node is not None:
            if node.key == key:
                prev.next = node.next
                return
            prev = node
            node = node.next

init()
set(2, "2")
print(items[2].value)
set(15, "15")
print(items[2].value, items[2].next.value)
set(28, "28")
print(items[2].value, items[2].next.value, items[2].next.next.value)
#print(get(2))
delete(15)
print((items[2].key))
print(items[2].key, items[2].next.key)

