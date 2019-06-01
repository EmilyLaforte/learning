import turtle

###1
##
##turtle.color("yellow")
##for i in range(3):
##    turtle.fd(100)
##    turtle.rt(90)
##
##turtle.fd(50)
##
##turtle.color("blue")
##for i in range(4):
##    turtle.fd(50)
##    turtle.rt(90)
##
###2
##
##for i in range(4):
##    turtle.color("red")
##    turtle.fd(50)
##    turtle.color("blue")
##    turtle.fd(50)
##    turtle.rt(90)
##
###3
##
##for i in range(4):
##    turtle.color("orange")
##    turtle.fd(50)
##    turtle.rt(90)
##
##turtle.lt(90)
##
##for i in range(4):
##    turtle.color("green")
##    turtle.fd(50)
##    turtle.lt(90)
##
###4
##
##turtle.color("black")
##turtle.lt(90)
##turtle.fd(50)
##turtle.rt(90)
##turtle.fd(25)
##turtle.rt(90)
##turtle.fd(50)
##turtle.color("grey")
##turtle.fd(50)
##turtle.rt(90)
##turtle.fd(25)
##turtle.rt(90)
##turtle.fd(50)
##
###5
##
##turtle.color("pink")
##turtle.lt(90)
##turtle.fd(75)
##turtle.rt(90)
##turtle.fd(50)
##turtle.rt(90)
##turtle.fd(50)
##turtle.lt(90)
##turtle.fd(50)
##turtle.lt(90)
##turtle.fd(50)
##turtle.rt(90)
##turtle.fd(50)
##turtle.rt(90)
##turtle.fd(150)
##turtle.rt(90)
##turtle.fd(50)
##turtle.rt(90)
##turtle.fd(50)
##turtle.lt(90)
##turtle.fd(50)
##turtle.lt(90)
##turtle.fd(50)
##turtle.rt(90)
##turtle.fd(50)
##turtle.rt(90)
##turtle.fd(150)

###Circle flower
##
##def circle():
##    for i in range(36):
##        turtle.fd(10)
##        turtle.rt(10)
##
##def  circle_flower():
##    turtle.speed(0)
##    turtle.trace(0, 0)
##    turtle.update
##    for i in range(24):
##        turtle.width(25)
##        turtle.color("orange")
##        circle()
##        turtle.rt(15)
##        turtle.width(20)
##        turtle.color("red")
##        circle()
##        turtle.rt(15)
##        turtle.width(15)
##        turtle.color("blue")
##        circle()
##        turtle.rt(15)
##        turtle.width(5)
##        turtle.color("yellow")
##        circle()
##        turtle.rt(15)
##        turtle.width(10)
##        turtle.color("green")
##        circle()
##        turtle.rt(15)
##        turtle.width(15)
##        turtle.color("purple")
##        circle()
##        turtle.rt(15)
##        turtle.width(20)
##        turtle.color("pink")
##        circle()
##        turtle.rt(15)
##        turtle.width(25)
##        turtle.color("turquoise")
##        circle()
##        turtle.rt(15)
##
##circle_flower()

#Double color circle_flower

def circle1():
    turtle.color("orange")
    turtle.width(10)
    for i in range(24):
        for i in range(36):
            turtle.fd(10)
            turtle.rt(10)
        turtle.rt(15)

turtle.speed(0)
turtle.tracer(0, 0)
circle1()

def circle2():
    turtle.color("green")
    turtle.width(6)
    for i in range(24):
        for i in range(36):
            turtle.fd(6)
            turtle.rt(10)
        turtle.rt(15)
        
circle2()

def circle3():
    turtle.color("black")
    turtle.width(5)
    for i in range(24):
        for i in range(36):
            turtle.fd(10)
            turtle.rt(10)
        turtle.rt(15)

circle3()

def circle4():
    turtle.color("black")
    turtle.width(3)
    for i in range(24):
        for i in range(36):
            turtle.fd(6)
            turtle.rt(10)
        turtle.rt(15)

circle4()
turtle.update()
