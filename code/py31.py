Regular_Charges = 6.5
industry_charge = 10
current_meter_reading = int(input("enter current meter reading:"))
Past_meter_reading = int(input("enter past meter reading:"))
customer_type = input("enter customer type(R or I):")

Unit_Consumed = current_meter_reading - Past_meter_reading
if customer_type == 'R':
    bill=Unit_Consumed*Regular_Charges
if customer_type == 'I':
    bill=Unit_Consumed*industry_charge   

print("Customer No : 2343")
print("Customer Name: xyz")
print("Past Reading:" ,Past_meter_reading)
print("Current Reading:" ,current_meter_reading)
print("Units Consumed:", Unit_Consumed)
print("Charge per Unit:" ,Charges_per_unit)
print("Past Reading:" ,Past_meter_reading)
print("Total bill",bill)
print("Name: Faizan Shaikh Id: 17103455")
