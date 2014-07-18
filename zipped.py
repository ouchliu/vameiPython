ta = [1,2,3]
tb = [4,4,6]

zipped = zip(ta, tb)
print(zipped)

na, nb=zip(*zipped)
print(na, nb)
