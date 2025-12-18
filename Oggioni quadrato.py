import turtle
screen = turtle.Screen()


screen.setup(width=1000, height=800)
screen.title("Quadrato")
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
    for b in range(4):
        drawing.forward(pixel_size)
        drawing.right(90)
    drawing.end_fill()

disegno(-100, 100, "green", 150)