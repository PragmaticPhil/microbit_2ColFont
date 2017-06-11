"""
Provides a "scroll" method that uses the WHALEYSANS_INTEGERS and PHILSANS_TEXT
alpha font.
"""
from microbit import *
from array import array


FONT = {
    '0': array('b', [9, 9, 9, 9, 9, 9, 9, 9, 9, 9,]),
    '1': array('b', [0, 9, 0, 9, 0, 9, 0, 9, 0, 9,]),
    '2': array('b', [9, 9, 0, 9, 9, 9, 9, 0, 9, 9,]),
    '3': array('b', [9, 9, 0, 9, 9, 9, 0, 9, 9, 9,]),
    '4': array('b', [9, 0, 9, 0, 9, 9, 0, 9, 0, 9,]),
    '5': array('b', [9, 9, 9, 0, 9, 9, 0, 9, 9, 9,]),
    '6': array('b', [9, 9, 9, 0, 9, 9, 9, 9, 9, 9,]),
    '7': array('b', [9, 9, 0, 9, 0, 9, 0, 9, 0, 9,]),
    '8': array('b', [9, 9, 9, 9, 0, 0, 9, 9, 9, 9,]),
    '9': array('b', [9, 9, 9, 9, 9, 9, 0, 9, 9, 9,]),
    'a': array('b', [0, 0, 0, 0, 9, 9, 9, 9, 0, 9,]),
    'b': array('b', [9, 0, 9, 0, 9, 0, 9, 9, 9, 9,]),
    'c': array('b', [0, 0, 0, 0, 9, 9, 9, 0, 9, 9,]),
    'd': array('b', [0, 9, 0, 9, 9, 9, 9, 9, 9, 9,]),
    'e': array('b', [9, 9, 9, 0, 9, 9, 9, 0, 9, 9,]),
    'f': array('b', [9, 9, 9, 0, 9, 9, 9, 0, 9, 0,]),
    'g': array('b', [9, 9, 9, 9, 0, 9, 0, 9, 9, 9,]),
    'h': array('b', [9, 0, 9, 0, 9, 9, 9, 9, 9, 9,]),
    'i': array('b', [9, 0, 0, 0, 9, 0, 9, 0, 9, 0,]),
    'j': array('b', [0, 9, 0, 0, 0, 9, 4, 9, 9, 9,]),
    'k': array('b', [9, 2, 9, 7, 9, 0, 9, 7, 9, 2,]),
    'l': array('b', [9, 0, 9, 0, 9, 0, 9, 0, 9, 6,]),
    'm': array('b', [9, 0, 0, 9, 9, 0, 0, 9, 9, 0,]),
    'n': array('b', [0, 0, 0, 0, 9, 9, 9, 9, 9, 9,]),
    'o': array('b', [0, 0, 9, 9, 9, 9, 9, 9, 0, 0,]),
    'p': array('b', [9, 9, 9, 9, 9, 4, 9, 0, 9, 0,]),
    'q': array('b', [0, 0, 9, 9, 9, 9, 4, 9, 0, 9,]),
    'r': array('b', [0, 0, 0, 0, 9, 9, 9, 0, 9, 0,]),
    's': array('b', [9, 9, 9, 0, 9, 9, 0, 9, 9, 9,]),
    't': array('b', [0, 0, 9, 0, 9, 9, 9, 0, 9, 9,]),
    'u': array('b', [0, 0, 0, 0, 9, 9, 9, 9, 9, 9,]),
    'v': array('b', [0, 0, 0, 0, 9, 9, 9, 9, 4, 4,]),
    'w': array('b', [0, 9, 9, 0, 0, 9, 9, 0, 0, 9,]),
    'x': array('b', [9, 9, 4, 4, 9, 9, 4, 4, 9, 9,]),
    'y': array('b', [0, 0, 9, 9, 9, 9, 0, 9, 9, 9,]),
    'z': array('b', [0, 0, 9, 9, 0, 9, 9, 0, 9, 9,]),
    ' ': array('b', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]),
}

def scroll(message, speed=150):
    width = (3 * len(message)) + 10
    img = Image(width, 5)
    column = 4
    for char in message.lower():
        character = FONT.get(char, False)
        if character:
            for i in range(5):
                pos = i * 2
                img.set_pixel(column, i, character[pos])
                img.set_pixel(column + 1, i, character[pos + 1])
        column += 3
    for i in range(width):
        display.show(img.crop(i, 0, 5, 5))
        sleep(speed)

#scroll("Hello world")
