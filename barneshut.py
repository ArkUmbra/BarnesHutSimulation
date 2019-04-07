from PIL import Image, ImageDraw
from node import Node
from particle import Particle
import random
import pygame
from time import sleep
# import sys

# size = 500
width = 1200
height = 900
size = (width, height)

bg = (255, 255, 255)

# img = Image.new('RGB', (size, size), color='white')
# d = ImageDraw.Draw(img)

node = Node(size, 0, 0)

particles = []

for i in range(900):
    x = random.random() * (width - 100)
    y = random.random() * (height - 100)
    # x = i * 40
    # y = i * 23
    particles.append(Particle(x, y))

# particles.append(Particle(31, 182))
# particles.append(Particle(17, 179))

for particle in particles:
    # print("x {}, y {}".format(particle.x, particle.y))
    node.addParticle(particle)


pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Barnes hut')

clock = pygame.time.Clock()

running = True
# main loop
while running:
    # event handling, gets all event from the event queue
    for event in pygame.event.get():
        # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            running = False

    screen.fill(bg)
    colour = (255, 255, 255)
    # pygame.draw.rect(screen, colour, (50, 50, 7, 7), 1)
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

# node.draw(d)
# img.save('barneshut.png')

pygame.quit()
quit()
