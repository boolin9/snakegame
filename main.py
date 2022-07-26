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
def controls():
    window.listen()
    window.onkey(snake.left, "Left")
    window.onkey(snake.right, "Right")
    window.onkey(snake.up, "Up")
    window.onkey(snake.down, "Down")


# Initialize game
game_on = True

# Run game
while game_on:
    controls()
    window.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score_inc()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -295:
        scoreboard.game_over()
        restart = window.textinput("GAME OVER", "Do you want to play again? (Y/N)").lower()
        if restart == 'y':
            controls()
            scoreboard.reset()
            snake.reset()
        else:
            scoreboard.reset()
            scoreboard.game_over()
            game_on = False
            

    # Detect collision with body
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            restart = window.textinput("GAME OVER", "Do you want to play again?").lower()
            if restart == 'y':
                controls()
                scoreboard.reset()
                snake.reset()
            else:
                scoreboard.reset()
                scoreboard.game_over()
                game_on = False


window.exitonclick()