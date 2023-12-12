#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
ld = int(repr(number)[-1])
str1 = " and is greater than 5"
str2 = " and is 0"
str3 = " and is less than 6 and not 0"
if number < 0:
    ld = number % -10
else:
    ld = number % 10
if ld > 5:
    print("Last digit of {} is {}".format(number, ld) + str1)
elif ld == 0:
    print("Last digit of {} is {}".format(number, ld) + str2)
else:
    print("Last digit of {} is {}".format(number, ld) + str3)
