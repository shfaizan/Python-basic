Drug_No= int(input("Enter drug no:"))
Drug_Name =input("Enter drug name:")
Unit_purchased = int(input("enter unit purchased:"))
rate_per_unit = int(input("enter rate per unit:"))
Drug_type = input("enter Drug type(I or B or T):")

bill=Unit_purchased*rate_per_unit

if Drug_type == 'I':
    dis=(bill/100)*7.5
    Tbill=bill-dis
if Drug_type == 'B':
    dis=(bill/100)*5
    Tbill=bill-dis
if Drug_type == 'T':
    dis=(bill/100)*2.5
    Tbill=bill-dis

print("--------------------------------------------------------")
print("Drug No :",Drug_No)
print("Drug Name:",Drug_Name)
print("Unit purchased:" ,Unit_purchased)
print("Rate per unit:" ,rate_per_unit)
print("Total bill ", bill)
print("Total bill after discount", Tbill)
print("--------------------------------------------------------")

print("Name: Faizan Shaikh Id: 17103455")
