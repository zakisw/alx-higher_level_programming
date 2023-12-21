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

    def area(self):
        """
        Return the area of square
        """
        return self.__size ** 2

    @property
    def size(self):
        '''
        return the size of square
        '''
        return self.__size

    @size.setter
    def size(self, value):

        '''
        Set the value of size
        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = value
    def my_print(self):
        for i in range (0,self.__size):
            if self.__size == 0:
                print(end='\n')
            else:
                print('#'*self.__size)
            
