""" FIFO Queue implementation using linked list. """


class _Node:
    """ Lightweight, non-public Class for creating nodes. """

    def __init__(self, element=None):
        self._element = element
        self._next = None


class LinkedQueue:

    def __init__(self):
        self.__head = _Node()
        self.__tail = None
        self.__size = 0

    def __len__(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def enqueue(self, e):
        new_node = _Node(e)
        if self.is_empty():
            self.__head = new_node
        else:
            self.__tail._next = new_node
        self.__tail = new_node
        self.__size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        node = self.__head
        answer = node._element
        self.__size -= 1
        self.__head = node._next
        if self.is_empty():
            self.__tail = None
        return answer

    def first(self):
        return self.__head._element
