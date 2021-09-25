import turtle

turtle.shape('turtle')
x=10
y=5
turtle.speed(20)
for i in range(32):
    turtle.forward(x)
    turtle.left(90)
    x+=y
    
