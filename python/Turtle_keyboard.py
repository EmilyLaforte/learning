import turtle
turtle.pensize(5)

def drawUp():
    turtle.seth(90)
    turtle.fd(20)

def drawDown():
    turtle.seth(270)
    turtle.fd(20)

def drawLeft():
    turtle.seth(180)
    turtle.fd(20)

def drawRight():
    turtle.seth(0)
    turtle.fd(20)

def drawUpRight():
    turtle.seth(45)
    turtle.fd(28.3)

def drawUpLeft():
    turtle.seth(135)
    turtle.fd(28.3)

def drawDownRight():
    turtle.seth(315)
    turtle.fd(28.3)

def drawDownLeft():
    turtle.seth(180 + 45)
    turtle.fd(28.3)

def setRed():
    turtle.color("red")

def setGreen():
    turtle.color("green")

def setTurquoise():
    turtle.color("turquoise")

turtle.onkey(drawUp, "k")
turtle.onkey(drawDown, "j")
turtle.onkey(drawLeft, "h")
turtle.onkey(drawRight, "l")
turtle.onkey(drawUpRight, "u")
turtle.onkey(drawUpLeft, "y")
turtle.onkey(drawDownLeft, "b")
turtle.onkey(drawDownRight, "n")

turtle.onkey(setRed, "r")
turtle.onkey(setGreen, "g")
turtle.onkey(setTurquoise, "t")

turtle.listen()

