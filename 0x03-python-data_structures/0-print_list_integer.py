#!/usr/bin/python3
def print_list_integer(my_list=[]):
    my_list = ['{}'.format(i) for i in range(len(my_list))]
    for x in my_list:
        print(x)
