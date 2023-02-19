from turtle import Turtle, Screen
import random


screen = Screen()

screen.setup(height=400, width=500)
user_bet = screen.textinput(title="What's your Bet?", prompt="Which turtle will win? Select your color:\n"
                                                             "red, orange, yellow, green, blue, purple")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

all_turtles = []
y_position = -100
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position)
    y_position += 40
    all_turtles.append(new_turtle)
# print(all_turtles)

race_on = False
if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 229:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Bet won! The {winning_color} turtle won the race!")
            else:
                print(f"Bet lost! The {winning_color} turtle won the race!")

        random_movement = random.randint(1, 10)
        turtle.forward(random_movement)

screen.exitonclick()

