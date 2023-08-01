
class Square:

    """using a double underscore with a name after a function makes it private   """

    def __init__(self, size):
        self.__size = size

    def area(self):
        return self.__size ** self.__size
