#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list)==0 or my_list==None:
            return None
    else:
        for i in range((len(my_list)) +1):
            i=1
            if my_list[0] < my_list[i]:
                i += 1
                return my_list[i]
            else:
                return my_list[0]
