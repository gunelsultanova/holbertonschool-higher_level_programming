#!/usr/bin/python3
"""This module defines a Square class.

The Square class represents a square object defined by its size. It includes methods for initializing the square object and calculating its area.
"""


class Square:
    """A class that defines a square by its size.

    Attributes:
        __size (int): The size of the square.
    """
    def __init__(self, size=0):
        """Method to initialize the square object.

        Args:
            size (int): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Method that returns the square area of the object.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
