# This program converts an input Miles to Yards, Feet, Inches.
print("Enter amount of Miles.")
miles = float(input())
yard = miles * 1760.0065617
feet = miles * 5280.019685
inches = miles * 63360.23622
print("The Distance in Yards is" + str(yard) + "yds")
print("The Distance in Feet is" + str(feet) + "ft")
print("The Distance in Inches is" + str(inches) + "Ins")
