import turtle as t
import random as rd

n = 5
angle = 45

t.penup()
t.goto(-200, 0)
t.pendown()

for i in range(n):
    length = rd.randint(50, 100)

    t.left((180 - angle) / 2)
    t.forward(length)
    t.right(180 - angle)
    t.forward(length)
    t.left((180 - angle) / 2)

t.exitonclick()
