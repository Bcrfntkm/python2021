import turtle
import time

x = -400
y = 0
vx = 40
vy = 100
dt = 0.1
g = -9.8
ay = 0.95
ax = 0.95
k = -0.05

turtle.shape('circle')
turtle.speed(1000)
turtle.goto(1000, 0)
turtle.goto(-1000, 0)
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.speed(200)

while True:
    x += vx * dt
    y += vy * dt + g * dt ** 2 / 2
    vy += g * dt + k * vy * dt
    vx += k * vx * dt

    if y <= 0:
        y = 0
        vy *= -ay
        vx *= ax
    turtle.goto(x, y)