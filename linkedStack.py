
# LIFO Stack implementation using linked list for storage

class _Node:
    """ Non-public, lightweight Class for creating nodes. """
    __slots__ = '_element', '_next'       # streamline memory usage

    def __init__(self, element, next):
        self._element = element
        self._next = next


class linkedStack:

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def push(self, e):
        self._head = _Node(e, self._head)
        self._size += 1

    def is_empty(self):
        return self._size == 0

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

    def top(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._head._element
