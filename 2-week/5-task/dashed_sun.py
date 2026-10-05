from dashed_forward import *


def draw_sun_with_vars(radius, ray_length, ray_count):
    setheading(90)
    pencolor('yellow')
    angle = 360/ray_count
    for _ in range(ray_count):
        dashed_forward(ray_length)
        backward(ray_length)
        right(angle)

    pensize(radius)
    forward(0)


draw_sun_with_vars(40, 100, 20)
done()
