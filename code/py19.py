'''
Write a program to find year, month and days from given number of days.
Consider a month of 30 days and year of 365 days.
'''
day=int(input("Enter no of day:"))

year =day/365
t =day%365
month =t/30
days=t%30
print("year =",int(year))
print("month =",int(month))
print("days =",int(days))


print("Name: Faizan Shaikh Id: 17103455")
