class _Node:

    def __init__(self, data):
    	self.data = data
    	self.next = None

class CircularlyLinkedList:

	def __init__(self):
		self.tail = None
		self.size = 0

	def __len__(self):
		return self.size

	def append(self, value):
		new_node = _Node(value)
		if self.size == 0:
			new_node.next = new_node
		else:
			new_node.next = self.tail.next
			self.tail.next = new_node
		self.tail = new_node
		self.size += 1

	def sorted_insert(self, value):
		new_node = _Node(value)

		if self.size == 0:
			new_node.next = new_node
			self.tail = new_node
		else:
			cur = self.tail.next
			while cur.next.data < value:
				if cur == self.tail:
					new_node.next = self.tail.next
					self.tail.next = new_node
					self.tail = new_node
					self.size += 1
					return
				cur = cur.next
			value_next = cur.next
			new_node.next = value_next
			cur.next = new_node
		self.size += 1
	
	def display(self):
		cur = self.tail.next
		number = self.size
		while number > 0:
			print(cur.data) 
			cur = cur.next
			number -= 1