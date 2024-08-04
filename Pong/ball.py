from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.xmove=5
        self.ymove=5
        self.move_speed=0.1




    def move(self):
        newx= self.xcor()+self.xmove
        newy= self.ycor()+self.ymove
        self.goto(x=newx,y=newy)

    def bounce_y(self):
        self.ymove *=-1

    def bounce_x(self):
        self.xmove *=-1
        self.move_speed*=0.9

    def reset(self):
        self.goto(0,0)
        self.move_speed = 0.1