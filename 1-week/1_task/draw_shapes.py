from turtle import *
from time import sleep


def rounded_stick():
    setheading(270)
    pencolor('green')
    pensize(30)
    forward(100)
    pencolor('white')
    pensize(20)
    backward(100)


def snowman():
    setheading(270)
    pencolor('blue')
    pensize(30)
    forward(0)
    pu()
    forward(40)
    pd()
    pensize(50)
    forward(0)
    pu()
    forward(75)
    pd()
    pensize(100)
    forward(0)


def moon():
    setheading(0)
    pencolor('blue')
    pensize(80)
    forward(0)
    pu()
    forward(20)
    pd()
    pencolor('white')
    pensize(80)
    forward(0)


def draw_eight(pen_size=10, pen_color='green'):
    pu()
    backward(25)
    left(90)
    forward(50)
    pd()

    pencolor(pen_color)
    pensize(pen_size)
    setheading(0)
    forward(50)
    right(90)
    forward(100)
    right(90)
    forward(50)
    right(90)
    forward(100)

    backward(50)
    right(90)
    forward(50)

    pu()
    backward(25)
    setheading(0)
    pd()


def draw_neon():
    pencolor('black')
    pensize(200)
    forward(0)
    draw_eight(10, 'green')
    draw_eight(5, '#90EE90')


def target():
    sizes = [('black', 120), ('red', 95), ('blue', 70), ('yellow', 45)]
    for color_name, size in sizes:
        pencolor(color_name)
        pensize(size)
        forward(0)


def brown_ball():
    setheading(45)
    pencolor('brown')
    pensize(80)
    forward(20)

    pu()
    pencolor('white')
    pensize(15)
    backward(60)
    pd()
    forward(100)


def cross():
    setheading(270)
    pencolor('black')
    pensize(25)
    forward(100)
    backward(70)
    left(90)
    forward(35)
    backward(70)

    pu()
    forward(35)
    left(90)
    forward(30)
    setheading(270)
    pd()
    pencolor('yellow')
    pensize(10)
    forward(100)
    backward(70)
    left(90)
    forward(35)
    backward(70)


def draw_all():
    speed(0)
    funcs = [rounded_stick, snowman, moon,
             draw_neon, target, brown_ball, cross]

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
