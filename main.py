# Imports
from snake import Snake
from turtle import Screen
from food import Food
import random
import time

# Screen
window = Screen()
window.setup(600, 600)
window.bgcolor('black')
window.title("Snake Game")
window.tracer(0)

# Snake
snake = Snake()
food = Food()

# Key controls
window.listen()
left = window.onkey(snake.left, "Left")
right = window.onkey(snake.right, "Right")
up = window.onkey(snake.up, "Up")
down = window.onkey(snake.down, "Down")

# Initialize game
game_on = True

# Run game
while game_on:
    window.update()
    time.sleep(0.1)
    snake.move()
    
    if snake.head.distance(food) < 15:
        food.refresh()


window.exitonclick()