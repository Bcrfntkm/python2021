import turtle as tl

tl.shape('turtle')

def circ_left(n):
    for i in range(n):
        tl.forward(10)
        tl.left(180-180*(n-2)/n)

def circ_right(n):
    for i in range(n):
        tl.forward(10)
        tl.right(180-180*(n-2)/n)

for i in range (3):
    circ_left(100)
    circ_right(100)
    tl.left(60)

    
