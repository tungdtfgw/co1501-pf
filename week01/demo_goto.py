import turtle as t

t.fillcolor('red')  # set the fill color to red
t.begin_fill()      # start filling the shape
t.goto(0, 100)
t.goto(100, 100)
t.goto(100, 0)
t.goto(0, 0)
t.end_fill()        # end filling the shape

t.penup()          # lift the pen up, so it won't draw
t.goto(200, 0)
t.pendown()        # put the pen down, so it will draw
t.goto(200, 100)
t.goto(300, 100)
t.goto(300, 0)
t.goto(200, 0)

t.exitonclick()