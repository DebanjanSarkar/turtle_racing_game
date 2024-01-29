import random
import turtle
from race_utils import *

# Setting the turtle colormode to set using rgb values.
turtle.colormode(255)

# This variable is used to start and end the turtle race.
is_race_on = False

# set the screen height and width values in pixels
initial_screen_width = 1000
initial_screen_height = 700

# x-coordinates of start and finish line of the turtle race, on the basis of turtle coordinate system
start_line_x_cor = ( -1 * (initial_screen_width//2) + 40 )
finish_line_x_cor = ( (initial_screen_width//2) - 50 )

# colors of the turles and their corresponding rgb values
rainbow_colors = {
    "violet"    :   (127, 0, 255),
    "indigo"    :   (75, 0, 130),
    "blue"      :   (0, 0, 255),
    "green"     :   (0, 255, 0),
    "yellow"    :   (255, 255, 0),
    "orange"    :   (255, 165, 0),
    "red"       :   (255, 0, 0),
}

screen = turtle.Screen()
# setup() method is used to setup the initial size of the turtle graphics window.
# Float parameters represent the fraction of width and height of total screen, resp.
# Integer parameters represent width and height in pixels, respec.
screen.setup(width=initial_screen_width, height=initial_screen_height)

# Shows a prompt dialog box where user can enter his choice of bet.
# Will continue to ask user for input till user enters a rainbow color correctly!
user_bet = "x"
while user_bet[0] not in "vibgyor":
    title = "Make your bet"
    prompt = "Which turtle will win the race? Enter a color of rainbow (VIBGYOR):"
    if user_bet != "x":
        # Once user enters invalid input, this error message will be appended
        # in prompt message in the subsequent prompts.
        prompt = "Invalid Entry! Enter valid color of rainbow...\n"+prompt

    # code to display the prompt dialogue box to take user input.
    user_bet = screen.textinput( 
        title=title, 
        prompt=prompt 
    ).lower()

    # If the user enters valid color, then only this block will run
    # Only first character is checked so that even if user makes spelling mistake, color is identified
    if user_bet[0] in "vibgyor":
        break

# This dictionary will contain the turtle colors as key values and the respective coloured-turtle
# object as the values.
turtles_dict = dict()

# Setting the x and y coordinates for positioning each turtle in the beginning.
x = ( -1 * (initial_screen_width//2) + 20 )
y = ( (initial_screen_height//2) - 150 )

# Loop to create all the turtle of each color, and place them into their starting points.
for color in rainbow_colors:
    turtles_dict[color] = turtle.Turtle("turtle")
    turtles_dict[color].speed(3)
    turtles_dict[color].color( rainbow_colors[color] )
    turtles_dict[color].penup()
    turtles_dict[color].goto( x, y )
    y -= 50

# Draws starying and the finishing lines of the race.
draw_start__line(start_line_x_cor, initial_screen_height)
draw_finish__line(finish_line_x_cor, initial_screen_height)


# Loop to make the turtle move/race, till one of the turtle crosses finish line
is_race_on = True   # Starts the race
while is_race_on:
    for color in turtles_dict:
        # Each coloured-turtle makes a random step between 5 to 20 pixels
        random_step = random.randint(5,20)
        turtles_dict[color].forward( random_step )

        if turtles_dict[color].xcor() >= finish_line_x_cor:
            # After moving, if the turtle crosses finish line, this block activates.
            # This ends the race, and the current-color turtle is the winner.
            winner = color
            is_race_on = False
            break


print(f"{color.upper()} turtle is the winner!") 
if user_bet[0] == color[0].lower():
    print("YOU WIN! Your bet was correct...\n\n\n")
else:
    print(f"You LOSE! Your bet was {user_bet}...\n\n\n")

screen.exitonclick()
input("Press Enter to exit!")
