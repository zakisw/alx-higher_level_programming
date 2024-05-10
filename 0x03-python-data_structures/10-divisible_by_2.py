#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result_list = []
    for i in my_list:
        if i % 2 == 0:
            result_list.insert(0, True)
        else:
            result_list.insert(0, False)
    return result_list
