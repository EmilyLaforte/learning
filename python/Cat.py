import turtle



#Cat

def circle(fd_val, line_color, fill_color, width):
    turtle.color(line_color, fill_color)
    turtle.width(width)
    for i in range(36):
        turtle.rt(10)
        turtle.fd(fd_val)
        
def triangle(fd_val, line_color, fill_color):
    turtle.color(line_color, fill_color)
    for i in range(3):
        turtle.rt(120)
        turtle.fd(fd_val)

turtle.speed(0)
turtle.begin_fill()
circle(25, "black", "grey", 5)
turtle.end_fill()
turtle.pu()
turtle.goto(-115, -35)
turtle.pd()
turtle.begin_fill()
triangle(120, "black", "grey")
turtle.end_fill()
turtle.pu()
turtle.goto(100, 60)
turtle.lt(35)
turtle.pd()
turtle.begin_fill()
triangle(120, "black", "grey")
turtle.end_fill()
turtle.pu()
turtle.goto(-100, -110)
turtle.pd()
turtle.begin_fill()
circle(7, "black", "black", 10)
turtle.end_fill()
turtle.pu()
turtle.goto(30, -80)
turtle.pd()
turtle.begin_fill()
circle(7, "black", "black", 10)
turtle.end_fill()
turtle.pu()
turtle.goto(-15, -175)
turtle.lt(35)
turtle.pd()
turtle.begin_fill()
triangle(4, "black", "grey")
turtle.end_fill()
turtle.pu()
turtle.goto(70, -200)
turtle.rt(5)
turtle.pd()
def whisker():
    for i in range(3):
        turtle.fd(50)
        turtle.backward(50)
        turtle.rt(35)
whisker()
turtle.pu()
turtle.goto(-90, -220)
turtle.lt(200)
turtle.pd()
def whisker():
    for i in range(3):
        turtle.fd(50)
        turtle.backward(50)
        turtle.lt(35)
whisker()
turtle.pu()
turtle.goto(-440, 300)
turtle.color("black")
turtle.write("Cat", font=("Roboto", 60, "bold"))
