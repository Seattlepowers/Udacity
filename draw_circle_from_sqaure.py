import turtle
import time


def draw_square():
    count = 0
    square = 4
    while count < square:
        brad.forward(100)
        brad.right(90)
        count = count +1

def rot():
    brad.right(10)

start = "start"
while(start == "start"):
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(10)

    time.sleep(1)

    count=0
    for i in range(1,37):
        draw_square()
        rot()
    count += 1

    window.exitonclick()

