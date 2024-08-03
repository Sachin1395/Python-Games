from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score=0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write("Score : "+str(self.current_score),align="center")
        self.hideturtle()
    def increase(self):
        self.clear()
        self.current_score+=1
        self.write("Score : " + str(self.current_score), align="center")

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center")
