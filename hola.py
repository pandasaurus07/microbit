# Imports go at the top
from microbit import *


# Code in a 'while True:' loop repeats forever
while True:
    display.show(Image.ARROW_E)
    sleep(1000)
    display.show(Image.ARROW_N)
    sleep(1000)
    display.scroll('Esteban')
