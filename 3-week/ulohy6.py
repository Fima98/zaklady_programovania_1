from turtle import *
from time import sleep

tracer(0)
hideturtle()


def go(x, y):
    penup()
    goto(x, y)
    pendown()


def bodka(size, color):
    old_size, old_color, was_down = pensize(), pencolor(), isdown()
    pensize(size)
    pencolor(color)
    pendown()
    fd(0)
    pensize(old_size)
    pencolor(old_color)
    if not was_down:
        penup()


def tree():
    pensize(10)
    pencolor("brown")
    go(0, -100)
    goto(0, 0)
    bodka(100, "green")


def flower():
    penup()
    for i in range(6):
        goto(0, 0)
        setheading(i * 60)
        forward(24)
        bodka(26, "purple")
    goto(0, 0)
    bodka(30, "yellow")


def square():
    pensize(2)
    pencolor("black")
    go(-50, -50)
    setheading(0)
    for i in range(4):
        bodka(20, "black")
        forward(100)
        left(90)


def decagon():
    pensize(1)
    pencolor("blue")
    go(-30, -92)
    setheading(0)
    for i in range(10):
        bodka(15, "blue")
        forward(60)
        left(36)


def radial():
    pensize(1)
    for i in range(12):
        go(0, 0)
        setheading(i * 30)
        pencolor("green")
        forward(120)
        bodka(14, "purple")

        pencolor("purple")
        left(30)
        forward(30)
        bodka(14, "purple")
        backward(30)
        right(60)
        forward(30)
        bodka(14, "purple")


for draw in (tree, flower, square, decagon, radial):
    clear()
    draw()
    update()
    sleep(1.5)

done()
