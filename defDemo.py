def square_sum(a, b):
	return a**2 + b**2

print square_sum(3,4)

def change_list(b):
	b[0] = b[0] + 1
	return b

b = [1,2,3]

print change_list(b)
print b
