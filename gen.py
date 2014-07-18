def gen():
	a = 100
	yield a
	a = a * 9
	yield a
	yield 10000

for i in gen():
	print i

def gen2():
	for i in range(4):
		yield i

for i in gen2():
	print i
