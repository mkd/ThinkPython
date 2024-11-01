
#!/usr/bin/python3

"""
Write a function called cumsum that takes a list of numbers and returns the cumulative sum; that is, a new list where the ith element is the sum of the first i + 1 elements from the
original list. For example:
>>> t = [1, 2, 3]
>>> cumsum(t)
[1, 3, 6]
"""

sum = 0
numbers = input('Enter a list of numbers separated by blanks: ')
t = numbers.split()
for n in t:
    sum += int(n)

print(f'The cumsum is = {sum}')