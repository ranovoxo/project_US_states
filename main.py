import turtle
import pandas as pd
from tkinter import messagebox

def check_for_non_chars(text):
    result = True
    for ltr in text:
        if ltr.isalpha() != True and ltr != " ":
            result = False
            break
    return result

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"title={len(guessed_states)}/50 States Correct", prompt="What's another state's name").title()

    if check_for_non_chars(answer_state) == False:
        msg = f"Non-Alphanumeric characters allowed !@#$%^& etc."
        messagebox.showinfo("showinfo", msg)
        continue
    if answer_state in guessed_states:
        msg = f"You guessed {answer_state} already."
        messagebox.showinfo("showinfo", msg)
        continue

    usa = pd.read_csv("50_states.csv")
    all_states = usa.state.to_list()
    
    if answer_state == "Exit":
        states_to_learn = []
        for state in all_states:
            if state not in guessed_states:
                states_to_learn.append(state)
        pd.DataFrame(states_to_learn).to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = usa[usa.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        guessed_states.append(answer_state)

if len(guessed_states) == 50:
    messagebox.showinfo("showinfo", "Congrats! You got all the states. You're state champion!")
    

