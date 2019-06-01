import turtle
import random

turtle.pensize(8)

color = ["blue", "green", "red", "yellow", "pink", "turquoise", "orange", "magenta"]

turtle.speed(0)

for c in range(10000):
    x = random.randint(-480, 400)
    y = random.randint(-480, 400)
    turtle.color(random.choice(color))
    turtle.goto(x, y)
