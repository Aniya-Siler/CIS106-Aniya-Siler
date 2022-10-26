def displayExpression(value, count, result):
    print(str(value) + " * " + str(count) + " = " + str(result))

def getAnswer():
    print("Do you want to continue or not")
    answer = input()
    
    return answer

def getValue(name):
    print("Enter " + name + ":")
    value = int(input())
    
    return value

def processExpressions(value, expressioncount):
    for count in range(1, expressioncount + 1, 1):
        result = value * count
        displayExpression(value, count, result)

# Main
# This program uses a loop to generate a list of
# mulitplication expressions for a given value
# References:
# https://bobbyhadz.com/blog/python-input-yes-no-loop
while True:    #This simulates a Do Loop
    value = getValue("value")
    expressioncount = getValue("expression")
    processExpressions(value, expressioncount)
    answer = getAnswer()
    if not(answer == "yes" or answer == "Yes"): break   #Exit loop
