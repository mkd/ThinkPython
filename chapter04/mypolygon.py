#!/usr/bin/python3

# Small app to draw polygons.

import turtle
import math

# polygon drawing functions
def polyline(t, n, length, angle):
"""Draw any kind of line in n steps of length with a given angle."""
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, n, length):
"""Draw a polygon with n sides of a given length."""
    angle = 360 / n
    polyline(t, n, length, angle)


def circle(t, r):
"""Draw a circle of a given radius r."""
    arc(t, r, 360)


def arc(t, r, angle):
"""Draw an arc of a given radius r and a given angle (=length in this case)."""
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    polyline(t, n, step_length, step_angle)


# main program
bob = turtle.Turtle()
circle(bob, 100)

turtle.mainloop()
