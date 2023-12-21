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
        self.size = size
    def size(self):
        return self.__size
    def size(self, value):
        if isinstance(value, int):
            pass
        else:
            raise TypeError("size must be an integer")
        if value < 0:
            raise TypeError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Return the area of square
        """
        return (self.__size * self.__size)
    def my_print(self):
        """Print the square with the # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
