import turtle
import random

turtle.bgpic("/home/claforte/Desktop/emily/kaito + coo.png")

a = turtle.Turtle()
a.color("red")

b = turtle.Turtle()
b.color("blue")

c = turtle.Turtle()
c.color("purple")

turtles = [a, b, c]

for item in turtles:
    item.pu()
    item.shape("turtle")
    item.shapesize(4, 4)

a.goto(-300, -100)
b.goto(-300, 0)
c.goto(-300, 100)

for race in range(100):
    for item in turtles:
        item.fd(random.randint(20, 120))
        item.rt(random.randint(1, 20))
        item.lt(random.randint(1, 20))
