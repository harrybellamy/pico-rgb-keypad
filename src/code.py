from buttonstate import ButtonState
import board
from digitalio import DigitalInOut, Direction

import animations
from keyboardhandler import KeyboardHandler
from midihandler import MidiHandler

cs = DigitalInOut(board.GP17)
cs.direction = Direction.OUTPUT
cs.value = 0
num_pixels = 16

buttonStates = ButtonState(num_pixels)

# startup animation
animations.topLeftToBottomRight(buttonStates.pixels)

buttonStates.released()

animations.clockwiseSpiral(buttonStates.pixels)

# initialise button handlers
midiHandler = MidiHandler()
keyboardHandler = KeyboardHandler()

currentHandler = midiHandler
otherHandler = keyboardHandler

stateChangeButtons = [0, 12]

while True:
    # detect a mode switch
    if buttonStates.areButtonsPressed(stateChangeButtons):
        print("changing state")
        temp = currentHandler
        currentHandler = otherHandler
        otherHandler = temp
        buttonStates.released()
        animations.topLeftToBottomRight(buttonStates.pixels)

    currentHandler.handleButtons(buttonStates)
