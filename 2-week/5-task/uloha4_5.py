from turtle import *


def draw_rotating_squares():
    pencolor("blue")
    setheading(270)
    for _ in range(3):
        for _ in range(4):
            forward(50)
            left(90)
        left(120)


def square_grid():
    pencolor("black")
    setheading(0)
    for _ in range(4):
        for _ in range(4):
            forward(50)
            left(90)
        left(90)


def triangle_star():
    pencolor("green")
    setheading(0)
    for _ in range(4):
        for _ in range(3):
            forward(50)
            right(120)
        left(90)


def draw_diagonal_squares():
    pencolor("black")
    setheading(0)
    for _ in range(3):
        for _ in range(4):
            forward(50)
            left(90)
        forward(50)
        left(90)
        forward(50)
        right(90)


def draw_all():
    speed(0)
    funcs = [
        draw_rotating_squares,
        square_grid,
        triangle_star,
        draw_diagonal_squares,
    ]

    x_start, y_start = -250, 100
    x, y = x_start, y_start

    for i, func in enumerate(funcs):
        if i > 0 and i % 2 == 0:
            x = x_start
            y -= 300

        penup()
        goto(x, y)
        pendown()
        func()
        x += 350


draw_all()
hideturtle()
done()
