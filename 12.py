import turtle as t

t.shape('classic')

def f(r):
    for i in range (90):
        t.forward(r)
        t.right(180-180*(180-2)/180)
t.left(90)
t.penup()
t.goto(-400,0)
t.pendown()
t.speed(1000)

for j in range (5):
    f(2)
    f(0.5)
    
