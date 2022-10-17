def displayExpression(value, count, result):
    print(str(value) + " * " + str(count) + " = " + str(result))

def getValue(name):
    print("Enter " + name + ":")
    value = int(input())
    
    return value

def processExpressions(value, expressioncount):
    count = 1
    while count <= expressioncount:
        result = value * count
        count = count + 1
        result = result + 1
        displayExpression(value, count, result)

# Main
# This program uses a loop to generate a list of
# mulitplication expressions for a given value
# References:
# https://harpercollege.pressbooks.pub/programmingfundamentals/chapter/loop-examples/
# https://stackoverflow.com/questions/51187314/how-do-i-use-while-loops-to-create-a-multiplication-table
value = getValue("value")
expressioncount = getValue("expression")
processExpressions(value, expressioncount)
