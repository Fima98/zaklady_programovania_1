from turtle import *
from time import sleep

# tracer(0)
hideturtle()


def stvorec(a=100):
    for i in range(4):
        fd(a)
        rt(90)


def reset():
    clear()
    penup()
    home()
    pendown()
    pensize(1)
    pencolor("black")


def draw_house():
    stvorec()
    lt(60)
    fd(100)
    rt(120)
    fd(100)


def draw_red_squares_thin():
    pencolor("red")
    pensize(2)
    for _ in range(8):
        fd(60)
        stvorec(60)
        bk(60)
        lt(45)


def draw_red_kvadrats():
    pencolor("red")
    pensize(5)
    for _ in range(10):
        stvorec(80)
        left(360 / 10)


def draw_blue_kvadrat():
    pencolor("blue")
    pensize(5)
    for _ in range(8):
        stvorec(80)
        left(45)


def draw_triangle():
    for _ in range(3):
        fd(140)
        stvorec(70)
        rt(120)


def draw_cross():
    for _ in range(4):
        lt(90)
        stvorec(65)
        rt(90)
        fd(130)
        rt(90)


def trojuholnik(a=30):
    for i in range(3):
        fd(a)
        rt(120)


def slnko():
    for i in range(24):
        trojuholnik(20)
        fd(20)
        lt(360 / 24)


def veniec():
    for i in range(20):
        lt(90)
        trojuholnik(30)
        rt(90)
        pu()
        fd(28)
        pd()
        lt(360 / 20)


for draw in (draw_house, draw_red_squares_thin, draw_red_kvadrats,
             draw_blue_kvadrat, draw_triangle, draw_cross, slnko, veniec):
    reset()
    draw()
    update()
    sleep(1.5)

done()
