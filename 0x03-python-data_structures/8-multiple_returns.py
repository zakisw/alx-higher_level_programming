#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        x = len(sentence)
        y = 'None'
        tuple_1 = x, y
        return tuple_1
    else:
        x = len(sentence)
        y = sentence[0]
        tuple_1 = x, y
        return tuple_1
