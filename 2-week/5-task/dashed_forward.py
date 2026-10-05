from turtle import *


def dashed_forward(distance, dash_len=10, gap_len=5):
    step = dash_len + gap_len
    steps = int(distance // step)
    for _ in range(steps):
        pd()
        fd(dash_len)
        pu()
        fd(gap_len)

    remainder = distance % step
    if remainder > 0:
        pd()
        fd(min(remainder, dash_len))
        pu()
        if remainder > dash_len:
            fd(remainder - dash_len)
