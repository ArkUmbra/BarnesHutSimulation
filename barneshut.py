from node import Node
from particle import Particle
from point import Point
from time import sleep
from vector import Vector
import random
import math
import pygame
import constants
# import sys

class BarnesHut(object):

    def __init__(self):
        self.width = constants.CANVAS_WIDTH
        self.height = constants.CANVAS_HEIGHT
        self.noOfParticles = constants.NO_OF_PARTICLES
        bg = constants.BG_COLOUR
        size = (self.width, self.height)


        rootNode = Node(size, 0, 0)
        particles = self.generateParticles()

        for particle in particles:
            rootNode.addParticle(particle)

        pygame.init()
        screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(constants.WINDOW_TITLE)

        # clock = pygame.time.Clock()

        running = True
        # main loop
        while running:
            if self.isQuitRequired():
                running = False

            sleep(constants.SLEEP_BETWEEN_DRAW)

            # TODO split our real space dimensions to screen pixels
            self.drawScreen(screen, rootNode)

            if False:
                continue
            # screen.fill(bg)
            # rootNode.pydraw(pygame.draw, screen)
            # pygame.display.update()

            # calc changes due to gravity
            for particle in particles:
                rootNode.applyGravityTo(particle)

            # recreate the tree for the next step
            rootNode = None
            rootNode = Node(size, 0, 0)
            for particle in particles:
                # while we're doing this, update particle positions
                #based on forces received
                particle.tick()
                rootNode.addParticle(particle)

            # clock.tick(60)

        pygame.quit()
        quit()


    def generateParticles(self):
        w = self.width
        h = self.height

        particles = []

        # large mass
        sun = Particle(Point(self.width*0.5, self.height*0.5), -1, constants.PARTICLE_MASS*120)
        particles.append(sun)

        particles.append(Particle(Point(self.width*0.2, self.height*0.2), -2, constants.PARTICLE_MASS*70, velocity=Vector(4, 1)))

        for id in range(self.noOfParticles):
            # x = (self.width - 150) + random.random()*100
            # y = (self.height - 150) + random.random()*100

            # Try to bias spawns towards the centre
            # xSeed = math.sin(math.degrees(random.random() * 180)) #- 0.5 # -0.5 0.5
            # ySeed = math.sin(math.degrees(random.random() * 180)) #- 0.5 # -0.5 0.5

            # xSeed = math.cos(math.degrees((random.random()-0.5) * 180)) #- 0.5 # -0.5 0.5
            # ySeed = math.cos(math.degrees((random.random()-0.5) * 180)) #- 0.5 # -0.5

            # xSign = 1 if random.random() > 0.5 else -1
            # ySign = 1 if random.random() > 0.5 else -1

            # x = (xSeed * w) + w/2
            # y = (ySeed * h) + h/2
            x = random.gauss(w/2, w/7)
            y = random.gauss(h/2, h/7)
            pos = Point(x, y)
            angle = random.gauss(math.pi*2, math.pi/2)
            xVel = (random.random()-0.5) * 40
            yVel = (random.random()-0.5) * 40
            # xVel = sun.pos.dist(pos) * math.sin(angle)
            # yVel = sun.pos.dist(pos) * math.cos(angle)
            vel = Vector(xVel, yVel)
            mass = random.random() * constants.PARTICLE_MASS * 10
            particles.append(Particle(pos, id, mass, velocity = vel))
        return particles


    def isQuitRequired(self):
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                return True

    def drawScreen(self, screen, rootNode):
        screen.fill(constants.BG_COLOUR)
        rootNode.pydraw(pygame.draw, screen)
        pygame.display.update()


if __name__ == "__main__":BarnesHut()
