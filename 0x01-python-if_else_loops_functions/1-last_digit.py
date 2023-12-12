#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
ld = int(repr(number)[-1])
if number > 0:
    if ld > 5:
        print(f'Last digit of {number} is {ld:d} and is greater than 5')

    elif ld == 0:
        print(f'Last digit of {number} is {ld:d} and is 0')

    else::
        print(f'Last digit of {number} is {ld:d} and is less than 6 and not 0')

elif number < 0:

    if ld == 0:
        print(f'Last digit of {number} is {ld:d} and is 0')
    else:
        print(f'Last digit of {number} is {-ld:d} and is less than 6 and not 0')


else:
    print(f'Last digit of {number} is {ld:d} and is 0')
    
