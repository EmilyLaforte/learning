import turtle

def octagon():
    for i in range(8):
        turtle.fd(50)
        turtle.rt(45)
def circle():
    for i in range(36):
        turtle.fd(10)
        turtle.rt(10)

###spirograph
##turtle.speed(0)
##for i in range(100):
##    circle()
##    turtle.fd(15)
##    turtle.rt(15)
##    octagon()
##    turtle.fd(15)
##    turtle.rt(15)

#slinky
        
def slinky():
    turtle.speed(0)
    for i in range(20):
        circle()
        turtle.fd(15)

slinky()

