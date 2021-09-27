from random import randint
import turtle

number_of_turtles = 20
steps_of_time_number = 1000

pool = [turtle.Turtle(shape = 'circle') for i in range(number_of_turtles)]
coord = [[randint(-200, 200), randint(-200, 200), randint(-20, 20), randint(-20, 20)] for i in range(number_of_turtles)]

dt = 1

for i in range(number_of_turtles):
    pool[i].penup()
    pool[i].goto(coord[i][0], coord[i][1])

for t in range(steps_of_time_number):
    for i in range(number_of_turtles):
        coord[i][0] += coord[i][2] * dt
        coord[i][1] += coord[i][3] * dt
        if coord[i][0] < -200:
            coord[i][0] = -200
            coord[i][2] *= -1
        if coord[i][0] > 200:
            coord[i][0] = 200
            coord[i][2] *= -1
        if coord[i][1] < -200:
            coord[i][1] = -200
            coord[i][3] *= -1
        if coord[i][1] > 200:
            coord[i][1] = 200
            coord[i][3] *= -1
        pool[i].goto(coord[i][0], coord[i][1])
