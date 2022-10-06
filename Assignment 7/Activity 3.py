def calculateCenti(miles):
    centi = miles * 160934
    
    
    return centi

def calculateFeet(miles):
    feet = miles * 5280.019685
    
    return feet

def calculateInches(miles):
    inches = miles * 63360.23622
    
    return inches


def calculateKilo(miles):
    kilo = miles * 1.60934
    
    return kilo


def calculateMeters(miles):
    meters = miles * 1609.34
    
    return meters


def calculateUS(metric, yards, inches, feet, getMiles):
    pass


def calculateYards(miles):
    yards = miles * 1760.0065617
    
    return yards


def displayResult(result, label):
    print(str(result) + " " + label)


def getChoice():
    print("Enter US to convert to US or Metric to convert to Metric:")
    choice = input()
    
    return choice


def getMeasurment(scale):
    print("Enter" + scale + "Measurment:")
    measurment = float(input())
    
    return measurment


def getMiles():
    print("Enter amount of Miles.")
    miles = float(input())
    
    return miles


def processMetric(miles):
    result = calculateKilo(miles)
    displayResult(result, "Kilometers")
    result = calculateMeters(miles)
    displayResult(result, "Meters")
    result = calculateCenti(miles)
    displayResult(result, "Centimeters")

    
def processUS(miles):
    result = calculateYards(miles)
    displayResult(result, "Yards")
    result = calculateFeet(miles)
    displayResult(result, "Feet")
    result = calculateInches(miles)
    displayResult(result, "Inches")

# Main
# Ask the user to input distance in miles,
# and ask if they would like to convert the distance to US or Metric.
# Display Results.
miles = getMiles()
choice = getChoice()
if choice == "Metric" or choice == "metric":
    processMetric(miles)
else:
    if choice == "US" or choice == "us":
        processUS(miles)
    else:
        print("You must enter Metric to convert to Metric or US to convert to US!")
