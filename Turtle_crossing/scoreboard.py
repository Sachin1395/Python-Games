from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level_no=1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(x=-280,y=250)
        self.write(f"Level : {self.level_no}",font=FONT)

    def score_inc(self):
        self.clear()
        self.level_no+=1
        self.write(f"Level : {self.level_no}", font=FONT)

