#!/usr/bin/python3

"""
Defining the class Square.
"""


class Square:
    """
    Representing the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializing the  new Square.

        Arguments:
            size (int): size of the new square.
        """
        self.__size = size
        self.__position = position

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
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance (value, tuple) and value >=0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    def my_print(self):
        '''
        prints in stdout the square with the character #
        '''
        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ",  end="")
                print("#" * (self.__size))


