from polygon import draw_polygon, move_next
import turtle as t

def draw_flower(length, n_shapes, n_sides):
    angle = 360 / n_shapes
    for i in range(n_shapes):
        draw_polygon(length, n_sides)
        t.left(angle)

if __name__ == '__main__':
    t.speed(0)
    # draw a flower with 15 triangles
    draw_flower(100, 15, 3)
    move_next(200)

    # draw a flower with 10 squares
    draw_flower(50, 10, 4)

    t.exitonclick()