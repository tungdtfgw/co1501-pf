import turtle as t

def draw_square(length):
    for i in range(4):
        t.forward(length)
        t.left(90)


draw_square(100)

t.penup()
t.forward(200)
t.pendown()

draw_square(50)

t.exitonclick()