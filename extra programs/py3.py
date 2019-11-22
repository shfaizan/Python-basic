import math 
def Series( x , n ): 
	sum = 1
	term = 1
	y = 2
	
	
	for i in range(1,n): 
		fct = 1
		for j in range(1,y+1): 
			fct = fct * j 
		
		term = term * (-1) 
		m = term * math.pow(x, y) / fct 
		sum = sum + m 
		y += 2
	
	return sum

 
x = int(input("enter x:"))
n = int(input("enter n:"))
print('%.4f'% Series(x, n)) 
print("Faizan Shaikh")
print(17103455)
 
