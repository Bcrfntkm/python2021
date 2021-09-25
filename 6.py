import turtle

turtle.shape('triangle')
n = int(input())
for i in range(n):
    turtle.forward(100)
    turtle.stamp()
    turtle.backward(100)
    turtle.left(360/n)
