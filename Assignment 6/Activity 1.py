# This program asks the user for amount of hours,
# Calculates the useres weekly, monthly, and annual pay,
# and displats the results.
#
# References:
# https://harpercollege.pressbooks.pub/programmingfundamentals/chapter/python-examples-3/

def get_hours():
  print("Enter amount hours worked:")
  hours = float(input())
  return hours
                
def get_rate():
  print("Enter rate per hr:")
  rate = float(input())
  return rate
               
def calculate_weekly(rate, hours):
  weekly = (rate * hours)
  return weekly
               
def calculate_monthly(weekly):
  monthly = (Weekly * 52 / 12)
  return annual

def calculate_annual(weekly):
  annual = (weekly * 52)
  return annual
               
def display_result(weekly, monthly, annual):
	print(str("Weekly income is " & weekly))
	print(str("Monthly income is " & monthly))
	print(str("Annual income is " & annual))
 
def main():
	hours = get_hours()
	rate = get_rate()
	display_result(weekly, monthly, annual)
	
	main()
