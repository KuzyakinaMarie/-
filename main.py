import turtle
import math
import random
wn=turtle.Screen()
wn.bgcolor('black')
a=turtle. Turtle()
a.speed(0)
a.color('white')
rotate=int(360)
def drawCircles(t,size):
    for i in range (10):
        t.circle(size)
    size=size - 4
def drawSpecial(t,size,repeat):
    for i in range(repeat):
        drawCircles(t,size)
    t.right (360/repeat)
drawSpecial(a,100,10)
b = turtle.Turtle()
b.speed(0)
b.color('yellow')
rotate = int(90)

def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-10
def drawSpecial(t,size,repeat):
    for i in range(repeat) :
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(b,100,10)
c=turtle.Turtle()
c.speed(0)
c.color('blue')
rotate=int(80)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-5
def drawSpecial(t, size, repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial (c, 100, 10)
d = turtle.Turtle()
d.speed(0)
d.color('orange')
rotate=int(90)

turtle.getscreen()._root.mainloop()