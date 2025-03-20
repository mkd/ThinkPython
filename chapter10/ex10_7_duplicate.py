#!/usr/bin/python3

"""
Exercise 10.7. Write a function called has_duplicates that takes a list and returns True if there is any element that appears more than once. It should not modify the original list.
"""


def hasDuplicates(mylist):
    """Check if there are duplicate elements."""
    for i in range(0, len(mylist)):
        for j in range(0, len(mylist)):
            if i != j:
                if mylist[i] == mylist[j]:
                    return True
    return False


# main program
mylist = []
while True:
    word = input('Enter a word: ')
    if word:
        mylist.append(word)
        continue
    break
    
if hasDuplicates(mylist):
    print(f'The list contains duplicates.')
else:
    print(f'The list does not contain duplicates.')
