import turtle as t

t.shape('classic')
t.color('black','yellow')
t.speed(100)

def f(s):
    for i in range(180):
        t.forward(s)
        t.left(180-180*(180-2)/180)
t.begin_fill()
f(5)
t.end_fill()
t.color('blue')
t.penup()
t.goto(-55,170)
t.pendown()
t.begin_fill()
f(0.75)
t.end_fill()
t.penup()
t.goto(55,170)
t.pendown()
t.begin_fill()
f(0.75)
t.end_fill()
t.penup()
t.goto(0,170)
t.width(10)
t.pendown()
t.right(90)
t.color('black')
t.forward(50)
t.penup()
t.goto(-85,115)
t.pendown()
t.color('red')

for j in range(90):
    t.forward(3)
    t.left(180-180*(180-2)/180)

