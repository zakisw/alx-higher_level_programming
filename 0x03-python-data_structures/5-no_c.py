#!/usr/bin/env python3
def no_c(my_string):
    translate_table = {ord("c") : None, ord("C") : None}
    return my_string.translate(translate_table)
