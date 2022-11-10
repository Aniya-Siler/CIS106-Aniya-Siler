# This program displays the array in order from highest to lowest score from what the user enters
# Refrences:
# https://www.digitalocean.com/community/tutorials/how-to-use-break-continue-and-pass-statements-when-working-with-loops-in-python-3
# https://stackoverflow.com/questions/70238155/ask-a-user-for-10-integers-one-at-a-time-and-store-in-list-python

def get_score():
    print ("Enter the scores:")
    score = int(input())
    return score

def get_scores_array():
    array = []
    while True:
        score = get_score()
        if not(score >= 0): break
        array.append(score)
    return array
    
def get_highest_score(array):
    highest = array[0]
    for index in range(1,len(array)):
        if highest < array[index]:
            highest = array[index]
    return highest

def get_lowest_score(array):
    lowest = array[0]
    for index in range(1,len(array)):
        if lowest > array[index]:
            lowest = array[index]
    return lowest

def get_average(array):
    total = 0
    for index in range(len(array)):
        total += array[index]
    average = total/array[index]
    return average
   
def display_result(highest, lowest, average):
    print("Highest score is " + str(highest) +
          " Lowest score is " + str(lowest) +
          " Average is " + str(average))
    
def main():
    array = get_scores_array()
    print(array)
    highest = get_highest_score(array)
    print(highest)
    lowest = get_lowest_score(array)
    print(lowest)
    average = get_average(array)
    print(average)
    display_result(highest, lowest, average)
    
    
main()
