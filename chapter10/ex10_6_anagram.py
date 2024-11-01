#!/usr/bin/python3

"""
Exercise 10.6. Two words are anagrams if you can rearrange the letters from one to spell the other.
Write a function called is_anagram that takes two strings and returns True if they are anagrams.
"""


def isAnagram(word1, word2):
    """Check letter by letter, if the words are anagrams to each other."""
    t1 = list(word1)
    t2 = list(word2)
    t1.sort()
    t2.sort()
    if t1 == t2:
        return True
    else:
        return False


# main program
word1 = input('Enter a word: ')
word2 = input('Enter another word: ')
if isAnagram(word1, word2):
    print(f'The words {word1} and {word2} are anagrams.')
else:
    print(f'The words {word1} and {word2} are not anagrams!')