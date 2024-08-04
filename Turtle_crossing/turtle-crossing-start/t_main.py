import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car = CarManager()
turtle= Player()


screen.listen()
screen.onkeypress(turtle.move,"Up")

score=Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()
    for x in car.allcars:
        if turtle.distance(x)<20 :
            game_is_on = False
    if turtle.ycor()==300:
        turtle.reset()
        car.speed_inc()
        score.score_inc()



