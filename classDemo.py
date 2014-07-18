class Bird(object):
	haveFeather = True
	wayOfreproduction = 'egg'
	position = [0,0]
	def move(self, dx, dy):
		self.position[0] += dx
		self.position[1] += dy
		return self.position
summer = Bird()
print 'after move:', summer.move(5, 8)

class Chicken(Bird):
	wayOfMove = 'walk'
	possibleInKFC = True

class Oriole(Bird):
	wayOfMove = 'fly'
	possibleInKFC = False
class happyBird(Bird):
	def __init__(self, more_words):
		print 'We are happy birds', more_words

summer = happyBird('h')
