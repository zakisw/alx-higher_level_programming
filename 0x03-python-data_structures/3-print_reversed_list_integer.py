#!/usr/bin/python3 
def print_reversed_list_integer(my_list=[]):
	x = 1
	for i in range (len(my_list)):
		if my_list == None:
			break
		else:
			print("{:d}".format(my_list[len(my_list)-x]))
			x+=1
