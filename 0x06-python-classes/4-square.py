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
        self.__size = size
        def size(self):
            self.__size=size
        def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        else:
        self.__size = value

    def area(self):
        """
        Return the area of square
        """

        return self.__size ** 2
