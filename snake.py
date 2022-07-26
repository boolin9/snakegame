# Imports
from turtle import Turtle

# Constants
START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# Snake class
class Snake:

    # Class initialization
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
    

    # Create snake function
    def create_snake(self):
        for position in START_POSITIONS:
            self.add_segment(position)
            
    
    def reset(self):
        for segment in self.snake_body:
            segment.goto(1000,1000)
            
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]

    
    # Add segment function
    def add_segment(self, position):
        segment = Turtle('square')
        segment.color('blue')
        segment.pu()
        segment.goto(position)
        self.snake_body.append(segment)
    
    
    # Extend snake function
    def extend(self):
        self.add_segment(self.snake_body[-1].position())


    # Move function
    def move(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DIST)


    # Turn west
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)            


    # Turn east
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    # Turn north
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    # Turn south
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)