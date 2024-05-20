import turtle

t = turtle.Turtle()
t.color("blue")

def draw_segment():
    t.forward(40)
    t.right(45)
    t.forward(40)
    t.penup()
    t.forward(5)
    t.pendown()
    t.right(45)

for _ in range(4):
    draw_segment()

def draw_rest():
    t.forward(40)
    t.right(45)
    t.forward(35)
    t.pendown()
    t.right(135)
    t.forward(67)
    t.right(90)
    t.forward(26.6)
    t.right(90)
    t.penup()
    t.forward(40)
    t.right(45)
    t.forward(40)
    t.right(45)
    t.forward(5)

for _ in range(4):
    draw_rest()

turtle.done()
