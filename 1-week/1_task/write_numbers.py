from turtle import *


coord_x = -200
step = 100


def move_to_the_right():
    pu()
    global coord_x
    coord_x += step
    goto(coord_x, 0)
    setheading(0)
    pd()


def draw_0():
    forward(50)
    right(90)
    forward(100)
    right(90)
    forward(50)
    right(90)
    forward(100)
    right(90)


def draw_2():
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)


def draw_9():
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(100)
    right(90)
    forward(50)


def write_numbers():
    pu()
    goto(coord_x, 0)
    pd()

    draw_2()
    move_to_the_right()
    draw_2()
    move_to_the_right()
    draw_0()
    move_to_the_right()
    draw_9()


pensize(2)
write_numbers()
done()
