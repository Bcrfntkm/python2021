import pygame
from pygame.draw import*

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
#pygame.display.set_palette(0)
rect(screen, (255, 255, 255), (0, 0, 400, 400))
circle(screen, (255, 255, 0), (200, 200), 100)
circle(screen, (255, 0, 0), (150, 175), 17)
circle(screen, (255, 0, 0), (250, 175), 14)
circle(screen, (0, 0, 0), (150, 175), 9)
circle(screen, (0, 0, 0), (250, 175), 8)
rect(screen, (0, 0, 0), (150, 250, 100, 20))
polygon(screen, (0, 0, 0), [(177, 174), (100, 120), (107, 114), (182, 165)])
polygon(screen, (0, 0, 0), [(222, 175), (220, 165), (284, 128), (288, 138)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
