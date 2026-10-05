from turtle import *


def draw_exponential_squares():
    pencolor("blue")
    setheading(0)
    side = 25
    for _ in range(4):
        for _ in range(4):
            forward(side)
            right(90)
        side *= 2


def draw_growing_triangles():
    pencolor("green")
    setheading(0)
    side = 50
    for _ in range(4):
        for _ in range(3):
            forward(side)
            right(120)
        side += 10


def draw_hexagon_flower():
    pencolor("red")
    setheading(0)
    for _ in range(6):
        forward(50)
        for _ in range(6):
            forward(25)
            right(60)
        backward(50)
        left(60)


def draw_all():
    speed(0)
    funcs = [
        draw_exponential_squares,
        draw_growing_triangles,
        draw_hexagon_flower,
    ]

    x_start, y_start = -300, 0
    x, y = x_start, y_start

    for func in funcs:
        penup()
        goto(x, y)
        pendown()
        func()
        x += 300


draw_all()
hideturtle()
done()
