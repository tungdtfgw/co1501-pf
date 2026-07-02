import turtle as t

def draw_polygon(length, n):
    angle = 360 / n
    for i in range(n):
        t.forward(length)
        t.left(angle)

def move_next(length):
    t.penup()
    t.forward(length)
    t.pendown()

if __name__ == '__main__':
    # draw a triangle
    draw_polygon(50, 3)
    move_next(150)
    # draw a square
    draw_polygon(50, 4)
    move_next(150)
    # draw a pentagon
    draw_polygon(50, 5)

    t.exitonclick()

