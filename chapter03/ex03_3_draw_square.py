#!/usr/bin/python3

"""
Exercise 3.3. Note: This exercise should be done using only the statements and other features we
have learned so far.
1. Write a function that draws a grid like the following:
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
Hint: to print more than one value on a line, you can print a comma-separated sequence of
values:
print('+', '-')
By default, print advances to the next line, but you can override that behavior and put a
space at the end, like this:
print('+', end=' ')
print('-')
The output of these statements is '+ -' on the same line. The output from the next print
statement would begin on the next line.
"""

def drawGrid():
    for a in range(2):
        for i in range(2):
            print('+', '-', end='')
            for j in range(3):
                print('-', end=' ')
        print('+')

        for i in range(2):
            print('|', end='')
            for j in range(4):
                print(' ', end=' ')
        print('|')
    
    for i in range(2):
        print('+', '-', end='')
        for j in range(3):
            print('-', end=' ')
    print('+')


drawGrid()