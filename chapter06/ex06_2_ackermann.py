#!/usr/bin/python3

"""
See http://en.wikipedia.org/wiki/Ackermann_function. Write a function named ack
that evaluates the Ackermann function. Use your function to evaluate ack(3, 4), which should be
125. What happens for larger values of m and n?
"""

def ack(m, n):
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return ack(m-1, 1)
    else:
        # perforce case:  m > 0 and n > 0; if negative parameters, should throw exception
        return ack(m-1, ack(m, n-1))


# main program
number1 = int(input('m = '))
number2 = int(input('n = '))
print(ack(number1, number2))
