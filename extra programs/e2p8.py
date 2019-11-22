print("17103455")
print("Faizan Shaikh", end='\n\n')

li = [['b', 80], ['a', 80], ['c', 70], ['d', 90]]
max = 0
smax = 0
for i in range(len(li)):
	if li[max][1] < li[i][1]:
		smax = max
		max = i
	if li[smax][1] < li[i][1] and li[i][1] != li[max][1]:
		smax = i

li2 = []
for i in range(len(li)):
	if li[i][1] == li[smax][1]:
		li2.append(li[i][0])		

print(sorted(li2))
