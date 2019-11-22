a=int(input("Enter amount for transistor:"))
b=int(input("Enter capacitor:"))
c=int(input("enter resistor:"))
if a>1000:
    dis=(a/100)*10
    a=a-dis
if b>500:
    dis=(b/100)*5
    b=b-dis
if c>2000:
    dis=(c/100)*10
    c=c-dis
print("transistor discount is ",a)
print("capacitor discount is ",b)
print("rasistor discount is ",c) 
print("Name: Faizan Shaikh Id: 17103455")
