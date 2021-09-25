import turtle

turtle.shape('turtle')
a = 10
x = -10
y = -10
for i in range(10):
    for j in range(4):
        turtle.forward(a)
        turtle.left(90)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    x -= 10
    y -= 10
    a += 20
