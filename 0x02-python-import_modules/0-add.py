#!/usr/bin/python3
addition =  __import__('add_0', globals(), locals(), [], 0)
a = 1
b = 2
result = addition.add(a,b)
print(f'{a} + {b} = {result}')
