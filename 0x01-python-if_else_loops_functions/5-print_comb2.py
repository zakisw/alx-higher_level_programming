#!/usr/bin/python3
for i in range(0, 100):
    if 0 <= i < 10:
        print(f'0{i:d}, ', end='')

    else:
        print(f'{i:d}, ', end='')
