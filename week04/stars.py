import turtle as t
import random as rd


n = 30
angle = 360 / n

t.speed(0)

for i in range(n):
    length = rd.randint(50, 100)
    t.forward(length)
    t.goto(0, 0)

    t.left(angle)

t.exitonclick()