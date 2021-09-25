import turtle as t

t.shape('classic')
n = int(input())     #решено для общего случая
a = 135*(n-2)/n-45
b = 90-90*(n-2)/n

def f (n):
    for i in range (n):
        t.right(180-b)
        t.forward(200)
t.right(180-a)

f(n)
