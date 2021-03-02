class _Node:

	def __init__(self, data):
		self.data = data
		self.next = None


class CircularlyLinkedQueue:

	def __init__(self):
		self.tail = None
		self.size = 0

	def __len__(self):
		return self.size

	def is_empty(self):
		return self.size == 0

	def enqueue(self, value):
		new_node = _Node(value)
		if self.is_empty():
			new_node.next = new_node
		else:
			new_node.next = self.tail.next
			self.tail.next = new_node
		self.tail = new_node
		self.size += 1

	def dequeue(self):
		if self.is_empty():
			raise Exception('Queue is empty')
		answer = self.tail.next
		if self.size == 0:
			self.tail = None
		else:
			self.tail.next = answer.next  
		self.size -= 1
		return answer.data

	def first(self):
		return self.tail.next.data

	def rotate(self):
		if not self.is_empty():
			self.tail = self.tail.next
