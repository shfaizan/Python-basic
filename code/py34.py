Basic_Salary =int(input("enter salary:"))

if Basic_Salary<10000:
    bon=(Basic_Salary/100)*10
    B_Sal= Basic_Salary + bon + 500
elif Basic_Salary>10000 and Basic_Salary<15000:
    bon=(Basic_Salary/100)*8
    B_Sal= Basic_Salary + bon + 300
elif Basic_Salary>15000 and Basic_Salary<25000:
    bon=(Basic_Salary/100)*6
    B_Sal= Basic_Salary + bon + 250
else:
    bon=(Basic_Salary/100)*12
    B_Sal= Basic_Salary + bon

print("--------------------------------------------------------")
print("Basic_Salary:",Basic_Salary)
print("Total Salary:",B_Sal)
print("--------------------------------------------------------")

print("Name: Faizan Shaikh Id: 17103455")
