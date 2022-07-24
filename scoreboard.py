from turtle import Turtle

class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.score = 0
        self.pu()
        self.hideturtle()
        self.goto(0, 260)
        self.color('white')
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align='center', font=('Arial', 24, 'normal'))


    def score_inc(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

