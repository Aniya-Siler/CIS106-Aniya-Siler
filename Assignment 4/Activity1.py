# This program prompts user for hours worked and calculates the rate per hour, weekly, monthly, and annual (gross) pay

print("Enter hours worked:")
hours = float(input())

print("Enter rate per hr:")
rate = float(input())

weekly = (hours*rate)

monthly = (weekly*52) /12

annual = (weekly*52)

print("Weekly income is" + str(weekly)
print("Monthly income is" + str(monthly)
print("Annual income is" + str(annual)
      
# Refences I used were the Programming Fundamentals book (Data and Operations) I also used google to search up the specific calculations.
