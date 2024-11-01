#!/usr/bin/python3

"""Print words with more than 20 characters, without counting whitespaces"""

fin = open('words.txt')

for line in fin:
    if len(line) > 20:
        print(line)

fin.close()
