from turtle import *


def draw_blue_kvadrat():
    pencolor("blue")
    for _ in range(8):
        for _ in range(4):
            forward(25)
            left(90)
        left(45)


def draw_red_kvadrats():
    pencolor("red")
    for _ in range(10):
        for _ in range(4):
            forward(25)
            left(90)
        left(360 / 10)


def draw_green_trojuholnik():
    pencolor("green")
    for _ in range(10):
        for _ in range(3):
            forward(25)
            left(120)
        left(36)


def draw_devatuholnik():
    pencolor("black")
    for _ in range(6):
        for _ in range(9):
            forward(20)
            left(40)
        left(60)


def draw_vyzerunok():
    pencolor("black")
    setheading(60)
    for _ in range(6):
        for _ in range(3):
            forward(15)
            right(60)
            forward(50)
            left(60)
            forward(15)
            left(120)

        left(60)


def draw_all():
    speed(0)
    funcs = [
        draw_blue_kvadrat,
        draw_red_kvadrats,
        draw_green_trojuholnik,
        draw_devatuholnik,
        draw_vyzerunok,
    ]

    x_start, y_start = -200, 100
    x, y = x_start, y_start

    for i, func in enumerate(funcs):
        if i > 0 and i % 3 == 0:
            x = x_start
            y -= 200

        penup()
        goto(x, y)
        pendown()
        func()
        x += 200


draw_all()
hideturtle()
done()
