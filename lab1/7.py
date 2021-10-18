import turtle

turtle.shape('classic')
turtle.speed(500)
i=0
while True:
    turtle.forward(0.2+i/1000)
    turtle.left(1)
    turtle.speed(500+i*10)
    i+=1
