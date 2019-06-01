import turtle 

t = turtle.Turtle()

screen = turtle.Screen()

screen.bgpic("shine!!!.gif")

t.pencolor("orange")
t.speed(0)
t.width(10)

t.setpos(-60,30)
t.circle(120, 90)

for i in range(500):
    t.fd(50)
    t.lt(123) # Let's go counterclockwise this time 
    
t.pencolor("turquoise")
for i in range(5):
    t.fd(100)
    t.lt(123)
    
turtle.done()
