class Base:
    """
    Creating our first class.
    """
    """
     A private class
     """
    __nb_objects = 0


def __init__(self, id=None):
    self.id = None

    """
     Initialize instance with id.
    """
    if id is not None:
        self.id = id
    else:
        Base.__nb_objects += 1
        self.id = Base.__nb_objects
