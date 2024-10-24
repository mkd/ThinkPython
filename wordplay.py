#!/usr/bin/python3

fin = open('words.txt')

for line in fin:
    word = line.strip()
    print(word)

fin.close()
