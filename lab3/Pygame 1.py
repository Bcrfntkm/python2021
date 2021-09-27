import pygame
from pygame.draw import*

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1600, 900))
#pygame.display.set_palette(0)
circle(screen, (255, 255, 0), (800, 450), 150)
circle(screen, (255, 0, 0), (745, 410), 32)
circle(screen, (255, 0, 0), (855, 410), 26)
circle(screen, (0, 0, 0), (745, 410), 16)
circle(screen, (0, 0, 0), (855, 410), 13)
rect(screen, (0, 0, 0), (740, 525, 120, 25))
polygon(screen, (255, 255, 255), [(745, )])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
