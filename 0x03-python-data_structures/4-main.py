#!/usr/bin/python3
new_in_list = __import__('4-new_in_list').new_in_list

my_list = [1, 2, 3]
idx = 0
new_element = 4
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)
