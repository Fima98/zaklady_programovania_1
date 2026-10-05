from turtle import *


def draw_sun(rays, color='black'):
    setheading(0)
    pensize(2)
    pencolor(color)
    for _ in range(rays):
        forward(60)
        backward(60)
        right(360/rays)

    # pensize(25)
    # forward(0)


def draw_stairs(stairs):
    for _ in range(stairs):
        setheading(0)
        pencolor('red')
        pensize(4)
        forward(20)
        left(90)
        forward(20)
        right(90)


def draw_tree(branches):
    pencolor('black')
    pensize(2)
    setheading(270)
    for _ in range(branches):
        left(45)
        forward(40)
        backward(40)

        right(90)
        forward(40)
        backward(40)

        left(45)
        forward(30)
    forward(30)


def draw_linedot(times):
    setheading(0)
    pencolor('black')
    pensize(6)
    for _ in range(times):
        forward(10)
        pu()
        forward(10)
        pd()
        forward(0)
        pu()
        forward(10)
        pd()


def draw_points(times):
    setheading(0)
    pencolor('black')
    pensize(6)
    for _ in range(times):
        forward(0)
        pu()
        forward(10)
        pd()


def draw_all():
    speed(0)
    funcs = [lambda: draw_sun(24), lambda: draw_stairs(
        5), lambda: draw_tree(3), lambda: draw_linedot(7), lambda: draw_points(10), lambda: draw_sun(200, 'red')]

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
