import time
from turtle import Screen
from bats import Paddle
from ball import Ball
from score import Score

game_screen=Screen()
game_screen.bgcolor("Black")
game_screen.setup(800,600)
game_screen.title("Pong")
game_screen.tracer(0)

score= Score()
score.update()



r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)
ball= Ball()



game_screen.listen()
game_screen.onkeypress(r_paddle.go_up,"Up")
game_screen.onkeypress(r_paddle.go_down,"Down")

game_screen.onkeypress(l_paddle.go_up,"w")
game_screen.onkeypress(l_paddle.go_down,"s")

game_is_on = True

while game_is_on:
    game_screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor()>290 or ball.ycor()<-290:
        ball.bounce_y()

    if (ball.xcor()==340 and ball.distance(r_paddle)<50) or (ball.xcor()==-340 and ball.distance(l_paddle)<50):
        ball.bounce_x()

    if 400<ball.xcor() :
        ball.reset()
        score.lscore+=1
        score.update()


    if ball.xcor() < -400:
        ball.reset()
        score.rscore += 1
        score.update()

game_screen.mainloop()