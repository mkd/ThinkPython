#!/usr/bin/python3

"""
Exercise 10.8. This exercise pertains to the so-called Birthday Paradox, which you can read about
at http: // en. wikipedia. org/ wiki/ Birthday_paradox. If there are 23 students in your class,
what are the chances that two of them have the same birthday?

You can estimate this probability by generating random samples of 23 birthdays and checking for
matches. Hint: you can generate random birthdays with the randint function in the random
module.
"""
import random


def generateBirthdays(n):
    """Generate a number of bithday dates, using 365 ints for each day of the year,
       and store them in a list to be returned."""
    bday_list = []
    for i in range(0, n):
        bday_list.append(random.randint(1, 365))

    return bday_list



def hasRepeated(nlist):
    """set() makes a list of different values, so we can compare it in length with the original
       list and, if the lenghts differ, there were repeated values."""
    filtered_list = set(nlist)
    if len(filtered_list) != len(nlist):
        return True
    else:
        return False


# main program
ntimes = 1000
repetitions = 0


"""Run the experiment ntimes, and take the avg. probability."""
for i in range(0, ntimes):
    mylist = generateBirthdays(23)
    if hasRepeated(mylist):
        repetitions = repetitions + 1

probability = repetitions * 100 / ntimes
print(f'Run the experiment {ntimes} times.')
print(f'Birthdays repeated in {repetitions} ocasions.')
print(f'Avg. probability: {probability}%')
