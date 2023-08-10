"""
importing attributes from rectangle.py
"""
# TASK 9
from rectangle import Rectangle

"""
the class Square is inheriting from Rectangle
"""


class Square(Rectangle):
    """
    initializing the attributes
    """

    def __init__(self, size, x=0, y=0, id=None):
        # size will stand for width & height
        super().__init__(size, size, x=0, y=0, id=None)

    def __str__(self):
        # I won't change width & height to size because size isn't defined due to inheritance
        return "[Square] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

# TASK 10
    """
    adding the setter and getter for the size
    """
    @property
    def size(self):
     # getter method
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
