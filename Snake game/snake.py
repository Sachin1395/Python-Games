from turtle import Turtle
STARTING_POS=[(0,0),(-20,0),(-40,0)]

class Snake:
    def __init__(self):
        self.segments = []
        self.size = 2
        self.snake()



    def snake(self):
        for x in STARTING_POS:
            self.add_segment(x)

    def add_segment(self,x):
            segment = Turtle()
            segment.shape("square")
            segment.color("white")
            segment.speed("slow")
            segment.penup()
            segment.goto(x)
            self.segments.append(segment)
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for x in range(len(self.segments) - 1, 0, -1):
            self.segments[x].goto(self.segments[x - 1].xcor(), self.segments[x - 1].ycor())
        self.segments[0].forward(20)


    def up(self):
        self.segments[0].setheading(90)

    def down(self):
        self.segments[0].setheading(270)

    def left(self):
        self.segments[0].setheading(180)

    def right(self):
        self.segments[0].setheading(0)

    def head(self):
        return self.segments[0]









