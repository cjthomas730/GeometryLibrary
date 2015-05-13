"""
core components for geomlib
"""


def hello_world():
    print('It works!')


class BaseGeometry(object):

    def __init__(self, num_sides):
        self.num_sides = num_sides

        if self.num_sides is 3:
            self._type = 'triangle'
        elif self.num_sides is 4:
            self._type = 'rectangle'
        else:
            raise ValueError('Invalid number of sides: %s' % num_sides)

    @property
    def type(self):
        return self._type


class Rectangle(BaseGeometry):

    def __init__(self):
        self.is_square = False


def square_from_side(length):

    """
    Return an instance of `Rectangle()` that is square.
    """

    pass

