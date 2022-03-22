from turtle import Turtle, Screen
import random
from tkinter import messagebox

CANVSIZE_X = 1280
CANVSIZE_Y = 720
STARTING_X = CANVSIZE_X / -2.13
STARTING_Y = 0
TEXT_COOR = (((-CANVSIZE_X / 2) + 20), ((CANVSIZE_Y / 2) -40))
FINISHING_X = CANVSIZE_X / 2.13
TURTLE_STEP = 30
TURTLE_SPEED = 0

screen = Screen()
screen.setup(CANVSIZE_X, CANVSIZE_Y)
screen.bgcolor("grey")

choices = {
    1: "Red",
    2: "Yellow",
    3: "Green",
    4: "Blue",
    5: "Purple"
}

user_bet = screen.textinput(title="Place your bet!", prompt="Which turtle are you betting on?"
                                                            "\n"
                                                            "\n1: Red"
                                                            "\n2: Yellow"
                                                            "\n3: Green"
                                                            "\n4: Blue"
                                                            "\n5: Purple"
                                                            "\n"
                                                            "\nPlease, enter a number:")

while not user_bet.isnumeric() or int(user_bet) not in choices.keys():
    user_bet = screen.textinput(title="Place your bet!", prompt="WRONG INPUT!"
                                                                "\n"
                                                                "\nWhich turtle are you betting on?"
                                                                "\n"
                                                                "\n1: Red"
                                                                "\n2: Yellow"
                                                                "\n3: Green"
                                                                "\n4: Blue"
                                                                "\n5: Purple"
                                                                "\n"
                                                                "\nPlease, enter a number:")



text = Turtle()
text.hideturtle()
text.speed(0)
text.penup()
text.goto(TEXT_COOR)
text.write(f"Your bet: {choices[int(user_bet)]}",
           font=("arial", 10, "normal"),
           align="left")
text.goto((FINISHING_X), (CANVSIZE_Y / 2))
text.color("white")
text.pendown()
text.goto((FINISHING_X), (-CANVSIZE_Y / 2))
text.penup()



red_turtle = Turtle()
red_turtle.hideturtle()
red_turtle.shape("turtle")
red_turtle.color("red")
red_turtle.speed(TURTLE_SPEED)
red_turtle.penup()
red_turtle.goto(STARTING_X, (STARTING_Y + 80))
red_turtle.showturtle()

yellow_turtle = Turtle()
yellow_turtle.hideturtle()
yellow_turtle.shape("turtle")
yellow_turtle.color("yellow")
yellow_turtle.speed(TURTLE_SPEED)
yellow_turtle.penup()
yellow_turtle.goto(STARTING_X, (STARTING_Y + 40))
yellow_turtle.showturtle()

green_turtle = Turtle()
green_turtle.hideturtle()
green_turtle.shape("turtle")
green_turtle.color("green")
green_turtle.speed(TURTLE_SPEED)
green_turtle.penup()
green_turtle.goto(STARTING_X, STARTING_Y)
green_turtle.showturtle()

blue_turtle = Turtle()
blue_turtle.hideturtle()
blue_turtle.shape("turtle")
blue_turtle.color("blue")
blue_turtle.speed(TURTLE_SPEED)
blue_turtle.penup()
blue_turtle.goto(STARTING_X, (STARTING_Y - 40))
blue_turtle.showturtle()

purple_turtle = Turtle()
purple_turtle.hideturtle()
purple_turtle.shape("turtle")
purple_turtle.color("purple")
purple_turtle.speed(TURTLE_SPEED)
purple_turtle.penup()
purple_turtle.goto(STARTING_X, (STARTING_Y - 80))
purple_turtle.showturtle()

turtle_list = [red_turtle, yellow_turtle, green_turtle, blue_turtle, purple_turtle]

race_over = False
race_winner = None

while not race_over:
    for turtle in turtle_list:
        turtle.forward(random.randint(0, TURTLE_STEP))
        if turtle.xcor() >= (FINISHING_X - 5):
            race_over = True
            race_winner = turtle.color()

print(race_winner[0].title())
if race_winner[0].title() == choices[int(user_bet)]:
    messagebox.showinfo(title="You win!", message=f"Congratulations!"
                                                  f"\n"
                                                  f"\n{race_winner[0].title()} turtle won the race!")
else:
    messagebox.showinfo(title="You lose.", message=f"You should have bet on {race_winner[0]} turtle.")

screen.exitonclick()




