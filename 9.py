import turtle
import math as np

turtle.shape('classic')
x = 20
s = 20
v = 3

def f (n):
    turtle.left(180-90*(n-2)/n)
    for i in range (n):
        turtle.forward(s)
        turtle.left(180-180*(n-2)/n)
    turtle.right(180-90*(n-2)/n)

for i in range(10):
    f (v)
    turtle.penup()
    turtle.goto(x,0)
    turtle.pendown()
    x += 20
    s = (s/(2*np.sin(np.pi/v))+20)*2*np.sin(np.pi/(v+1))
    v += 1
