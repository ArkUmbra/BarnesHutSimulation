import math

class Point(object):


    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        x = math.fabs(self.x - other.x)
        y = math.fabs(self.y - other.y)

        return math.hypot(x, y)

    def distx(self, other):
        return math.fabs(self.x - other.x)

    def disty(self, other):
        return math.fabs(self.y - other.y)
