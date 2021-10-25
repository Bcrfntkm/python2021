import turtle as t
with open('Python.txt','r') as f:
    b = []
    for line in f:
        a = eval(line)
        b.append(a)
        
index=[1,4,1,7,0,0]   # индекс по цифрам заносится в соответсвующий массив
x = 0
y = 0
for number in index:
    list_coords = b[number]
    start = list_coords[0]
    t.penup()
    vert,hor = list_coords[0]
    x += hor
    y += vert
    t.goto(x,y)
    t.pendown()
    for coords in list_coords[1:-1]:
        s,a = coords
        t.forward(s)
        t.left(a)
    t.penup()
    finish = list_coords[-1]
    vert,hor = finish
    x += hor
    y += vert
    t.goto(x,y)
    
