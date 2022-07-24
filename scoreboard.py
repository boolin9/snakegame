# Imports
from turtle import Turtle

# Scoreboard class
class Scoreboard(Turtle):

    # Class initialization
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pu()
        self.hideturtle()
        self.goto(0, 260)
        self.color('white')
        self.update_scoreboard()


    # Update score function
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align='center', font=('Arial', 24, 'normal'))


    # Game over function
    def game_over(self):
        self.color('red')
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=('Arial', 36, 'bold'))


    # Increase score function
    def score_inc(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

