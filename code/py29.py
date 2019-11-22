x=int(input("Enteer maths marks"))
y=int(input("Enter pysics marks"))
a=int(input("Enter chemistry marks"))
c=int(input("Enteer computer marks"))
d=int(input("Enter P.E markd"))
e=int(input("Enter S.S marks"))

per=(x+y+a+c+d+e)*100/600
if per>=60:
    print("First class ",per)
elif per>=48 and per<=60:
    print("Second class",per)
elif 40<=per<=48:
    print("Pass",per)
else:
    print("Fail ",per)

print("Name: Faizan Shaikh Id: 17103455")
