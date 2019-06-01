import time

import turtle

turtle.mode("logo")

h = turtle.Turtle()
h.color("blue")
h.shape("arrow")
h.shapesize(1, 10)

m = turtle.Turtle()
m.color("black")
m.shape("arrow")
m.shapesize(1, 14)

s = turtle.Turtle()
s.color("red")
s.shape("arrow")
s.shapesize(1, 17)

def showHands():
    t = time.localtime()
    s.seth(t.tm_sec*6)
    m.seth(t.tm_min*6)
    h.seth(t.tm_hour*30 + t.tm_min*0.5)
    turtle.ontimer(showHands, 1000)

showHands()

#Hyoo hyoo, Kyaaaaa, Pero pero... pero pero... pero pero popo
