# Using text reading software/library was a bit overkill, and the image recognition wasn't the best. I could have
# done better formating for the text typing.

# Next time, use some web scrapping, since the text appears on the 'html' of the website, with that I wouldn't need
# to use image recognition, would be faster and need less resources.

# The random part probably could be better.

# The if statements could be better too.

from random import randint
from pynput.keyboard import Controller
from pyautogui import screenshot
from pytesseract import pytesseract
from PIL import ImageOps
import time

keyboard = Controller()
image_name = "characters.png"
ss_region = (583, 338, 850, 345)

# Makes the keyboard look less robotic
natural_times = [0.01, 0.02, 0.03, 0.04, 0.06, 0.07, 0.08, 0.09, 0.09, 0.09, 0.09, 0.09, 0.09, 0.09, 0.09, 0.09, 0.09]


# Function that writes the parameter.
def type_string(string):
    time.sleep(0.5)
    max_index = len(natural_times) - 1
    for i in string:
        random_time = randint(0, max_index)
        time.sleep(natural_times[random_time])
        keyboard.type(i)


def get_image(region, format):
    time.sleep(2)
    if format == "a":
        image = screenshot(region=region)
        image_gs = ImageOps.grayscale(image)
        image_gs.save(image_name)
        return image_gs
    if format == "b":
        image = screenshot()
        image_gs = ImageOps.grayscale(image)
        image_gs.save(image_name)
        return image_gs


def img_to_text(image):
    text = pytesseract.image_to_string(image)
    text[0].upper()

    print(text)
    return text


# Using Tesseract OCR to extract all the characters in the image saved.
tesseract_path = "C:\\TESSERACT-OCR\\tesseract.exe"
pytesseract.tesseract_cmd = tesseract_path

ss_format = input("[a]Typeracer screenshot or [b]full screenshot? ")


if ss_format == "a" or ss_format == "b":
    get_image(ss_region, ss_format)
else:
    quit()

type_string(img_to_text(image_name))
