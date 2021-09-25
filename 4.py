import turtle

turtle.shape('turtle')
def f (n):
    angle = 180*(n-2)/n
    return angle

for i in range (100):
    turtle.forward(5)
    turtle.left(180-f(100))

