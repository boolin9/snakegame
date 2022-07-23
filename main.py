# Imports
from snake import Snake
from turtle import Screen
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

left = window.onkey(snake.left, "Left")
right = window.onkey(snake.right, "Right")
up = window.onkey(snake.up, "Up")
down = window.onkey(snake.down, "Down")
window.listen()

# Initialize game
game_on = True

# Run game
while game_on:
    window.update()
    time.sleep(0.1)

    snake.move()
    
window.exitonclick()