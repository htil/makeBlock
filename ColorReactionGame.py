import cyberpi
from random import choice
from time import time, sleep

# List of colors
colors = ["red", "green", "blue", "yellow", "purple", "orange"]

# Function to display a random color
def display_color():
    color = choice(colors)
    cyberpi.led.on(color)
    return color

# Function to play the reaction game
def play_reaction_game():
    # Instructions
    cyberpi.console.print("Wait for color...")
    sleep(1)
    cyberpi.console.print("Press button when you see:")
    target_color = display_color()
    sleep(0.5)

    # Wait for the target color to be displayed
    start_time = time()
    elapsed_time = 0
    while display_color() != target_color and elapsed_time < 5:  # Timeout set to 5 seconds
        elapsed_time = time() - start_time

    # Check if the player pressed the button in time
    while not cyberpi.controller.is_press('A'):
        pass

    # Display the result
    cyberpi.console.clear()
    if elapsed_time < 5:
        cyberpi.console.print("Congratulations!")
        cyberpi.audio.play_music(67, 0.25)
    else:
        cyberpi.console.print("Too slow!")
        cyberpi.audio.play_music(62, 0.25)

# Main loop
while True:
    play_reaction_game()
    sleep(2)
