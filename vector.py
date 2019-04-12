import math

class Vector(object):

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def mag(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def __repr__(self):
        return '<Vector x: {}, y:{}>'.format(self.x, self.y)
