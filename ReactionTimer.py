import cyberpi
import random
from time import time, sleep

# Function to play the reaction time tester game
def play_reaction_time_tester():
    # Instructions
    cyberpi.console.print("Press the button when the signal appears!")

    # Wait for random time before displaying the signal
    sleep_time = 1 + random.randint(1, 5)
    sleep(sleep_time)

    # Display the signal
    cyberpi.console.clear()
    cyberpi.console.print("Press now!")
    cyberpi.led.on("red")

    # Measure the reaction time
    start_time = time()
    while not cyberpi.controller.is_press('A'):
        pass
    reaction_time = time() - start_time

    # Display the result
    cyberpi.console.clear()
    cyberpi.console.print(f"Reaction time: {reaction_time:.2f} seconds")
    cyberpi.led.off()

# Main loop
while True:
    cyberpi.console.print("Press A to start the Reaction Time Tester!")
    while not cyberpi.controller.is_press('A'):
        pass
    play_reaction_time_tester()
    sleep(2)

