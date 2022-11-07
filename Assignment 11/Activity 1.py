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
    print (day_number)

def lookdayname(day_number):
    day = {
            0 : "Saturday",
            1 : "Sunday",
            2 : "Monday",
            3 : "Tuesday",
            4 : "Wednesday",
            5 : "Thursday",
            6 : "Friday"
        }
    return day_name

