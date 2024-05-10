#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
            return None
    elif len(my_list) == 1:
        return my_list[0]
    else:
            for j in range((len(my_list))):
                if  my_list[1]>my_list[j]:
                    maxx = my_list[1]
                else:
                    maxx = my_list[j]
                    j+=1
                return maxx   
                    

