#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    x = 1
    if not my_list:
            return None
    for i in range(len(my_list)):
        print("{:d}".format(my_list[len(my_list)-x]))
        x += 1
