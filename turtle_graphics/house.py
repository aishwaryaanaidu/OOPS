from turtle import Turtle
from random import randint

turtle1 = Turtle()
turtle1.color('green')
turtle1.shape('turtle')
turtle1.penup()
turtle1.goto(-280, 70)
turtle1.pendown()

turtle2 = Turtle()
turtle2.color('red')
turtle2.shape('turtle')
turtle2.penup()
turtle2.goto(-120, 40)
turtle2.pendown()

turtle3 = Turtle()
turtle3.color('blue')
turtle3.shape('turtle')
turtle3.penup()
turtle3.goto(50, 10)
turtle3.pendown()

turtle_list = [turtle1, turtle2, turtle3]
for turtle in turtle_list:
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(30)
    turtle.forward(100)
    turtle.right(120)
    turtle.forward(100)

input("Press enter to close")
