#!/usr/bin/python3

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
n = int(input("n = "))

if n > 2 and a**n+b**n == c**n:
    print("Holy smokes, Fermat was wrong!")
else:
    print("No, that doesn't work.")

