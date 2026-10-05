from turtle import *


def draw_dots():
    radius = 10
    pencolor('purple')
    setheading(0)
    pensize(5)
    for _ in range(10):
        forward(50)
        pensize(radius)
        forward(0)
        pensize(5)
        radius += 5


draw_dots()
done()
