#!/usr/bin/python3

"""Give me a word with three consecutive double letters. I’ll give you a couple of words
   that almost qualify, but don’t. For example, the word committee, c-o-m-m-i-t-t-e-e. It
   would be great except for the ‘i’ that sneaks in there. Or Mississippi: M-i-s-s-i-s-s-i-
   p-p-i. If you could take out those i’s it would work. But there is a word that has three
   consecutive pairs of letters and to the best of my knowledge this may be the only word.
   Of course there are probably 500 more but I can only think of one. What is the word?"""



def hasThreeConsecutiveDoubles(word):
    """Check if a word has three pairs of double letters consecutively."""

    i  = -1 

    while i < len(word):
        i += 1
        if i < 6:
            continue
        if word[i-1] == word[i-2] and word [i-3] == word [i-4] and word[i-5] == word[i-6]:
            return True


# main program
cin = open('words.txt')

for line in cin:
    if hasThreeConsecutiveDoubles(line):
        print(line)

cin.close()
