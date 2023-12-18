#!/usr/bin/python3
def uppercase(txt):

    for i in (txt):
        if (i >= 'a') and (i <= 'z'):
            j = chr(ord(i) - 32)
            print('{}'.format(j),end='')
        else:
            j = i 
            print('{}'.format(j),end='')


         
