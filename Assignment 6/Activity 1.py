# This program asks the user for amount of hours,
# Calculates the useres weekly, monthly, and annual pay,
# and displats the results.
#
# References:
# https://harpercollege.pressbooks.pub/programmingfundamentals/chapter/python-examples-3/

def get_hours():
    print("Enter amount of hours worked:")
    hours = float(input())
    return hours
        
        
def get_rate():
    print("Enter rate per hour:")
    rate = float(input())
    return rate
         
         
def calculate_weekly(rate, hours):
    weekly = (rate * hours)
    return weekly
         
def calculate_monthly(weekly):
    monthly = (weekly * 52 / 12)
    return monthly
        
        
def calculate_annual(weekly):
    annual = (weekly * 52)
    return annual
         
         
def display_result(weekly, monthly, annual):
    print("Weekly income is " + str(weekly))
    print("Monthly income is " + str(monthly))
    print("Annual income is " + str(annual))
          
          
def main():
    hours = get_hours()
    rate = get_rate()
    weekly = calculate_weekly(hours, rate)
    monthly = calculate_monthly(weekly)
    annual = calculate_annual(weekly)
    display_result(weekly, monthly, annual)
           
main()
