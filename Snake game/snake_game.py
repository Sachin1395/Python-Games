import time
from snake import Snake
from scoreboard import Score
from food import Food
from turtle import Screen


screen= Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)


tim = Snake()
fd= Food()
score=Score()

screen.listen()
screen.onkey(tim.up,"Up")
screen.onkey(tim.down,"Down")
screen.onkey(tim.left,"Left")
screen.onkey(tim.right,"Right")




game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    tim.move()

    if tim.segments[0].distance(fd)<20:
        Food.relocate(fd)
        score.increase()
        tim.extend()
    if tim.head().xcor() > 290 or tim.head().xcor()<-290 or tim.head().ycor()> 290  or tim.head().ycor()<-290:
        game_is_on = False
        score.game_over()

    for x in tim.segments[1:]:
        if tim.head().distance(x)<10 :
            game_is_on=False
            score.game_over()





screen.mainloop()