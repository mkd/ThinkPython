#!/usr/bin/python3

"""
Exercise 6.4. A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a
function called is_power that takes parameters a and b and returns True if a is a power of b. Note:
you will have to think about the base case.
"""

def isPower(a, b):
    if b == 0:
        return False
    elif a == b:
        return True
    elif a % b == 0 and isPower(a/b, b):
        return True
    else:
        return False
    

# main program
a = int(input('a = '))
b = int(input('b = '))
if isPower(a, b):
    print(f'{a} is a power of {b}')
else:
    print(f'{a} is NOT a power of {b}')