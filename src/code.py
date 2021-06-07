from buttonstate import ButtonState
import time
import board
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

import usb_midi
import adafruit_midi

from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff
from adafruit_midi.control_change import ControlChange

from digitalio import DigitalInOut, Direction

import animations
import button_actions.generic
import button_actions.visualstudio

cs = DigitalInOut(board.GP17)
cs.direction = Direction.OUTPUT
cs.value = 0
num_pixels = 16
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)
def colourwheel(pos):
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

buttonStates = ButtonState(num_pixels)


# startup animation
animations.topLeftToBottomRight(buttonStates.pixels, colourwheel)

buttonStates.released()

animations.clockwiseSpiral(buttonStates.pixels, colourwheel)

midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0)

noteMap = [
    "D#3",
    "B2",
    "G2",
    "D#2",
    "D3",
    "A#2",
    "F#2",
    "D2",
    "C#3",
    "A2",
    "F2",
    "C#2",
    "C3",
    "G#2",
    "E2",
    "C2"
]

while True:

    index = buttonStates.getFirstPressedButtonIndex()

    if not index == -1:
        note = noteMap[index]
        if not note is None:
            midi.send(NoteOn(note, 120))
            time.sleep(0.1)
            midi.send([NoteOff(note, 120),
               ControlChange(3, 44)])


buttonActions = [
    None,
    None,
    None,
    button_actions.visualstudio.StopDebugging,
    None,
    button_actions.visualstudio.GoToImplementation,
    None,
    None,
    None,
    button_actions.visualstudio.FindReferences,
    None,
    button_actions.generic.F10,
    None,
    button_actions.generic.F12,
    button_actions.visualstudio.RunTests,
    button_actions.generic.F5
]

while True:
    pressedIndex = buttonStates.getFirstPressedButtonIndex()

    if (pressedIndex >= 0):
        buttonStates.pixels[pressedIndex] = colourwheel(pressedIndex * 16)

        if buttonStates.isNotHeld(pressedIndex):
            buttonAction = buttonActions[pressedIndex]
            if not buttonAction is None:
                buttonAction(kbd)
            buttonStates.setHeld(pressedIndex)

    else:  # Released state
        buttonStates.released()
        time.sleep(0.1) # Debounce
