import turtle
screen = turtle.Screen()


screen.setup(width=1000, height=800)
screen.title("diamond")
screen.colormode(255)
R = 30
G = 158
B = 175
screen.bgcolor(R, G, B)
drawing = turtle.Turtle()
drawing.speed(2)
drawing.turtlesize(3)

def disegno(x, y, color, pixel_size):
    drawing.penup()
    drawing.goto(x, y)
    drawing.pendown()
    drawing.fillcolor(color)
    drawing.begin_fill()
    for b in range(2):
        drawing.circle(100, 60)
        drawing.right(170)
        drawing.circle(100, 60)
        drawing.right(130)
    drawing.end_fill()
    
disegno(-100, 100,"green", 150)