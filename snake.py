from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20


class Snake:


    def __init__(self):
        self.snake_body = []
        self.create_snake()
    

    def create_snake(self):
        for position in START_POSITIONS:
            segment = Turtle('square')
            segment.color('blue')
            segment.pu()
            segment.goto(position)
            self.snake_body.append(segment)


    def move(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)
        self.snake_body[0].forward(MOVE_DIST)


    def left(self):
        self.snake_body[0].setheading(180)


    def right(self):
        self.snake_body[0].setheading(0)


    def up(self):
        self.snake_body[0].setheading(90)


    def down(self):
        self.snake_body[0].setheading(270)