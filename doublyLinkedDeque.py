	
class _DoublyLinkedList:

	class _Node:
		__slots__ = '_element', '_prev', '_next'
		def __init__(self, element, prev, next):
			self._element = element
			self._prev = prev
			self._next = next

	def __init__(self):
		self.header = self._Node(None, None, None)
		self.trailer = self._Node(None, None, None)		
		self.header._next = self.trailer
		self.trailer._prev = self.header
		self.size = 0

	def __len__(self):
		return self.size

	def is_empty(self):
		return self.size == 0

	def _insert_between(self, value, predecessor, successor):
		new_node = self._Node(value, predecessor, successor)
		successor._prev = new_node
		predecessor._next = new_node
		self.size += 1

	def _delete_node(self, node):
		previous = node._prev
		successor = node._next
		element = node._element
		node._next = node._element = node._prev = None
		previous._next = successor
		successor._prev = previous
		self.size -= 1
		return element


class LinkedDeque(_DoublyLinkedList):

	def first(self):
		if self.is_empty():
			raise Exception('Deque is empty')
		return self.header._next._element

	def last(self):
		if self.is_empty():
			raise Exception('Deque is empty')
		return self.trailer._prev._element		 

	def add_first(self, value):
		self._insert_between(value, self.header, self.header._next) 

	def add_last(self, value):
		self._insert_between(value, self.trailer._prev, self.trailer)		

	def delete_first(self):
		if self.is_empty():
			raise Exception('Deque is empty')
		return self._delete_node(self.header._next)

	def delete_last(self):
		if self.is_empty():
			raise Exception('Deque is empty')
		return self._delete_node(self.trailer._prev)

	def display(self):
		cur = self.header
		while cur._next != self.trailer:
			cur = cur._next
			print(cur._element, end=" --> ")
