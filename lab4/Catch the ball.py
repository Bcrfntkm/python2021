import pygame
from pygame.draw import *
from random import randint

print('Choose your level: Elementary, Confidence, Veteran')
level = str(input())
levels = {'Elementary': 1.5,
          'Confidence': 1,
          'Veteran': 0.5
         }

quot = levels[level]

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 900))
BLACK = (0, 0, 0)
result = 0

class Ball:
    '''
    Class that make and move the balls
    '''
    def __init__(self):
        '''
        Function that put the ball on a random place with random velocity
        '''
        self.coord = [randint(100, 1100), randint(100, 900)]
        self.r = randint(30, 100) * quot
        self.velocity = [randint(-30, 30) / quot, randint(-30, 30) / quot]
        self.color = (randint(0, 254), randint(0, 254), (randint(0, 254)))
        self.flag = True

    def move(self):
        '''
        Function that moves th ball
        '''
        v0_x, v0_y = self.velocity
        self.coord[0] += v0_x
        self.coord[1] += v0_y

    def draw(self):
        '''
        Function draws the ball via its coordinates
        '''
        circle(screen, self.color, (self.coord[0], self.coord[1]), self.r)

    def collision(self, BORDER_OF_EDGE):
        '''
        Function reflect the ball from the window
        :param BORDER_OF_EDGE: borders of game window
        '''
        if self.coord[0] <= 0 or self.coord[0] >= BORDER_OF_EDGE[0]:
            self.velocity[0] *= -1
        if self.coord[1] <= 0 or self.coord[1] >= BORDER_OF_EDGE[1]:
            self.velocity[1] *= -1

    def event(self, event):
        '''
        Function handles the event that a gamer make
        :param event: here is press of mouse button
        '''
        x0, y0 = self.coord
        pos_x, pos_y = event.pos
        if (pos_x-x0)**2 + (pos_y-y0)**2 <= self.r**2:
            self.flag = False


pygame.display.update()
clock = pygame.time.Clock()
finished = False

pool = [Ball(), Ball(), Ball(), Ball(), Ball()]

while not finished:
    clock.tick(FPS)

    for var in pool:
        var.move()
        var.draw()
        var.collision([1200, 900])
    for event in pygame.event.get():
        for var in pool:
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                var.event(event)
                if not var.flag:
                    pool.pop(pool.index(var))
                    result += 100//var.r
    if not pool:
        finished = True

    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()

print('Enter your name:')
name = input()
print(result)
with open('Results.txt', 'a') as f:
    # Making an entry to the file of the best players
    f.write(level + ' ')
    f.write(name + ' ')
    f.write(str(result) + '\n')

