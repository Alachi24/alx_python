"""using a double underscore with a name after a function makes it private   """


class Square:
    def __init__(self, size):
        self.__size = size

    def length(self):
        print(4)


c = Square
c.length()
