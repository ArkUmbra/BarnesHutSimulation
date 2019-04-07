from node import Node
from particle import Particle
import random
import pygame
from time import sleep
# import sys

class BarnesHut(object):

    def __init__(self):
        width = 1200
        height = 900
        size = (width, height)

        bg = (255, 255, 255)

        node = Node(size, 0, 0)
        particles = []

        for i in range(900):
            x = random.random() * (width - 100)
            y = random.random() * (height - 100)
            particles.append(Particle(x, y))

        for particle in particles:
            node.addParticle(particle)

        pygame.init()
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Barnes hut')

        clock = pygame.time.Clock()

        running = True
        # main loop
        while running:
            if self.isQuitRequired():
                running = False

            screen.fill(bg)
            colour = (255, 255, 255)
            node.pydraw(pygame.draw, screen)
            pygame.display.update()

            for particle in particles:
                particle.x = particle.x + 1
                particle.y = particle.y + 3

            node = None
            node = Node(size, 0, 0)
            for particle in particles:
                node.addParticle(particle)

            sleep(0.2)
            # clock.tick(60)

        pygame.quit()
        quit()


    def isQuitRequired(self):
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                return True


if __name__ == "__main__":BarnesHut()
