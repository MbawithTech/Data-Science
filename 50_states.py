import turtle
import pandas
from turtle import Turtle, Screen
import time
import pandas as pd

screen = Screen()
image = "blank_states_img.gif"
screen.title("US States Game")
# screen.bgpic(picname="blank_states_img.gif")
screen.addshape(image)
turtle.shape(image)
df = pd.read_csv("50_states.csv")
# #get coordinates of points when clicked on screen
#
#
# def get_onscreen_coordinates(x, y):
#     print(x, y)
#
# turtle.onscreenclick(fun=get_onscreen_coordinates)

correct_states = 0
correct_guesses = []
is_game_on = True
# print(type(df["state"].values))

while correct_states < 50:
    answer_input = screen.textinput(title=f"{correct_states}/50 guessed correctly",
                                    prompt="What is your answer??").title()
    if answer_input in correct_guesses:
        t3 = Turtle()
        t3.hideturtle()
        t3.penup()
        t3.goto(x=0, y=280)
        t3.write(arg="You have already guessed this state", align="center", font=("Arial", 16, "normal"))
        time.sleep(0.5)
        t3.clear()
    elif answer_input in df["state"].values:
        ans_index = df[df["state"] == answer_input].index
        # x = int(df[df["state"] == answer_input]["x"])
        # y = int(df[df["state"] == answer_input]["y"])
        # x = int(df["x"].iloc[ans_index])
        # y = int(df["y"].iloc[ans_index])
        t = Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x=int(df["x"].iloc[ans_index]), y=int(df["y"].iloc[ans_index]))
        t.write(arg=f"{answer_input}", align="Center")
        correct_guesses.append(answer_input)
        correct_states += 1
    else:
        t1 = Turtle()
        t1.hideturtle()
        t1.penup()
        t1.goto(x=0, y=280)
        t1.write(arg="There is no such state!!!", align="center", font=("Arial", 16, "normal"))
        time.sleep(0.5)
        t1.clear()

if len(correct_guesses) == 50:
    t2 = Turtle()
    t2.hideturtle()
    t2.penup()
    t2.goto(x=0, y=280)
    t2.write(arg="Congratulations!! you guessed all states correctly", align="center", font=("Arial", 16, "normal"))
    time.sleep(0.8)
    t2.clear()

    # if correct_states == 50:
    #     is_game_on = False

turtle.mainloop()
# screen.exitonclick()


