def calculateFeet(miles):
    feet = miles * 5280.019685
    
    return feet

def calculateInches(miles):
    inches = miles * 63360.23622
    
    return inches

def calculateYard(miles):
    yard = miles * 1760.0065617
    
    return yard

def displayResult(miles, yard, feet, inches):
    print("The Distance in Yards is" + str(yard) + "yds")
    print("The Distance in Feet is" + str(feet) + "ft")
    print("The Distance in Inches is" + str(inches) + "Ins")

def getMiles():
    print("Enter amount of Miles.")
    miles = float(input())
    
    return miles

# Main
# This program asks the user for amount of Miles,
# Converts the given amount to Yards, Feet, Inches,
# and displays the results.
miles = getMiles()
yard = calculateYard(miles)
feet = calculateFeet(miles)
inches = calculateInches(miles)
displayResult(miles, yard, feet, inches)
