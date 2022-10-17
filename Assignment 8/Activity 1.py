def displayExpression(value, count, result):
    print(str(value) + " * " + str(count) + " = " + str(result))

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
# https://harpercollege.pressbooks.pub/programmingfundamentals/chapter/loop-examples/
# https://www.youtube.com/watch?v=yaqMSBr_NCU&t=347s
value = getValue("value")
expressioncount = getValue("expression")
processExpressions(value, expressioncount)
