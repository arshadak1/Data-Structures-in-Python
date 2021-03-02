
class Queue:
    ''' FIFO queue implementation using a Python list as underlying storage. '''
    DEFAULT_CAPACITY = 10  # moderate capacity for all new Queues

    def __init__(self):
        ''' Create an empty Queue. '''
        self._data = [None] * Queue.DEFAULT_CAPACITY
        self._size = 0  # represents current number of elements in Queue
        self._front = 0  # represents the index within data of the ﬁrst element of the queue

    def __len__(self):
        ''' Return the number of element in the Queue. '''
        return self._size

    def is_empty(self):
        ''' Return True if Queue is empty. '''
        return self._size == 0

    def first(self):
        '''
        Return (but do not remove) the element at the front of the queue.
        Raise exception if the queue is empty.
        '''
        if self.is_empty():
            raise Exception('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        '''
        Remove and return the ﬁrst element of the queue (i.e., FIFO).
        Raise exception if the queue is empty.
        '''
        if self.is_empty():
            raise Exception('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None  # helps garbbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:  # shrinking of the array
            self._resize(len(self._data) // 2)
        return answer

    def _resize(self, cap):  # we assume cap >= len(self)
        ''' Resize to a new list of capacity >= len(self). '''
        old_data = self._data  # keep a track of existing list
        self._data = [None] * cap  # allocate list with new capacity
        order = self._front
        for i in range(self._size):  # only consider existing elements
            self._data[i] = old_data[order]
            order = (order + 1) % len(old_data)
        self._front = 0  # front has been realigned

    def enqueue(self, e):
        ''' Add an element to the back of queue. '''
        if self._size == len(self._data):
            self._resize(2 * self._size)  # double the array size

        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1
