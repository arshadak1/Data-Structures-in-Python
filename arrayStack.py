
class Stack:

    ''' LIFO Stack implementation using a Python list as underlying storage. '''

    def __init__(self):
        ''' create an empty Stack '''
        self._data = []                  # non-public list instance

    def __len__(self):
        ''' return the number of element in Stack. '''
        return len(self._data)

    def is_empty(self):
        ''' return True if Stack is empty. '''
        return len(self._data) == 0

    def push(self, e):
        ''' add element e to the top of the Stack. '''
        self._data.append(e)             # nem item stored at end of the list

    def pop(self):
        ''' Remove and return the top element in the Stack.
            Raise exception if the stack is empty.'''
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._data.pop()			 # remove last item from the list

    def top(self):
        ''' Return (but do not remove) the element at the top of the stack.
                Raise exception if the stack is empty. '''
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._data[-1]			 # the last item in the list
