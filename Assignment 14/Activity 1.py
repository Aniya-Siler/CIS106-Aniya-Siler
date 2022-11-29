# This progam displays high, low, and average scores based on input from scores.txt.
# References:
# https://www.stechies.com/read-file-line-by-line-python/
# https://harpercollege.pressbooks.pub/programmingfundamentals/chapter/python-examples-7/


def read_file(filename):
    try:
        filename = open("scores.txt", "r") 
        array = []
        while True:
            line = filename.readline()
            if line== "":
                break
            else:
                line = line.strip()
                line = line.split(',')
                score = line[1]
                array.append(int(float(score)))
    except Exception as e:
        print(e)
    return array


def get_highest_score(array):
    highest = array[1]
    for index in range(1, len(array)):
        if highest < array[index]:
            highest = array[index]
    return highest


def get_lowest_score(array):
    lowest = array[1]
    for index in range(1, len(array)):
        if lowest > array[index]:
            lowest = array[index]
    return lowest


def get_average(array):
    total = 0
    for index in range(len(array)):
        total += array[index]
    average = total /len(array)
    return average
   
   
def display_result(array, highest, lowest, average):
    print(array)
    print("High is " + str(highest))
    print(" Low is " + str(lowest))
    print(" Average is " + str(average))

    
def main():
    filename = 'scores.txt'
    array = read_file(filename)
    highest = get_highest_score(array)
    lowest = get_lowest_score(array)
    average = get_average(array)
    display_result(array, highest, lowest, average)


main()
        
         
