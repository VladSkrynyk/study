
"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
"""
size = 100001
library = []

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

def _hash(strng):
    global size
    n = 13
    h = 0

    for l in range(len(strng)):
        h = n * h + ord(strng[l])
    return h % size

def init():
    """ Викликається 1 раз на початку виконання програми. """
    global library
    library = [None for _ in range(size)]


def addBook(author, title):
    """ Додає книгу до бібліотеки.
    :param author: Автор книги
    :param title: Назва книги
    """
    curr = _hash(author.lower())
    node = library[curr]
    while node is not None:
        if node.key == author.lower():
            node = Node(author.lower(), title)
            node.next = library[curr]
            library[curr] = node
            return
        node = node.next

    node = Node(author.lower(), title)
    node.next = library[curr]
    library[curr] = node


def find(author, title):
    """ Перевірає чи міститься задана книга у бібліотеці.
    :param author: Автор
    :param title: Назва книги
    :return: True, якщо книга міститься у бібліотеці та False у іншому разі.
    """
    author = author.lower()
    curr = _hash(author)
    node = library[curr]
    while node is not None:
        if node.key == author:
           if node.value == title:
                return True

           while node.next is not None:
                if node.next.value == title:
                    return True
                node = node.next
           return False
        node = node.next
    return False


def delete(author, title):
    """ Видаляє книгу з бібліотеки.
    :param author: Автор
    :param title: Назва книги
    """
    author = author.lower()
    curr = _hash(author)
    node = library[curr]
    if node is not None:
        if node.key == author and node.value == title:
            library[curr] = node.next
            return

        prev = node
        node = node.next
        while node is not None:
            if node.key == author and node.value == title:
                prev.next = node.next
                return
            prev = node
            node = node.next

def findByAuthor(author):
    """ Повертає список книг заданого автора.
    Якщо бібліотека не міститься книг заданого автора, то підпрограма повертає порожній список.
    :param author: Автор
    :return: Список книг заданого автора у алфавітному порядку.
   """
    author = author.lower()
    curr = _hash(author)
    node = library[curr]
    while node is not None:
        if node.key == author:
           books = []
           books.append(node.value)
           while node.next is not None:
                node = node.next
                books.append(node.value)
           books = sorted(books)
           return books
        node = node.next
    return []


#init()
#addBook("a", "1")
#addBook("a", "2")
#addBook("a", "3")
#addBook("a", "4")
#addBook("a", "5")

#delete("a", "1")
#delete("a", "3")
#print(findByAuthor("A"))
#delete("a", "1")
#print(find("a", "1"))
#print(findByAuthor("a"))
#print(library)
#print(library[6].value)
#print(library[6].next.value)
#print(library[6].next.next.value)
#print(library[6].next.next.next.value)

