#!/usr/bin/python3

"""Read words from a file and calculate the percentage of words without
   the character 'e'."""


def hasNoE(word):
    """Check if a word has 'e' or not."""
    if word.count('e') == 0:
        return True
    else:
        return False


counter = 0
percentage = 0
noEcounter = 0

fin = open('words.txt')

for line in fin:
    if hasNoE(line):
        noEcounter += 1
    
    counter += 1

percentage = 100 * noEcounter / counter

print(f'Total number of words = {counter}')
print(f'Words with no \'e\' = {noEcounter}')
print(f'Percentage of words without E = {percentage:.1f}%')

fin.close()
