import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Drawing Polygons with Turtle")

pen = turtle.Turtle()
pen.speed(3)

def draw_polygon(sides, length, fill_color):
    angle = 360 / sides
    pen.fillcolor(fill_color)
    pen.begin_fill()
    for _ in range(sides):
        pen.forward(length)
        pen.left(angle)
    pen.end_fill()

pen.penup()
pen.goto(-200, 0)
pen.pendown()
draw_polygon(3, 100, "yellow")

pen.penup()
pen.goto(0, 0)
pen.pendown()
pen.fillcolor("green")
pen.begin_fill()
for _ in range(2):
    pen.forward(150)
    pen.left(90)
    pen.forward(80)
    pen.left(90)
pen.end_fill()

pen.penup()
pen.goto(200, 0)
pen.pendown()
draw_polygon(6, 80, "orange")

pen.hideturtle()
turtle.done()