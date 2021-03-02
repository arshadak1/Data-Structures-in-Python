
class Deque:
    ''' Double ended Queues '''
    DEFAULT_CAPACITY = 10  # moderate capacity for all new Queues

    def __init__(self):
        self._data = [None] * Deque.DEFAULT_CAPACITY
        self._front = 0
        self._size = 0

    def __len__(self):
        ''' Return the number of elements in the Deque. '''
        return self._size

    def is_empty(self):
        ''' Return True if Deque is empty. '''
        return self._size == 0

    def first(self):
        '''
        Return (but do not remove) the element at the front of the Deque.
        Raise exception if the queue is empty.
        '''
        if self.is_empty():
            raise Exception('Deque is empty')
        return self._data[self._front]

    def last(self):
        '''
        Return (but do not remove) the element at the back of the Deque.
        Raise exception if the queue is empty.
        '''
        if self.is_empty():
            raise Exception('Deque is empty')
        back = (self._front + self._size - 1) % len(self._data)
        return self._data[back]

    def _resize(self, cap):  # we assume cap >= len(self)
        ''' Resize to a new list of capacity >= len(self). '''
        old_data = self._data  # keep a track of existing list
        self._data = [None] * cap  # allocate list with new capacity
        order = self._front
        for i in range(self._size):  # only consider existing elements
            self._data[i] = old_data[order]
            order = (order - 1) % len(old_data)
        self._front = 0  # front has been realigned

    def add_first(self, e):
        ''' Add element e to the front of deque. '''
        if self._size == len(self._data):
            self._resize(2 * self._size)  # double the array
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size += 1

    def add_last(self, e):
        ''' Add element e to the back of deque. '''
        if self._size == len(self._data):
            self._resize(2 * self._size)  # double the array
        back = (self._front + self._size) % len(self._data)
        self._data[back] = e
        self._size += 1

    def delete_first(self):
        '''
        Remove and return the first element in the deque.
        Raise exception if deque is empty.
        '''
        if self.is_empty():
            raise Exception('Deque is empty')
        answer_first = self._data[self._front]
        self._data[self._front] = None  # helps garbbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:  # shrinking of the array
            self._resize(len(self._data) // 2)
        return answer_first

    def delete_last(self):
        '''
        Remove and return the last element in the deque.
        Raise exception if deque is empty.
        '''
        if self.is_empty():
            raise Exception('Deque is empty')
        back = (self._front + self._size - 1) % len(self._data)
        answer_last = self._data[back]
        self._data[back] = None  # helps garbbage collection
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:  # shrinking of the array
            self._resize(len(self._data) // 2)
        return answer_last

    def display(self):
        return self._data
        