import turtle

import pandas

score = 0
answers = []

data = pandas.read_csv("50_states.csv")
states = data.state

image = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(image)
turtle.shape(image)

while score < 50:
    user_answer = screen.textinput(f"{score}/50 States Correct", "Type a State name")
    user_answer = user_answer.title()
    if user_answer == "Exit":
        break
    for state in states:
        if user_answer == state:
            score += 1
            row = data[data["state"] == state]
            x = int(row.x)
            y = int(row.y)
            text = turtle.Turtle()
            text.penup()
            text.speed("fastest")
            text.goto(x, y)
            text.hideturtle()
            text.write(f"{state}")
            answers.append(user_answer)

states = states.to_list()

states_not_guessed = [state for state in states if state not in answers]


states_not_guessed = pandas.DataFrame(states_not_guessed, columns=["Missing States"])
states_not_guessed.to_csv()

print(states_not_guessed)
