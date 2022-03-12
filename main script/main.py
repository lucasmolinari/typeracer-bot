from pynput.keyboard import Controller
import time
from random import randint

keyboard = Controller()

# Makes the keyboard look less robotic
natural_times = [0.01, 0.02, 0.03, 0.04, 0.06, 0.07, 0.08, 0.09, 0.09, 0.09, 0.09]


def type_string(string):
    time.sleep(1)
    max_index = len(natural_times) - 1
    for letter in string:
        random_time = randint(0, max_index)
        time.sleep(natural_times[random_time])
        keyboard.type(letter)


type_string("Hello, World! I'm using Python!")
