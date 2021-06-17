import button_actions.generic
import button_actions.visualstudio

import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from colourwheel import colourwheel

class KeyboardHandler:
    buttonActions = [
        None, #0
        None, #1
        None, #2
        button_actions.visualstudio.StopDebugging, #3
        None, #4
        button_actions.visualstudio.GoToImplementation, #5
        None, #6
        None, #7
        None, #8
        button_actions.visualstudio.FindReferences, #9
        None, #A
        button_actions.generic.F10, #B
        None, #C
        button_actions.generic.F12, #D
        button_actions.visualstudio.RunTests, #E
        button_actions.generic.F5 #F
    ]

    def __init__(self):
        self.kbd = Keyboard(usb_hid.devices)
        self.layout = KeyboardLayoutUS(self.kbd)

    def handleButtons(self, buttonStates):
        pressedIndex = buttonStates.getFirstPressedButtonIndex()

        if (pressedIndex >= 0):
            buttonStates.pixels[pressedIndex] = colourwheel(pressedIndex * 16)

            if buttonStates.isNotHeld(pressedIndex):
                buttonAction = self.buttonActions[pressedIndex]
                if not buttonAction is None:
                    buttonAction(self.kbd)
                buttonStates.setHeld(pressedIndex)
        else:  # Released state
            buttonStates.released()
            time.sleep(0.1) # Debounce
