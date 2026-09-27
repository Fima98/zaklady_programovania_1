from turtle import *


def draw_pentagon():
    pencolor('deepskyblue')
    pensize(2)
    setheading(-20)
    for _ in range(5):
        dot(10, 'deepskyblue')
        forward(75)
        left(360 / 5)


def draw_star():
    pencolor('yellow')
    pensize(3)
    setheading(90)
    for _ in range(5):
        forward(100)
        right(144)


def draw_better_sun():
    setheading(0)
    pensize(2)
    for i in range(36):
        pencolor('brown' if i % 2 == 0 else 'green')
        forward(60)
        backward(60)
        right(10)
    pencolor('white')
    pensize(40)
    forward(0)
    pencolor('yellow')
    pensize(25)
    forward(0)


def draw_snowflake():
    pencolor('blue')
    pensize(2)
    for _ in range(8):
        forward(25)
        dot(10, 'blue')
        forward(25)

        left(45)
        for _ in range(3):
            forward(12)
            dot(10, 'blue')
            backward(12)
            right(45)

        left(90)
        backward(50)
        right(360/8)


def draw_idk_what():
    colors = [
        'red', 'orange', 'yellow', 'green', 'cyan', 'blue',
        'lightskyblue', 'pink', 'magenta', 'purple', 'violet', 'deeppink'
    ]
    pensize(3)
    pencolor('purple')

    for _ in range(4):
        forward(30)
        right(120)
        forward(30)
        right(120)
        forward(30)
        left(150)

    setheading(90)
    for i in range(12):
        pu()
        forward(45)
        pd()
        pencolor(colors[i])
        forward(15)
        backward(15)
        pu()
        backward(45)
        pd()
        right(30)


def draw_triangle_ring():
    pencolor('deepskyblue')
    pensize(2)
    for _ in range(12):
        for _ in range(3):
            forward(25)
            left(120)
        pu()
        circle(45, 360 / 12)
        pd()


def draw_all():
    speed(0)
    funcs = [draw_pentagon, draw_star,
             draw_better_sun, draw_snowflake, draw_idk_what, draw_triangle_ring]

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
