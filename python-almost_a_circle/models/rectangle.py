# TASK 0

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


# TASK 1

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

       # TASK 2

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
        if value < 0:
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
        if value < 0:
            raise ValueError("y must be >= 0")

    # TASK 3

    def area(self):
        """
       Calculate the area of the geometry.

        Raises:
            its value after multiplication
        """
        return self.width * self.height

    # TASK 6
    # Modified from task 4
    def display(self):
        """
        will use this method to display the instances using "#"
        """
        for row in range(self.y):
            print()
        else:
            for row in range(self.height):
                for column in range(self.x):
                    print(" ", end="")
                else:
                    for column in range(self.width):
                        print("#", end="")
                    else:
                        print()

    # TASK 5

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    # TASK 7

    def update(self, *args):
        """
        passing arguments to attributes
        """
        args_length = len(args)

        if args_length > 0:
            self.id = args[0]  # only this will run
        if args_length > 1:
            self.id = args[1]  # only "0" then "1" will run
        if args_length > 2:
            self.id = args[2]  # only "0, 1" then "2" will run
        if args_length > 3:
            self.id = args[3]  # only "0, 1, 2" then "3" will run
        if args_length > 4:
            self.id = args[4]  # only "0, 1, 2, 3" then "4" will run
