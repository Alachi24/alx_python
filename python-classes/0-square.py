
class Square:

    """using a double underscore with a name after a function makes it private   """

    def __init__(self, size):
        self.__size = size

    def area(self):
        return self.__size ** self.__size


my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)
print(Square.__doc__)
