import turtle
from turtle import Turtle, Screen
import random as rand

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
user_bet = user_bet.lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Turtle creations
timmy = Turtle(shape="turtle")
rich = Turtle(shape="turtle")
bob = Turtle(shape="turtle")
star = Turtle(shape="turtle")
juan = Turtle(shape="turtle")
fluffy = Turtle(shape="turtle")

turtle_xcoord = -230
turtle_ycoord = -100

racing_turtles = [timmy, rich, bob, star, juan, fluffy]
shuffled_colors = colors.copy()
rand.shuffle(shuffled_colors)


for index, color in enumerate(colors):
    # lifting the pen of each turtle so that each time it gets moved to it necessary location on the grid, it doesn't leave a line
    racing_turtles[index].penup()
    # I don't want error to occur on account of there being index that ezxist that the lenght of colors that exists
    if len(shuffled_colors) == len(racing_turtles):
        racing_turtles[index].color(shuffled_colors[index])
    # placing a turtle where it should be on the grid
    racing_turtles[index].goto(turtle_xcoord, turtle_ycoord)
    # incrementing the vertical location/spacing of the next turtle being iterated on
    turtle_ycoord += 50

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in racing_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won!! The {winning_color} turtle won!")
            else:
                print(f"You lost!! The {winning_color} turtle won!")

        random_distance = rand.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()