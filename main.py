import turtle
import pandas

screen = turtle.Screen()
screen.title("Guess The States Game")
image = "india-states-map.gif"
screen.addshape(image)

turtle.shape(image)

# def buttonclick(x, y):
#     #turtle.onscreenclick(None)
#     print(x, y)
#
# turtle.onscreenclick(buttonclick)
# turtle.mainloop()

data = pandas.read_csv("indian_states_uts.csv")



guessed_states = []
missing_states = []
all_states = data.state.to_list()

while len(guessed_states) <= 35:

    answer_text = screen.textinput(title=f"{len(guessed_states)}/35 right!",
                                   prompt="Type the name of a state or UT").title()
    #We can use the title() function to capitalize the first letter and keep the other letters small.

    if answer_text == "Exit":
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        print(missing_states)
        break

    if answer_text in all_states:
        guessed_states.append(answer_text)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_text]
        # This line will help us pull the particular row corresponding to the answer text

        t.goto(int(state_data.x), int(state_data.y))
        #This line makes the invisible Turtle reach that location in the map.

        t.write(answer_text)
        # Or you can write t.write(state_data.state.item())
        # Item is a Pandas functions which looks at a row and grabs the first element alone.

screen.exitonclick()