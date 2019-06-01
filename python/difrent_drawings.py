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
def cat():
    turtle.goto(0, 0)
    turtle.seth(0)
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


def circle2(fd_val):
    for i in range(36):
        turtle.lt(10)
        turtle.fd(fd_val)

def circleflower(fd_val, width, color):
    turtle.width(width)
    turtle.color(color)
    for i in range(24):
        turtle.rt(15)
        circle2(fd_val)

def two_color_flower():
    turtle.goto(0, 0)
    turtle.seth(0)
    turtle.speed(0)
    turtle.tracer(0, 0)

    circleflower(9, 12, "yellow")

    circleflower(10, 6, "orange")

    circleflower(10, 1, "black")

    circleflower(6, 4, "red")

    circleflower(6, 1, "black")

    turtle.update()


#Peacock gear
def square(fd_val, color, width):
    turtle.color(color)
    turtle.width(width)
    for i in range(4):
        turtle.rt(90)
        turtle.fd(fd_val)

def circle3(fd_val, line_color, fill_color, width):
    turtle.color(line_color, fill_color)
    turtle.width(width)
    for i in range(36):
        turtle.rt(10)
        turtle.fd(fd_val)

def circle_flower():
    turtle.goto(0, 0)
    turtle.seth(0)
    turtle.speed(0)
    turtle.tracer(0, 0)
    for i in range(240):
        square(400, "blue", 15)
        square(350, "green", 15)
        square(250, "purple", 15)
        circle3(9,"brown", "brown", 50)
        turtle.lt(5)
        turtle.update()

def blank():
    turtle.home()
    turtle.color("white")
    turtle.width(100000)
    turtle.fd(0.1)
    turtle.width(3)
    turtle.color("black")

turtle.onkey(cat, "c")
turtle.onkey(blank, "s")
turtle.onkey(two_color_flower, "t")
turtle.onkey(circle_flower, "p")


turtle.listen()

