#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    elif len(my_list) == 1:
        return my_list[0]
    else:
        maxx = my_list[0]
        for j in my_list[1:]:
            if j > maxx:
                maxx = j
        return maxx
