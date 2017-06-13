import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(5)
    count = 0
    square = 4
    while count <= square:
        brad.right(90)
        brad.forward(100)
        count = count +1

    adam =turtle.Turtle()
    adam.speed(10)
    adam.shape("arrow")
    adam.forward(100)
    adam.circle(100)

    angie =turtle.Turtle()
    angie.speed(10)
    angie.shape("arrow")
    angie.color("white")
    count = 0
    triangle = 3
    
    while count < triangle:
        angie.speed(10)
        angie.forward(200)
        angie.right(240)
        count += 1

    window.exitonclick()

draw_square()