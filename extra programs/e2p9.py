print("17103455")
print("Faizan Shaikh", end='\n\n')

li = [ 10, 20, 30, 40, {"a", "B", "c", "d"}, ['a', 12, 'b'], (42,24)]

c = 0

for i in range(len(li)):
	if (isinstance(li[i], tuple)):
		break
	else:
		c += 1

print("Elements encountered till tuple = ", c)
