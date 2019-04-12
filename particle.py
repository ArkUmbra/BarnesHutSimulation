from drawable import Drawable
from centreofmass import CentreOfMass
from point import Point
from vector import Vector
import constants as cn
import math


class Particle(Drawable):

    def __init__(self, pos, id, mass = cn.PARTICLE_MASS, velocity = Vector()):
        self.particleColour = cn.PARTICLE_COLOUR
        self.pos = pos
        self.id = id
        self.mass = mass
        self.velocity = velocity
        self.accel = Vector()

    def tick(self):
        # if (self.pos.x > 850 and self.pos.y > 550):
        #     print(self)

        self.velocity.x += self.accel.x
        self.velocity.y += self.accel.y

        self.accel = Vector()

        self.pos.x += cn.TICK_SECONDS * self.velocity.x / cn.SCALE_TO_METERS
        self.pos.y += cn.TICK_SECONDS * self.velocity.y / cn.SCALE_TO_METERS


    # def pullByGravity(self, centreOfMass):
    #     combinedMass = self.mass + centreOfMass.mass
    #     x = self.pos


    def getCentreOfMass(self):
        return CentreOfMass(self.mass, Point(self.pos.x, self.pos.y))

    def pydraw(self, pd, surface):
        vmag = self.velocity.mag()
        colour = (self.clamp(50 + vmag, 255),
            # self.clamp(self.mass / cn.PARTICLE_MASS, 255),
            self.clamp(10+ vmag/4, 255),
            self.clamp(10+ vmag/3, 255))

        x = math.floor(self.pos.x)
        y = math.floor(self.pos.y)
        # pd.rect(surface, self.particleColour, (self.pos.x, self.pos.y, 1, 1), 0)
        # pd.circle(surface, self.particleColour, (self.pos.x, self.pos.y), math.floor(self.mass/3), 0)
        pd.circle(surface, colour, (x,y), 1 + math.floor(0.2*self.mass/cn.PARTICLE_MASS), 0)

    def clamp(self, number, clampMax):
        val = number if number < clampMax else clampMax
        val = val if val > 0 else 0
        return math.floor(val)

    def __repr__(self):
        return '<Particle x: {}, y:{}>'.format(self.pos.x, self.pos.y)
