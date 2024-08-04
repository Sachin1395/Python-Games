from turtle import  Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1



class CarManager():
    def __init__(self):
        self.allcars=[]

    def create_car(self):
        chance=random.randint(1,8)
        if chance==1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1,stretch_len=3)
            new_car.y=random.randint(-250,250)
            new_car.goto(300,new_car.y)
            new_car.color(random.choice(COLORS))
            self.allcars.append(new_car)

    def move(self):
        for x in self.allcars:
            x.backward(STARTING_MOVE_DISTANCE)

    def speed_inc(self):
        global STARTING_MOVE_DISTANCE
        for x in self.allcars:
            STARTING_MOVE_DISTANCE+=MOVE_INCREMENT


