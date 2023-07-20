#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
a = "last digit of"
b = "is"
c = "and is greater than 5"
d = "and is 0"
e = "and is less than 6 and not 0"
f = abs(number) % 10

if number < 0:
    f = -f
    print("{} {} {} {}".format(a, number, b, f,))

if abs(number) % 10 > 5:
    print("{} {} {} {} and is greater than 5".format(a, number, b, f))
if abs(number) % 10 == 0:
    print("{} {} {} {} and is 0".format(a, number, b, f))
if abs(number) % 10 < 6 != 0:
    print("{} {} {} {} {}".format(a, number, b, f, e))
