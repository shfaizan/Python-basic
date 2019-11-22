x=int(input("Enter basic amount"))

a=int(input("Enter working hour"))
salary=x
c=1

if x<=5000:
    while c<=11 or c<=a:
        
        salary=salary+50
        c+=1
    if c==11:
        while salary<=7500 and c<=21 and c<=a:
            salary=salary+75
            c+=1
    
elif 5000<x<10000:
    c=1
    while c<=10 and c<=a:
        salary=salary+75
        
        c+=1
        print(c)
    if c==11:
        
        while salary<=10000 and c<=21 and c<=a:
            salary=salary+100
            c+=1
else:
    c=1
    while c<=11 or c==a:
        
        salary=salary+100
        c+=1
    if c==11:
        while salary<15000 and c<=21 or c<=a:
            salary=salary+150
            c+=1

print("salary =",salary)

print("Name: Faizan Shaikh Id: 17103455")
