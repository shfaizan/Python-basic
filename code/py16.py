'''
Write a program to calculate the amount to be paid by customer for electric bill, where
unit consumed = current meter reading – Past meter reading &Total bill = Unit Consumed * Charges per unit
Output should be,
Electricity Bill
————————————————————
Customer No.              : ****
Customer Name          : ***********************
Past Reading               : *******
Current Reading          : *******
Units Consumed          : *******
Charge per Unit           : *******
Past Reading               : *******
Billed Amount             : ********.**
————————————————————–
'''
Charges_per_unit = 5
current_meter_reading = int(input("enter current meter reading:"))
Past_meter_reading = int(input("enter past meter reading:"))

Unit_Consumed = current_meter_reading - Past_meter_reading

Total_bill = Unit_Consumed * Charges_per_unit

print("Customer No : 2343")
print("Customer Name: xyz")
print("Past Reading:" ,Past_meter_reading)
print("Current Reading:" ,current_meter_reading)
print("Units Consumed:", Unit_Consumed)
print("Charge per Unit:" ,Charges_per_unit)
print("Past Reading:" ,Past_meter_reading)
print("Total bill", Total_bill)


print("ID: 17103455 Name: Faizan Shaikh")
