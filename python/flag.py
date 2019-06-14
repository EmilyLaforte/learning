import turtle

def rectangle():
    for i in range(2):
        turtle.fd(50)
        turtle.rt(90)
        turtle.fd(90)
        turtle.rt(90)
    turtle.fd(60)

turtle.width(10)

turtle.color("blue")  
turtle.begin_fill()
for i in range(2):
        turtle.fd(50)
        turtle.rt(90)
        turtle.fd(90)
        turtle.rt(90)
turtle.end_fill()
turtle.fd(50)
turtle.color("black")
rectangle()
turtle.color("red")
turtle.begin_fill()
for i in range(2):
        turtle.fd(50)
        turtle.rt(90)
        turtle.fd(90)
        turtle.rt(90)
turtle.end_fill()
