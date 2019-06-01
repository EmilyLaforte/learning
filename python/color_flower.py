import turtle

def circle(fd_val):
    for i in range(36):
        turtle.lt(10)
        turtle.fd(fd_val)

def circleflower(fd_val, width, color):
    turtle.width(width)
    turtle.color(color)
    for i in range(24):
        turtle.rt(15)
        circle(fd_val)

def two_color_flower():
    turtle.speed(0)
    turtle.tracer(0, 0)

    circleflower(9, 12, "yellow")

    circleflower(10, 6, "orange")

    circleflower(10, 1, "black")

    circleflower(6, 4, "red")

    circleflower(6, 1, "black")

    turtle.update()

two_color_flower()
