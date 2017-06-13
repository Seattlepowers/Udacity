import turtle
import time



def draw_square():
    count = 0
    square = 4
    while count <= square:
        brad.right(90)
        brad.forward(100)
        count = count +1

    
def draw_circle():
    adam.forward(100)
    adam.circle(100)

def draw_triangle():
    count = 0
    triangle = 3

    while count < triangle:
        angie.speed(10)
        angie.forward(200)
        angie.right(240)
        count += 1

start = "start"
while(start == "start"):
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(10)
    
    adam =turtle.Turtle()
    adam.speed(10)
    adam.shape("arrow")

    angie =turtle.Turtle()
    angie.speed(10)
    angie.shape("arrow")
    angie.color("white")

    time.sleep(1)
    draw_square()
    draw_circle()
    draw_triangle()
    window.exitonclick()

