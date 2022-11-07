# This program asks the user to enter their birthday and then displays the day of the week they were born
#Refrences:
# https://harpercollege.pressbooks.pub/programmingfundamentals/chapter/displaying-array-members/
# https://www.geeksforgeeks.org/zellers-congruence-find-day-date/

def get_year():
    print("What year were you born?")
    year = int(input())
    return year

def get_month():
    print("What month were you born?")
    month = int(input())
    return month

def get_day():
    print("What day were you born?")
    day = int(input())
    return day

def calculate_zellers_congruence(year,month,day):
    if (month == 1) :
        month = 13
        year = year - 1
 
    if (month == 2) :
        month = 14
        year = year - 1
    q = day
    m = month
    k = year % 100;
    j = year // 100;
    h = q + 13 * (m + 1) // 5 + k + k // 4 + j // 4 + 5 * j
    h = h % 7
    return h

def lookdayname(day_number):
    days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    day_name = days[day_number]
    return day_name
    
def display_results(day_name):
    print("Your day of birth landed on a " + str(day_name))
def main():
    year = get_year()
    print(year)
    month = get_month()
    print(month)
    day = get_day()
    print(day)
    zellers_congruence = calculate_zellers_congruence(year,month,day)
    print(zellers_congruence)
    day_name = lookdayname(zellers_congruence)
    print(day_name)
    display_results(day_name)
    
    
main()
