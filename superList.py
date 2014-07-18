class superList(list):
	def __sub__(self, b):
		a = self[:]
#		b = b[:]
		while len(b) > 0:
			element_b = b.pop()
			if element_b in a:
				a.remove(element_b)
		return a
a = superList([1,2,3])
print a - superList([3,4])
print a
