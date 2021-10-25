from random import *
import turtle as t
import math as m

t.shape('turtle')
t.color('green')
t.speed(30)
a = int(input())    #границы выбора шага черепашки
b = int(input())

for i in range(10000):
    t.forward(randint(a,b))
    t.left(360*random())
    
