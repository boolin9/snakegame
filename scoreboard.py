# Imports
from turtle import Turtle


# Scoreboard class
class Scoreboard(Turtle):

    # Class initialization
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('score.txt') as high_score:
            self.highscore = int(high_score.read())
        self.pu()
        self.hideturtle()
        self.goto(0, 260)
        self.color('white')
        self.update_scoreboard()


    # Update score function
    def update_scoreboard(self):
        self.clear()
        self.goto(0, 260)
        self.color('white')
        self.write(f"Score: {self.score} | High Score: {self.highscore}", align='center', font=('Bit5x3', 24, 'normal'))
        
    
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score 
            with open('score.txt', mode='w') as new_score:
                new_score.write(str(self.score))
        self.score = 0
        self.update_scoreboard()


    # Game over function
    def game_over(self):
        self.color('red')
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=('Bit5x3', 36, 'bold'))


    # Increase score function
    def score_inc(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

