# Imports
from turtle import Turtle
import random

# Food class
class Food(Turtle):


    # Initialize function
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.pu()
        self.shapesize(0.5, 0.5)
        self.speed('fastest')
        self.refresh()


    # Refresh food placement function
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)