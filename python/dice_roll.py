import turtle
import random

##def dice_roll(width, color, fill):
##    turtle.speed(0)
##    turtle.width(width)
##    turtle.color(color)
##    turtle.fill(fill)
##    turtle.begin_fill()
##    for i in range(4):
##        turtle.fd(100)
##        turtle.rt(90)
##    turtle.end_fill()
##    turtle.pu()
##    d = random.randint(1, 6)
##    turtle.color("white")
##    turtle.goto(27, -100)
##    turtle.write(d, font=("Arial", 60, "bold"))
##
##dice_roll(15, "red", "green")

def dice_roll(width, line_color, fill_color, x, y):
    turtle.pu()
    turtle.goto(x, y)
    turtle.pd()
    turtle.speed(0)
    turtle.width(width)
    turtle.color(line_color, fill_color)
    turtle.begin_fill()
    for i in range(4):
        turtle.fd(100)
        turtle.rt(90)
    turtle.end_fill()
    turtle.pu()
    d = random.randint(1, 6)
    turtle.color("white")
    turtle.goto(x+50, y-100)
    turtle.write(d, font=("", 60, "bold"))
    
dice_roll(15, "red", "green", -480, 400)
dice_roll(15, "turquoise", "purple", 370, 400)

