from turtle import Turtle, Screen
import random


def left():
    snake.setheading(180)

def right():
    snake.setheading(0)

def up():
    snake.setheading(90)

def down():
    snake.setheading(270)


screen = Screen()
snake = Turtle('turtle')
screen.bgcolor('black')
screen.title("Snake Game")
screen.listen()
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(up, "Up")
screen.onkey(down, "Down")

while True:
    snake.pu()
    snake.forward(1)




screen.listen()

screen.exitonclick()