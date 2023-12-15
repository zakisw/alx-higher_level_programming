#!/usr/bin/python3
def uppercase(txt):
    for i in (txt):
        if (i >= 'a') and (i <= 'z'):
            j = ord(i) - 32
            print('{}'.format(chr(j)), end='')
        else:
            print('{}'.format(i), end='')
    print(end='\n')
