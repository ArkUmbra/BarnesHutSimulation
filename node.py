from drawable import Drawable
from centreofmass import CentreOfMass
from force import Force
import pygame
import constants

class Node(Drawable):


    def __init__(self, size, x, y):
        self.borderColour = constants.NODE_BORDER_COLOUR
        self.width = size[0]
        self.height = size[1]
        self.x = x
        self.y = y
        self.drawGrid = constants.DRAW_GRID
        self.childNodes = {"ne": None, "se": None, "sw": None, "nw": None}
        self.particle = None
        self.centreOfMass = None
        self.theta = constants.THETA
        # self.totalMass = 0

    def addParticle(self, newParticle):
        if (self.isEmptyNode()):
            self.particle = newParticle
            self.centreOfMass = newParticle.getCentreOfMass()
            return

        if (self.childNodes['ne'] is None):
            self.populateNodes()

        if (self.particle is not None):
            # clear centre of mass, as we're going to update it
            # based on child nodes
            self.centreOfMass = None

        self.addParticleToChildNodes(self.particle)
        self.addParticleToChildNodes(newParticle)
        #self.centreOfMass = centreOfMass.combine(centreOfMass2)
        # self.centreOfMass = self.centreOfMass.combine(newParticle.getCentreOfMass())
        self.particle = None

    def populateNodes(self):
        subW = self.width / 2
        subH = self.height / 2
        subSize = (subW, subH)
        x = self.x
        y = self.y
        self.childNodes["nw"] = Node(subSize, x, y)
        self.childNodes["ne"] = Node(subSize, x + subW, y)
        self.childNodes["se"] = Node(subSize, x + subW, y + subH)
        self.childNodes["sw"] = Node(subSize, x, y + subH)

    def addParticleToChildNodes(self, particle):
        if (particle is None):
            return
        # self.totalMass += particle.mass

        for node in self.childNodes.values():
            if (node.boundsAround(particle)):
                node.addParticle(particle)
                com = node.centreOfMass
                self.centreOfMass = com.combine(self.centreOfMass)
                return

        # Node has fallen out of bounds, so we just eat it
        print ('Node moved out of bounds')

    def boundsAround(self, particle):
        pos = particle.pos
        return (pos.x >= self.x
                and pos.y >= self.y
                and pos.x < self.x + self.width
                and pos.y < self.y + self.height)

    # def applyGravityTo(self, particle):
    #     force = self.getForceAppliedTo(particle)
    #
    #     if force is None:
    #         return
    #     particle.applyForce(force)

    def applyGravityTo(self, particle):
        if (self.particle is particle or self.isEmptyNode()):
            return
        elif (self.isExternalNode()):
            Force.applyForceBy(particle, self.particle)
        elif (self.isFarEnoughForApproxMass(particle)):
            Force.applyForceByCOM(particle, self.centreOfMass)
        else:
            # Recurse through child nodes to get more precise total force
            for node in self.childNodes.values():
                node.applyGravityTo(particle)


    def isFarEnoughForApproxMass(self, particle):
        # s('regionwidth') / d('distance') < theta
        # return False
        d = self.centreOfMass.pos.dist(particle.pos)
        return self.width / d < self.theta

    def isInternalNode(self):
        return self.particle is None and self.childNodes['ne'] is not None

    def isExternalNode(self):
        return self.childNodes['ne'] is None and self.particle is not None

    def isEmptyNode(self):
        return self.childNodes['ne'] is None and self.particle is None

    # def getCentreOfMass(self):
    #     if (self.particle is not None:
    #         return self.centreOfMass
    #     else:
    #         return self.centreOfMass.combine

    # def calcMass(self):
    #     cumulative = 0
    #     if (self.particle is not None):
    #         cumulative += self.particle.mass
    #
    #     return cumulative + self.totalMass

    def pydraw(self, pd, screen):
        if (self.drawGrid):
            pd.rect(screen, self.borderColour,
                (self.x, self.y, self.width, self.height), 1)

        if (self.particle is None):
            for node in self.childNodes.values():
                if (node is not None):
                    node.pydraw(pd, screen)
        else:
            self.particle.pydraw(pd, screen)

        if (not constants.DRAW_COM or self.centreOfMass is None):
            return

        mass = self.centreOfMass.mass
        if (self.width > 1):
            font = pygame.font.SysFont('Comic Sans MS', 20 + (int)(30 * self.width / constants.CANVAS_WIDTH))
            textsurface = font.render(str(mass), False, (255,255,255))
            screen.blit(textsurface, (self.x + (self.width * 0.5) - 50, self.y + (self.height*0.5) - 50))

    def __repr__(self):
        return '<Node x: {}, y:{}, width:{}, height:{}, particle:{}, nodes:{}>'.format(self.x, self.y, self.width, self.height, self.particle, self.nodes)
