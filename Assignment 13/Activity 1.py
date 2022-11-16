# This program asks user for full name
# and displays it as lastname, first initial
# References:
# https://bobbyhadz.com/blog/python-split-string-on-first-occurrence
# https://discuss.codecademy.com/t/how-to-select-only-last-names/435968
# https://harpercollege.pressbooks.pub/programmingfundamentals/chapter/python-examples-7/


def get_full_name():
    print("What's your full name?")
    full_name = str(input())
    return full_name
    
    
def get_first_ini(full_name):
    first = full_name.strip()[0]
    return first


def get_last_name(full_name):
    last = full_name.split()[1]
    return last


def display_name(first, last):
    print(last + ', ' + first + '.')
    
    
def main():
    full_name = get_full_name()
    first = get_first_ini(full_name)
    last = get_last_name(full_name)
    display_name(first, last)
    

main()
