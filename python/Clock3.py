import time

import turtle

turtle.mode("logo")

turtle.width(5)

h = turtle.Turtle()
h.color("green")
h.shape("arrow")
h.shapesize(1, 10)

m = turtle.Turtle()
m.color("blue")
m.shape("arrow")
m.shapesize(1, 14)

s = turtle.Turtle()
s.color("turquoise")
s.shape("arrow")
s.shapesize(1, 17)

def showHands():
    turtle.tracer(0, 0)
    t = time.localtime()
    s.seth(t.tm_sec*6)
    m.seth(t.tm_min*6)
    h.seth(t.tm_hour*30 + t.tm_min*0.5)
    turtle.ontimer(showHands, 50)
    turtle.update()

def makeFace():
    b = turtle.Turtle()
    b.speed(0)
    b.hideturtle()
    b.penup()

    b.dot(350)
    b.pencolor("white")
    b.dot(340)

    b.pencolor("black")
    num = 1
    for a in range(1, 13):
        b.goto(0, -22)
        b.seth(a*30)
        b.fd(140)
        b.write(a, align = "center", font = ("Arial", 25, "bold"))
    for a in range(0, 360, 6):
        b.goto(0, 0)
        b.seth(a)
        b.fd(160)
        b.dot(5)


makeFace()


showHands()

#Hyoo hyoo, Kyaaaaa, Pero pero... pero pero... pero pero popo
