
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


class PositionalList(_DoublyLinkedList):

	class Position:

		def __init__(self, container, node):
			self._container = container
			self._node = node

		def element(self):
			return self._node._element

		def __eq__(self, other):
			return type(self) is type(other) and self._node is other._node

		def __ne__(self, other):
			return not (self == other)

	def _validate(self, p):
		if not isinstance(p, self.Position):
			raise TypeError
		if p._container is not self:
			raise ValueError
		if p._node._next is None:
			raise ValueError
		return p._node

	def _make_position(self, node):
		if node is self.header or node is self.trailer:
			return None
		else:
			return self.Position(self, node)

	def first(self):
		return self._make_position(self.header._next)

	def last(self):
		return self._make_position(self.trailer._prev)

	def before(self, p):
		node = self._validate(p)
		return self._make_position(node._prev)

	def after(self, p):
		node = self._validate(p)
		return self._make_position(node._next)

	def __iter__(self):
		cursor = self.first()
		while cursor is not None:
			yield cursor.element()
			cursor = self.after(cursor)

	def _insert_between(self, value, predecessor, successor):
		node = super()._insert_between(value, predecessor, successor)
		return self._make_position(node)

	def add_first(self, value):
		return self._insert_between(value, self.header, self.header._next)

	def add_last(self, value):
		return self._insert_between(value, self.trailer._prev, self.trailer)

	def add_before(self, p, value):
		original = self._validate(p)
		return self._insert_between(value, original._prev, original)

	def add_after(self, p, value):
		original = self._validate(p)
		return self._insert_between(value, original, original._next)

	def delete(self, p):
		original = self._validate(p)
		self._delete_node(original)

	def replace(self, p, value):
		original = self._validate(p)
		old_value = original._element
		original._element = value
		return old_value


def insertion_sort(L):
	""" Sort PositionalList of comparable elements into nondecreasing order. """
	if len(L) > 1:		# otherwise no need to sort
		marker = L.first()
		while marker != L.last():
			pivot = L.after(marker)
			value = pivot.element()
			if value > marker.element():
				marker = pivot
			else:
				walk = marker
				while walk != L.first() and L.before(walk).element() > value:
					walk = L.before(walk)
				L.delete(pivot)
				L.add_before(walk, value)
