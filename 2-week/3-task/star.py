from turtle import *


def draw_star(needles):
    angle = 90 - (180/needles)
    setheading(angle)
    for _ in range(needles):
        fd(50)
        right(180-angle)
        fd(50)
        left(angle)


draw_star(6)
