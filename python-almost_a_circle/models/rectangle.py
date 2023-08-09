"""
Defining a class that has both private and instances
"""


class Base:
    """
    Creating our first class.
    """
    """
     A private class
     """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        function __init__ calling self and an id
        """
        self.id = None

        """
        Initialize instance with id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


"""
The class rectangle is inheriting from class Base
"""


class Rectangle(Base):
    """Rectangle class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        self.__width = value

        """
        Raises:
        TypeError: the width must be an integer
        ValueError: the width must be > 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        self.__height = value

        """
        Raises:
        TypeError: the height must be an integer
        ValueError: the height must be > 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x coordinate of the rectangle"""
        self.__x = value

        """
        Raises:
        TypeError: the x must be an integer
        ValueError: the x must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y coordinate of the rectangle"""
        self.__y = value

        """
        Raises:
        TypeError: the y must be an integer
        ValueError: the y must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be >= 0")

    # def area(self):
    #     """
    #     Calculate the area of the geometry.

    #     Raises:
    #         its value after multiplication
    #     """
    #     return self.width ** self.height
