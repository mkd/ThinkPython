#!/usr/bin/python3

import turtle

def drawKorch(t, length):
    if length <= 3:
        t.fd(length)
    else:
        drawKorch(t, length/3)
        t.lt(60)
        drawKorch(t, length/3)
        t.rt(120)
        drawKorch(t, length/3)
        t.lt(60)
        drawKorch(t, length/3)


bob = turtle.Turtle()
length = int(input("x = "))
drawKorch(bob, length)
