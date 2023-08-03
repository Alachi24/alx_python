"""
This class represent a Square with a given size

Attribute:
    _size(int): The size of the square(private attribute)
"""


class Square:
    """
    This class represent a Square with a given size

Attribute:
    _size(int): The size of the square(private attribute)
    """

    def __init__(self, size=0):
        """
        initialize a square object with an optional size

        Args:
            size(int): the size of the square(default is 0)
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        @property
        def size(self):
            """
            @property decorator:
            Allows one to create getters and setters method for a private attribute.
            Enables controlled access to that attribute while maintaining encapsulation
            """
            return self.__size

        @size.setter
        def size(self, value):
            """
            @size.setter:
            Decorator used in conjunction with @property to define the setter method for a property
            """
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

        def area(self):
            """
            calculate the area of the square
            Returns:
                int: the area of the square
            """
            return self.__size ** 2
            return area(self.__size ** 2)

        def perimeter(self):
            """
            calculate the perimeter of the square
            Returns:
                int: the perimeter of the square
            """
            return 4 * self.__size

        def get_size(self):
            """
            gets the size of the square
            Returns:
                int: the size of the square
            """
            return self.__size

        def set_size(self, new_size):
            """
            sets the size of the square to a new value

            Args:
                new_size(int): the new size to set

            Raises:
                TypeError: if the new size is not an integer
                ValueError: if the new size is < 0
            """
            if not isinstance(new_size, int):
                raise TypeError("size must be an integer")
            if new_size < 0:
                raise ValueError("Size must be >= 0")
            self.__size = new_size
