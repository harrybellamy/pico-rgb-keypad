import time

import usb_midi
import adafruit_midi

from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff
from adafruit_midi.control_change import ControlChange

class MidiHandler:
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

    def __init__(self):
       self.midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0)

    def handleButtons(self, buttonStates):
        index = buttonStates.getFirstPressedButtonIndex()

        if not index == -1:
            note = self.noteMap[index]
            if not note is None:
                self.midi.send(NoteOn(note, 120))
                time.sleep(0.1)
                self. midi.send([
                    NoteOff(note, 120),
                    ControlChange(3, 44)])

