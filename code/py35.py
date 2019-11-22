Customer_No= int(input("Enter Customer no:"))
Customer_Name =input("Enter Customer name:")
current_meter_reading = int(input("enter current meter reading:"))
Past_meter_reading = int(input("enter past meter reading:"))

Unit_Consumed = current_meter_reading - Past_meter_reading

if Unit_Consumed<200:
    bill=Unit_Consumed*2.5
    
elif Unit_Consumed>201 and Unit_Consumed<400:
    bill=Unit_Consumed*3
    T_bill= bill + 500
elif Unit_Consumed>401 and Unit_Consumed<600:
    bill=Unit_Consumed*5
    T_bill= bill + 1100
else:
    bill=Unit_Consumed*8.5
    T_bill= bill + 2100

print("--------------------------------------------------------")
print("Customer No :",Customer_No)
print("Customer Name:",Customer_Name)
print("Past Reading:" ,Past_meter_reading)
print("Current Reading:" ,current_meter_reading)
print("Units Consumed:", Unit_Consumed)
print("Total bill is ",T_bill)
print("--------------------------------------------------------")

print("Name: Faizan Shaikh Id: 17103455")
