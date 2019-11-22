x=int(input("Enter purchase amount"))

a=input("Enter cloth type mill or handloom:")


if x<=1000:
    if a=='mill':

          bill=x
    else:
        bill=x-(x*5)/100
    
elif 1000<x<=2000:
    if a=='mill':

          bill=x-(x*5)/100
    else:
        bill=x-(x*7.5)/100
elif 2000<x<3000:
    if a=='mill':

          bill=x-(x*7.5)/100
    else:
        bill=x-(x*10)/100
else:
    if a=='mill':

          bill=x-(x*10)/100
    else:
        bill=x-(x*15)/100

print("Net amount =",bill)

print("Name: Faizan Shaikh Id: 17103455")
