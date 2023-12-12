#!/usr/bin/python3
for i in range(123):

    if( 65 <= i) and (i <= 90):
        print('{} is upper'.format(chr(i)))
    elif (97 <= i <= 122):
        print('{} is lower'.format(chr(i)))
