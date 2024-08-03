import random
from turtle import Turtle
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5)
        self.color("blue")
        self.penup()
        self.goto(random.randint(-208, 280), random.randint(-280, 280))


    def relocate(self):
        self.goto(random.randint(-280, 280)/2, random.randint(-280, 280)/2)
