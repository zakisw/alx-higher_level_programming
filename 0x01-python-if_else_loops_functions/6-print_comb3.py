#!/usr/bin/python3
for i in range(0,9):
    for j in range (0,9):
        if i == j:
            pass
        else:
            print('{}{} ,'.format(i,j), end='')
