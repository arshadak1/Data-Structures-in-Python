
class _Node:
    """ Non-public, lightweight Class for creating nodes. """
    __slots__ = '_data', '_next'      # streamline memory usage

    def __init__(self, data=None):
        self._data = data  # data or value of the node
        self._next = None  # reference to the next node


class LinkedList:

    def __init__(self):
        self._head = _Node()
        self._size = 0      # to keep a track of length of linked list

    def __len__(self):
        """ Return the number of elements in the linked list. """
        return self._size

    def __getitem__(self, index):
        """ Return the item at index. """
        if self._size == 0:
            raise Exception('IndexError: pop from an empty linked list')
        elif index >= self._size or abs(index) > self._size:
            raise Exception('IndexError: Index is out of range')

        if index < 0:
            index += self._size
        node = self._head
        ind = 0
        while True:
            node = node._next
            if ind == index:
                return node._data
            ind += 1

    def __setitem__(self, index, value):
        if index >= self._size or abs(index) > self._size:
            raise Exception('IndexError: Index is out of range')
        elif self._size == 0:
            raise Exception('IndexError: pop from an empty linked list')
        if index < 0:
            index += self._size
        ind = 0
        node = self._head
        while True:
            node = node._next
            if ind == index:
                node._data = value
                return
            ind += 1

    def append(self, element):
        """ To add new element in the link. """
        new_node = _Node(element)
        node = self._head
        while node._next is not None:
            node = node._next
        node._next = new_node
        self._size += 1

    def remove(self, value):
        """ Remove the first occurrence of the value.
            Raises ValueError if the value is not present. """
        node = self._head
        while True:
            last_node = node
            node = node._next
            if node._data == value:
                last_node._next = node._next
                self._size -= 1
                return
            elif node is None:
                raise Exception(
                    'ValueError: sLinkedList.remove(x): x is not in the linked list')

    def pop(self, index=-1):
        """ Return and Remove item at index (default last).
            Raises IndexError if list is empty or index is out of range. """
        if index >= self._size or abs(index) > self._size:
            raise Exception('IndexError: Index is out of range')
        elif self._size == 0:
            raise Exception('IndexError: pop from an empty linked list')
        if index < 0:
            index += self._size
        ind = 0
        node = self._head
        while True:
            last_node = node
            node = node._next
            if ind == index:
                last_node._next = node._next
                self._size -= 1
                return node._data
            ind += 1

    def count(self, value):
        """ Return the number of occurrences of the value"""
        count = 0
        node = self._head
        while node._next is not None:
            if node._next._data == value:
                count += 1
            node = node._next
        return count

    def clear(self):
        """ Remove all nodes. """
        self._head = _Node()
        self._size = 0

    def display(self):
        node = self._head
        c = []
        while node._next is not None:
            c.append(node._next._data)
            node = node._next
        return c
