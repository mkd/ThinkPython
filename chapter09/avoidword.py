#!/usr/bin/python3

"""Ask the user for a forbidden substring and print the number of words without
   the forbidden pattern."""


def hasNoPattern(word, pattern):
    #if word.count(pattern) == 0:
    if pattern not in word:
        return True
    else:
        return False


counter = 0
substring = input('Enter pattern to avoid: ')
fin = open('words.txt')
for line in fin:
    if hasNoPattern(line, substring):
        counter += 1

print(f'Number of words without forbidden pattern = {counter}')
