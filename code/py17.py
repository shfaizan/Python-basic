'''
Write a program to calculate bill amount for lorry driver.
Input lorry number, distance travelled in kms, rate per kms and number of days of journey.
For each day driver will be given Rs. 750 for his own expense.
Print lorry number, distance in kms, rate per kms.
Number of days of journey and bill amount
'''

lorry_number = int(input("enter lorry number:"))
distance_travelled = int(input("distance travelled in kms:"))
rate_per_kms= 12
driver_daily_salary= 750
total_bill = (distance_travelled * rate_per_kms ) + driver_daily_salary

print("toatal bill" ,total_bill)

print("Name: Faizan Shaikh Id: 17103455")
