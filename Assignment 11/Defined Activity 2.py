# This program asks the user to enter their birthday and then displays
# the day of the week they were born

# References:
# https://harpercollege.pressbooks.pub/programmingfundamentals
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


def calculate_zellers_congruence(year, month, day):
    if month == 1:
        month = 13
        year = year - 1
 
    if month == 2:
        month = 14
        year = year - 1

    century_year = year % 100
    century = year // 100

    day_number = (day + 13 * (month + 1) // 5 + 
        century_year + century_year // 4 + 
        century // 4 + 5 * century)

    day_number = day_number % 7
    return day_number


def get_day_name(day_number):
    days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 
        'Wednesday', 'Thursday', 'Friday']
    day_name = days[day_number]
    return day_name


def display_results(day_name):
    print("Your day of birth landed on a " + str(day_name))


def main():
    year = get_year()
    month = get_month()
    day = get_day()

    zellers_congruence = calculate_zellers_congruence(year, month, day)
    day_name = get_day_name(zellers_congruence)

    display_results(day_name)
    
    
main()
