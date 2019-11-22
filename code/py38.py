l=int(input("Enter vlevel:"))
salary=int(input("Eneter salary"))
perks=input("Enter perks type 'C' or 'E'")
if l==1:
    if perks=='c':
        salary=salary+20000
        salary=salary+(salary*25)/100
        
    else:
        salary=salary+600
        salary=salary+(salary*25)/100
        
elif l==2:
    if perks=='c':
        salary=salary+7000
        salary=salary+(salary*25)/100
        
    else:
        salary=salary+400
        salary=salary+(salary*25)/100
    
elif l==3:
    if perks=='c':
        salary=salary+4000
        salary=salary+(salary*25)/100
    
    else:
        salary=salary+200
        salary=salary+(salary*25)/100
        
elif l==4:
    if perks=='c':
        salary=salary+1500
        salary=salary+(salary*25)/100
    
    else:
        salary=salary
        salary=salary+(salary*25)/100
        
else:
    print("level invailed")
if salary<=20000:
    salary=salary
elif 20000<salary<=40000:
    salary=salary-(salary*3)/100
elif 40000<salary<=50000:
    salary=salary-(salary*5)/100
else:
    salary=salary-(salary*8)/100
print("salary =",salary)

print("Name: Faizan Shaikh Id: 17103455")
