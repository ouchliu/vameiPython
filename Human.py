class Human(object):
	age = 0
	def __init__(self, inputGender):
		self.gender = inputGender
	def printGender(self):
		print self.gender
lilei = Human('Male')
print lilei.gender
lilei.printGender()
