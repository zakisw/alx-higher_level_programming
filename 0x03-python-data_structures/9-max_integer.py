#!/usr/bin/python3
def max_integer(my_list=[]):
    for x in my_list:
        if x == None:
            return None
        else:
            for i in range((len(my_list)) +1):
                i=1
                if my_list[0] < my_list[i]:
                    i += 1
                    return my_list[i]
                else:
                    return my_list[0]
