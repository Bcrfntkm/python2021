import math
from random import randrange as rnd, choice
import pygame
from pygame.locals import *
import time

pygame.font.init()

FPS = 30
g = -2
k = -0.02
ax = ay = 0.91
session_time = 0
time_limit = 30 * FPS  # ограничение игры по времени

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600

PixSpeed = int(WIDTH / 0.266 / FPS)


class Ball:
    def __init__(self, screen: pygame.Surface, SN, x, y, GunSpeedX, GunSpeedY):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        screen - экран, на котором происходит отрисовка событий
        SN - номер шарика, которым поразили цель
        GunSpeedX - скорость пушки по горизонтали
        GunSpeedY - скорость пушки по вертикали
        """
        self.screen = screen
        self.x = x  # 40
        self.y = y  # 450
        self.r = 10
        self.vx = PixSpeed + GunSpeedX  # 100
        self.vy = -(PixSpeed + GunSpeedY)  # -100
        self.color = choice(GAME_COLORS)
        self.live = 30
        self.pause = FPS  # пауза перед удалением объекта
        self.SN = SN

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

    def draw(self):
        """
        Функция создает шарик-пулю
        """
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r)

    def walltest(self, wall: tuple):
        """Функция проверяет сталкивалкивается ли данный обьект со стенами.

        Args:
            wall: координаты стен
        """
        r = self.r
        vert = wall[0] - r
        hor = wall[1] - r
        if self.x > hor:
            self.x = hor
            self.vx *= -ax
            self.vy *= ay
        if self.y > vert:
            self.y = vert
            self.vx *= ax
            self.vy *= -ay

        if self.y <= r:
            self.y = r
            self.vy *= -ay
            self.vx *= ax
        elif self.x <= r:
            self.x = r
            self.vx *= -ax
            self.vy *= ay

    def TestSpeed(self):
        """
        Проверка,остановился ли шарик и надо ли его удалять
        """
        if (self.vy * self.vy + self.vx * self.vx) ** 0.5 < 1.5:
            if self.pause > 0:
                self.pause -= 1
        else:
            self.pause = FPS
        return self.pause == 0


class Gun:
    """
    Класс определяет объект пушка, который может двигаться и стреляет по различного вида мишеням.
    """

    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 25
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.SN = 1
        #    начальные координаты пистолета
        self.x = 20
        self.y = 450
        #    начальная скорость пистолета
        self.Vx = 0
        self.Vy = 0

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        if self.f2_on:
            global balls
            new_ball = Ball(self.screen, self.SN, self.x, self.y, self.Vx, self.Vy)
            self.SN += 1
            new_ball.r += 5
            self.an = math.atan2((event.pos[1] - new_ball.y), (event.pos[0] - new_ball.x))
            new_ball.vx = self.f2_power * math.cos(self.an)
            new_ball.vy = - self.f2_power * math.sin(self.an)
            balls.append(new_ball)

        self.f2_on = 0
        self.f2_power = 25

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event.pos[0] != self.x:
            self.an = math.atan((event.pos[1] - self.y) / (event.pos[0] - self.x))
        else:
            self.an = math.atan((event.pos[1] - 450))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        """
        Изменение вида пушки в зависимости от положения мышки
        """
        w = 8
        l = self.f2_power
        x = self.x
        y = self.y
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

    # обрабатываем события мыши для пистолета

    def handle_event(self, event):
        if event.type == MOUSEMOTION:
            self.targetting(event)
        elif event.type == MOUSEBUTTONDOWN:
            self.fire2_start(event)
        elif event.type == MOUSEBUTTONUP:
            self.fire2_end(event)
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                self.x -= 3
            elif event.key == K_RIGHT:
                self.x += 3
            elif event.key == K_UP:
                self.y -= 3
            elif event.key == K_DOWN:
                self.y += 3


class Target:
    """
    Статичная мишень.
    """
    def __init__(self):
        self.points = 0
        self.live = 1
        self.SN = 0
        self.new_target()
        self.TextPause = FPS * 3

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(650, 770)
        y = self.y = rnd(300, 570)
        r = self.r = rnd(10, 30)
        color = self.color = RED
        self.live = 1

    def hit(self, points=1):
        """
        Попадание шарика в цель.
        """
        self.points += points

    def hittest(self, obj):
        """
        Проверка на столкновение шарика и мишени.
        ARGS:
            obj - шарик-пуля, с которым проверяется столкновение
        """
        if self.live == 0:
            return False
            # расстояние между центрами цели и шарика
        dx = obj.x - self.x
        dy = obj.y - self.y
        min_dist = (obj.r + self.r) ** 2

        dist = dx * dx + dy * dy
        return dist <= min_dist

    def draw(self):
        """
        Функция отвечает за прорисовку статичного шарика и за вывод сообщения на экран о количестве выстрелов,
        за которое были сбиты мишени.
        """
        if self.live == 1:
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)
            self.TextPause = FPS * 3
        elif m_target.live == 0:
            shoots = max(self.SN, m_target.SN)
            T2 = 'Цели поражены за ' + str(shoots) + ' выстрел'
            if shoots == 2 or shoots == 3 or shoots == 4:
                T2 += 'а'
            elif shoots != 1:
                T2 += 'ов'
            Text2 = f1.render(T2, True, BLACK)
            RectObj = Text2.get_rect()
            RectObj.center = (WIDTH / 2, HEIGHT / 2)
            screen.blit(Text2, RectObj)
            gun.SN = 1

            if self.TextPause > 0:
                self.TextPause -= 1
            if self.TextPause == 0:
                target.new_target()
                m_target.new_target()


class Moving_Target(Target):
    """
    Класс, наследуемый от Target. Отвечает за подвижную мишень.
    """

    def __init__(self):
        super().__init__()
        self.vy = 5

    def new_target(self):
        """
        Инициализация новой цели.
        Отличается от родительской другим коридором значений, где может появиться.
        """
        r = self.r = rnd(10, 30)
        x = self.x = rnd(500, 650 - target.r - self.r)
        y = self.y = rnd(300, 550)
        color = self.color = BLUE
        self.live = 1

    def hit(self, points=2):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        """
        Прорисовка шарика и его движения(чтобы не плодить лишнюю функцию move).
        """
        if self.live == 1:
            self.y += self.vy
            if HEIGHT - 30 <= self.y or self.y <= 30:
                self.vy *= -1
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)
            self.TextPause = FPS * 3
        else:
            pass


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

Text2Pause = FPS * 3
bullet = 0  # количество пуль
balls = []  # массив для хранения объектов-шариков

clock = pygame.time.Clock()
gun = Gun(screen)
target = Target()
m_target = Moving_Target()
finished = False
f1 = pygame.font.SysFont('Tahoma', 20)

while not finished:
    screen.fill(WHITE)

    Text1 = f1.render(str(target.points + m_target.points), True, BLACK)
    points = target.points + m_target.points
    screen.blit(Text1, (10, 10))

    gun.draw()
    target.draw()
    m_target.draw()
    session_time += 1

    for b in balls:
        b.draw()

    clock.tick(FPS)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or session_time >= time_limit:
            finished = True
        if target.live == 1 or m_target.live == 1:
            gun.handle_event(event)

    for b in balls:
        b.move()
        b.walltest((HEIGHT, WIDTH))
        if target.hittest(b):
            target.live = 0
            target.SN = b.SN
            target.hit()
        if m_target.hittest(b):
            m_target.live = 0
            m_target.SN = b.SN
            m_target.hit()
        if b.TestSpeed():
            balls.remove(b)
            del b
    gun.power_up()

text = 'Print your name: '
font = pygame.font.SysFont(None, 48)
img = font.render(text, True, RED)
rect = img.get_rect()
rect.topleft = (20, 20)
cursor = Rect(rect.topright, (3, rect.height))
running = True
background = GREY
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                running = False
        if event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                if len(text) > 0:
                    text = text[:-1]
            else:
                text += event.unicode
            img = font.render(text, True, RED)
            rect.size = img.get_size()
            cursor.topleft = rect.topright
    screen.fill(background)
    screen.blit(img, rect)
    if time.time() % 1 > 0.5:
        pygame.draw.rect(screen, RED, cursor)
    pygame.display.update()

for b in balls:
    del b
del target
del m_target
del gun
pygame.quit()
name = text[17:-1]
with open('Results.txt', 'a') as f:
    # Making an entry to the file of the best players
    f.write("{} {}\n".format(name, points))
