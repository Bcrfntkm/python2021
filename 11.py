import turtle as t
import math as m

t.shape('circle')
t.speed(3000)
r=0.5

def f(s):
    for i in range(180):
        t.forward(s)
        t.left(180-180*(180-2)/180)
    for i in range(180):
        t.forward(s)
        t.right(180-180*(180-2)/180)
t.left(90)

for j in range(10):
    f(r)
    r = (r/(2*m.sin(m.pi/180))+10)*2*m.sin(m.pi/180)
