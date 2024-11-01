#!/usr/bin/python3

"""
Exercise 10.5. Write a function called is_sorted that takes a list as a parameter and returns True
if the list is sorted in ascending order and False otherwise. For example:
>>> is_sorted([1, 2, 2])
True
>>> is_sorted(['b', 'a'])
False
"""


def isSorted(elements):
    """Return True if elements are sorted in ascending order, False otherwise."""

    # special case:
    if len(elements) <= 1:
        return True
    
    for i in range(0, len(elements) - 1):
        if not (elements[i] < elements[i+1]):
            return False
    return True


# main program
t = input('Enter list of elements: ')
e = t.split()
if (isSorted(e)):
    print('The list is sorted.')
else:
    print('The list is not sorted!')