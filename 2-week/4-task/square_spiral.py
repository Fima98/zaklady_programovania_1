from turtle import *
from time import sleep


def draw_spiral(step_func=lambda i: i, angle=90, n=50):
    setheading(270)
    for i in range(1, n + 1):
        fd(step_func(i))
        rt(angle)


demos = [
    ("i (standard)", lambda i: i, 90, 50),
    ("i + 50", lambda i: i + 50, 90, 20),
    ("i * 2", lambda i: i * 2, 90, 50),
    ("i ** 2 (quadratic)", lambda i: i**2, 90, 16),
    ("i * 1.5, angle 120°", lambda i: i * 1.5, 120, 50),
    ("i * 1.5, angle 80°", lambda i: i * 1.5, 80, 50),
    ("i * 1.5, angle 70°", lambda i: i * 1.5, 70, 50),
    ("i * 1.5, angle 60°", lambda i: i * 1.5, 60, 50),
    ("i * 1.5, angle 50°", lambda i: i * 1.5, 50, 50),
]

hideturtle()

for title, func, angle, n in demos:
    tracer(0)
    clear()

    pu()
    goto(0, 250)
    write(f"Mode: {title}", align="center", font=("Arial", 14, "bold"))
    goto(0, 0)
    pd()

    draw_spiral(func, angle, n)
    update()

    sleep(0.5)

done()
