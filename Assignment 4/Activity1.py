# This program calculates the rate per hour, weekly, monthly, & annual pay

print("Enter hours worked:")
hours = float(input())

print("Enter rate per hr:")
rate = float(input())

weekly = (hours * rate)

monthly = (weekly * 52) / 12

annual = (weekly * 52)

print("Weekly income is" + str(weekly))
print("Monthly income is" + str(monthly))
print("Annual income is" + str(annual))
