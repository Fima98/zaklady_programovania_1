from dashed_forward import *


def draw_square():
    setheading(0)
    for _ in range(4):
        dashed_forward(100)
        rt(90)


draw_square()
done()
