Basic_Salary =int(input("enter salary:"))

if Basic_Salary<2000:
    bon=(Basic_Salary/100)*5
    B_Sal= Basic_Salary + bon
elif Basic_Salary>2000 and Basic_Salary<5000:
    bon=(Basic_Salary/100)*7
    B_Sal= Basic_Salary + bon
elif Basic_Salary>500 and Basic_Salary<7000:
    bon=(Basic_Salary/100)*9
    B_Sal= Basic_Salary + bon
else:
    bon=(Basic_Salary/100)*12
    B_Sal= Basic_Salary + bon

print("--------------------------------------------------------")
print("Basic_Salary:",Basic_Salary)
print("Salary after bonus:",B_Sal)
print("--------------------------------------------------------")

print("Name: Faizan Shaikh Id: 17103455")
