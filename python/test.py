import turtle 

t = turtle.Turtle()

t.pencolor("pink")
t.speed(0)

for i in range(5):
    t.fd(50)
    t.lt(123) # Let's go counterclockwise this time 
    
t.pencolor("turquoise")
for i in range(5):
    t.fd(100)
    t.lt(123)
    
turtle.done()
