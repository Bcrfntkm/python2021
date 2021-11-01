import math
from random import randrange as rnd, choice

import pygame


FPS = 30
g = -2
k = -0.01
ax = ay = 0.91
interval = 91

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600

class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 100
        self.vy = -100
        self.color = choice(GAME_COLORS)
        self.live = 30
        self.flag = True

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """

        self.x += self.vx
        self.y -= self.vy + g
        self.vy += g + k * self.vy
        self.vx += k * self.vx
        if abs(self.vy) < 1.3 and abs(self.vx) < 1.3:
            self.flag = False


    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj, wall: tuple):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
            wall: Объект стена, с которым тоже проверяется столкновение
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        vert, hor = wall
        if self.x > hor:
            self.x = hor
            self.vx *= -ax
            self.vy *= ay
        if self.y > vert:
            self.y = vert
            self.vx *= ax
            self.vy *= -ay

        if self.y <= 0:
            self.y = 0
            self.vy *= -ay
            self.vx *= ax
        elif self.x <= 0:
            self.x = 0
            self.vx *= -ax
            self.vy *= ay
        dx = obj.x - self.x
        dy = obj.y - self.y
        min_dist = (obj.r + self.r) ** 2

        dist = dx * dx + dy * dy
        if dist > min_dist:
           return False
        else:
            return True


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 25
        self.f2_on = 0
        self.an = 1
        self.color = GREY

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 25

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        w = 8
        l = self.f2_power
        x = 20
        y = 450
        sin_an = math.sin(self.an)
        cos_an = math.cos(self.an)
        coords = [(x + w * 0.5 * sin_an, y - w * 0.5 * cos_an),
                  (x + w * 0.5 * sin_an + l * cos_an, y - w * 0.5 * cos_an + l * sin_an),
                  (x - w * 0.5 * sin_an + l * cos_an, y + w * 0.5 * cos_an + l * sin_an),
                  (x - w * 0.5 * sin_an, y + w * 0.5 * cos_an)]
        pygame.draw.polygon(screen, self.color, coords)

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
                self.color = RED
            else:
                self.color = GREY


class Target:
    def __init__(self):
        self.points = 0
        self.live = 1
        self.new_target()
        self.shoots = 1

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(2, 50)
        color = self.color = RED
        self.live = 1

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)
target = Target()
finished = False

while not finished:
    interval += 1
    screen.fill(WHITE)
    gun.draw()
    if interval > 90:
        target.draw()
    for b in balls:
        if b.flag:
            b.draw()
        else:
            balls.remove(b)
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for b in balls:
        b.move()
        if b.hittest(target, (HEIGHT-b.r, WIDTH-b.r)) and target.live:
            interval = 0
            target.live = 0
            target.hit()
        elif target.live:
            target.shoots += 1
    if interval == 90:
        target.new_target()
    gun.power_up()

pygame.quit()
