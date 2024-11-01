#!/usr/bin/python3

import time

# get the time since Epoch in seconds
t = time.time()

# calculate the day
days = t // 3600 // 24

# get the reminder of seconds after calculating the days
t %= (3600 * 24)

# calculate the hours
hours = t // 3600

# new reminder of seconds after extracting the hours
t %= 3600

# calculate the minutes
minutes = t // 60

# the remining seconds
seconds = t % 60



print("Time since epoch: " + str(days) + "d, " + str(hours) + "h, " + str(minutes) + "min, " + str(seconds) + "s.")
