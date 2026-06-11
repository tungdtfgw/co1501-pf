import turtle as t

# go forward 100 units
length = 5
n = 100
angle = 360 / n

for i in range(n):
    t.forward(length)
    t.left(angle)

t.exitonclick()