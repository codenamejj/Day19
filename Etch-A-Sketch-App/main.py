from turtle import Turtle, Screen


tom = Turtle()
screen = Screen()


def move_forward():
    return tom.forward(10)


def move_backward():
    return tom.backward(10)


def turn_right():
    return tom.right(10)


def turn_left():
    return tom.left(10)


def draw_circle():
    tom.circle(10)


def reset():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()


screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(reset, "c")
screen.onkey(draw_circle, "q")

screen.listen()

screen.exitonclick()


