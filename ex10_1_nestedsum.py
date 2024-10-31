#!/usr/bin/python3

"""
Write a function called nested_sum that takes a list of lists of integers and adds up
the elements from all of the nested lists. For example:
>>> t = [[1, 2], [3], [4, 5, 6]]
>>> nested_sum(t)
"""

def nested_sum(t):
    sum = 0
    for i in t:
        for j in i:
            sum += j

    return sum


numbers = [[3, 4, 6], [8, 5, 9]]
print(nested_sum(numbers))