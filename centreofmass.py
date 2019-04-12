from point import Point

class CentreOfMass(object):


    def __init__(self, mass, pos):
        self.mass = mass
        self.pos = pos

    def combine(self, other):
        if (other is None):
            return self

        # m = m1 + m2
        # x = (x1*m1 + x2*m2) / m
        # y = (y1*m1 + y2*m2) / m

        m = self.mass + other.mass

        newX = (self.pos.x * self.mass + other.pos.x * other.mass) / m
        newY = (self.pos.y * self.mass + other.pos.y * other.mass) / m

        position = Point(newX, newY)

        return CentreOfMass(self.mass + other.mass, position)

    def __repr__(self):
        return '<CentreOfMass mass: {}, pos:{}>'.format(self.mass, self.pos)
