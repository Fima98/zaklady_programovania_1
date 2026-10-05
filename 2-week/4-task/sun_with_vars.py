from turtle import *


def draw_sun_with_vars(radius, ray_length, ray_count):
    setheading(90)
    angle = 360/ray_count
    for _ in range(ray_count):
        forward(ray_length)
        backward(ray_length)
        right(angle)

    pensize(radius)
    forward(0)


def draw_all():
    speed(0)
    suns_data = [
        (20, 50, 8),
        (30, 80, 12),
        (15, 40, 6),
        (40, 100, 16),
        (25, 60, 10),
        (35, 90, 14),
    ]

    x_start, y_start = -300, 200
    x, y = x_start, y_start

    for i, params in enumerate(suns_data):
        if i > 0 and i % 4 == 0:
            x = x_start
            y -= 300

        pu()
        goto(x, y)
        pd()
        draw_sun_with_vars(*params)
        x += 200


draw_all()
done()
