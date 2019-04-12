import constants

class Force(object):


    def __init__(self):
        self.xForce = 0
        self.yForce = 0

    def add(self, other):
        return Force(self.xForce + other.xForce, self.yForce + other.yForce)

    # def accelerate(particle):


    # @staticmethod
    # def calcForceOn(particle, centreOfMass):
    #     xDiff = p1.pos.distx(p2.pos)
    #     yDiff = p1.pos.disty(p2.pos)
    #     dist = p1.pos.dist(p2.pos)
    #
    #     f = constants.CALC_TICK_TIME *
    #         (constants.GRAVITATIONAL_CONSTANT * p1.mass * p2.mass)
    #         / math.pow(dist)
    #
    #     p1.accel.x = f * xDiff / p1.mass
    #     p2.accel.y = f * yDiff / p1.mass

    @staticmethod
    def applyForceBy(p1, p2):
        # G = 6.673 x 10-11 Nm^2/kg^2
        # Fgrav = (G*m1*m2)/d^2
        # F = m*a
        xDiff = p1.pos.x - p2.pos.x #.distx(p2.pos)
        yDiff = p1.pos.y - p2.pos.y #.disty(p2.pos)
        dist = p1.pos.dist(p2.pos)

        f = constants.TICK_SECONDS * (constants.GRAVITATIONAL_CONSTANT * p1.mass * p2.mass) / dist*dist

        p1.accel.x -= f * xDiff / p1.mass
        p1.accel.y -= f * yDiff / p1.mass
        p2.accel.x += f * xDiff / p2.mass
        p2.accel.y += f * yDiff / p2.mass

    @staticmethod
    def applyForceByCOM(p1, com):
        # G = 6.673 x 10-11 Nm^2/kg^2
        # Fgrav = (G*m1*m2)/d^2
        # F = m*a
        xDiff = p1.pos.x - com.pos.x #.distx(p2.pos)
        yDiff = p1.pos.y - com.pos.y #.disty(p2.pos)
        dist = p1.pos.dist(com.pos)

        f = constants.TICK_SECONDS * (constants.GRAVITATIONAL_CONSTANT * p1.mass * com.mass) / dist*dist

        p1.accel.x -= f * xDiff / p1.mass
        p1.accel.y -= f * yDiff / p1.mass
