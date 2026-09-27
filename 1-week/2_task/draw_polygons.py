from turtle import *


def draw_polygon(n):
    step = 80
    angle = 360 / n
    for _ in range(n):
        forward(step)
        left(angle)


x = -300
for n in [3, 5, 6, 7]:
    pu()
    goto(x, 0)
    pd()
    x += 150
    draw_polygon(n)

done()
