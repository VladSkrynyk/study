SIZE = 1000001
keys = []
values = []

def init():
    global keys, values, SIZE
    keys = [None for i in range(SIZE)]
    values = [None for i in range(SIZE)]

def _hash(strng):
    global SIZE
    n = 13
    h = 0

    for l in range(len(strng)):
        h = n * h + ord(strng[l])
    return h % SIZE


def addBook(author, title):
    global SIZE

    author = author.lower()
    cur = _hash(author)
    while keys[cur] is not None:
        if title not in values[cur] and keys[cur] == author:
            values[cur].append(title)
            return
        cur = (1 + cur) % SIZE
    keys[cur] = author
    values[cur] = [title]


def find(author, title):
    global SIZE

    author = author.lower()
    cur = _hash(author)
    while keys[cur] is not None:
        if (keys[cur] == author) and (title in values[cur]):
            return True
        cur = (cur + 1) % SIZE
    return False


def findByAuthor(author):
    global SIZE

    author = author.lower()
    cur = _hash(author)
    while keys[cur] is not None:
        if keys[cur] == author:
            return sorted(values[cur])

        cur = (cur + 1) % SIZE
    return []


def delete(author, title):
    global SIZE
    cur = _hash(author.lower())
    try:
        while keys[cur] is not None:
            if keys[cur] == author.lower():
                values[cur].remove(title)
            if len(values[cur]) == 0:
                values[cur] = None
                keys[cur] = None

            cur = (cur + 1) % SIZE
    except ValueError:
        pass


#init()
#print(keys)
#delete("a", "1")
#print(keys)


