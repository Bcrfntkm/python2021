import pygame
from pygame.draw import *
from random import randint

time = 0
pool = []

print('Choose your level: Elementary(1), Confidence(2), Veteran(3)')
level = input()
levels = {'1': 1.5,
          '2': 1,
          '3': 0.5
          }

quot = levels[level]

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 900))
BLACK = (0, 0, 0)
result = 0

class Ball:
    '''
    Class that makes and moves the balls
    '''
    def __init__(self):
        '''
        Function that put the ball on a random place with random velocity
        '''
        self.coord = [randint(100, 1100), randint(100, 900)]
        self.r = randint(60, 100) * quot
        self.velocity = [randint(-25, 25) / quot, randint(-25, 25) / quot]
        self.color = (randint(0, 254), randint(0, 254), (randint(0, 254)))
        self.flag = True
        self.points = 100//self.r

    def move(self, time):
        '''
        Function that moves the ball
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

class Square:
    '''
    Class that creates the fluctuating square
    '''
    def __init__(self):
        self.r = randint(80, 100) * quot
        self.coord = [randint(100, 1100), randint(100, 900)]
        self.color = (randint(0, 254), randint(0, 254), (randint(0, 254)))
        self.flag = True
        self.points = 200//self.r

    def move(self, time):
        '''
        Function that moves the square
        time: counter of moves
        '''
        if time % (15*quot) == 0:
            self.coord = [randint(100, 1100), randint(100, 900)]

    def draw(self):
        '''
        Function draws the square via its coordinates
        '''
        rect(screen, self.color, [self.coord[0], self.coord[1], self.r, self.r])

    def event(self, event):
        '''
        Function handles the event that a gamer make
        event: here is press of mouse button
        '''
        x0, y0 = self.coord
        pos_x, pos_y = event.pos
        if (abs(x0 + self.r / 2 - pos_x) < self.r) and (abs(y0 + self.r / 2 - pos_y < self.r)):
            self.flag = False

    def collision(self, BORDER_OF_EDGE):
        '''
        Function do nothing as square cannot make a collision
        :param BORDER_OF_EDGE: borders of game window
        '''
        pass


pygame.display.update()
clock = pygame.time.Clock()
finished = False
for _ in range(int(3/quot)):
    pool.append(Ball())
    pool.append(Ball())
    pool.append(Square())

while not finished:
    clock.tick(FPS)

    time += 1

    for var in pool:
        var.move(time)
        var.draw()
        var.collision([1200, 900])
        if time % 5 == 0:
            var.next_move = True

    for event in pygame.event.get():
        for var in pool:
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                var.event(event)
                if not var.flag:
                    pool.pop(pool.index(var))
                    result += var.points
    if not pool:
        finished = True

    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()

result *= 9*FPS/time

print('Enter your name:')
name = input()
print(result)
with open('Results.txt', 'a') as f:
    # Making an entry to the file of the best players
    f.write(level + ' ')
    f.write(name + ' ')
    f.write(str(result) + '\n')

