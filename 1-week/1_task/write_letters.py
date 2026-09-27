from turtle import *
from time import sleep


def write_l():
    setheading(270)
    forward(100)
    left(90)
    forward(50)


def write_e():
    for _ in range(2):
        forward(50)
        backward(50)
        right(90)
        forward(50)
        left(90)
    forward(50)


def write_h():
    setheading(270)
    forward(100)
    backward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    backward(100)


def write_k():
    setheading(270)
    forward(100)
    backward(50)
    setheading(45)
    forward(70)
    backward(70)
    setheading(315)
    forward(70)


def write_m():
    setheading(90)
    forward(100)
    right(150)
    forward(58)
    left(120)
    forward(58)
    right(150)
    forward(100)


pencolor('black')
pensize(2)

for func in [write_l, write_e, write_h, write_k, write_m]:
    reset()
    func()
    sleep(1)
done()
