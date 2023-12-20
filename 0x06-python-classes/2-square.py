#!/usr/bin/python3

"""
Defining the class Square.
"""


class Square:
    """
    Representing the square.
    """

    def __init__(self, size=0):
        """
        Initializing the  new Square.

        Arguments:
            size (int): size of the new square.
        """
        if isinstance(size, int):
            pass
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be >= 0")
        self.__size = size
