# Imports
from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time

# Screen
window = Screen()
window.setup(600, 600)
window.bgcolor('black')
window.title("Snake Game")
window.tracer(0)

# Objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score_inc()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()

    # Detect collision with body
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()


window.exitonclick()