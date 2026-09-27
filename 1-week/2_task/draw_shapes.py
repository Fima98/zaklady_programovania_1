from turtle import *


def draw_sun():
    angle = 360/9
    setheading(90)

    for _ in range(9):
        pencolor('orange')
        pensize(4)
        forward(50)
        backward(50)
        right(angle)

    pencolor('yellow')
    pensize(30)
    forward(0)


def draw_stairs():
    for _ in range(5):
        setheading(0)
        pencolor('red')
        pensize(4)
        forward(20)
        left(90)
        forward(20)
        right(90)


def draw_lekaren():
    setheading(90)
    pensize(4)
    pencolor('green')
    for _ in range(4):
        forward(30)
        right(90)
        forward(30)
        right(90)
        forward(30)
        left(90)


def ouroboros():
    angle = 360/10
    setheading(0)
    pencolor('red')
    for _ in range(10):
        pensize(20)
        forward(10)
        pu()
        right(angle)
        forward(12)
        pd()


def draw_tree():
    pencolor('gray')
    pensize(2)
    setheading(270)
    for _ in range(3):
        left(45)
        forward(20)
        backward(20)

        right(90)
        forward(20)
        backward(20)

        left(45)
        forward(30)
    forward(30)


def draw_endoparasite():
    pencolor('green')
    pensize(5)
    setheading(0)
    for _ in range(6):
        left(90)
        forward(25)
        right(90)
        forward(25)
        right(90)
        forward(25)
        left(90)
        forward(25)


def draw_all():
    speed(0)
    funcs = [draw_sun, draw_stairs, draw_lekaren,
             ouroboros, draw_tree, draw_endoparasite]

    x_start, y_start = -300, 200
    x, y = x_start, y_start

    for i, func in enumerate(funcs):
        if i > 0 and i % 4 == 0:
            x = x_start
            y -= 300

        pu()
        goto(x, y)
        pd()
        func()
        x += 200


draw_all()
done()
