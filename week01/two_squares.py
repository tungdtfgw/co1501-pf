import turtle as t

# draw first square
t.forward(100)
t.left(90)          # turn left 90 degrees
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)

# moving to the position for the second square
t.left(90)
t.penup()          # lift the pen up, so it won't draw
t.forward(200)     # move forward 200 units
t.pendown()        # put the pen down, so it will draw

# draw second square
t.forward(100)
t.left(90)          
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)

# wait for the user to click on the window before closing it
t.exitonclick()