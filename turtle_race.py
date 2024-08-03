from turtle import Turtle, Screen
import random



screen=Screen()
screen.setup(1000,600)
user_input = screen.textinput(title="Make a guess", prompt="ENter a color :")

colors=["red","green","blue", "yellow"]
if user_input not in colors:
    colors.append(user_input)
    colors.remove("green")
final_tims=[]
for x in range(4):
    new=Turtle()
    new.shape("turtle")
    a=random.choice(colors)
    new.color(a)
    colors.remove(a)
    final_tims.append(new)


y=[200,100,-100,-200]
for x in range(4):
    final_tims[x].penup()
    final_tims[x].goto(x=-400,y=y[x])

is_race_on = True

while is_race_on:
    for x in final_tims:
        x.speed("fastest")
        if x.xcor() >= 400:
            is_race_on= False
            if x.color()== user_input:
                print("u won")
            else :
                print(" u lost")
        x.forward(random.randint(0,10))

screen.exitonclick()