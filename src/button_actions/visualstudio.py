import time
from adafruit_hid.keycode import Keycode

def StopDebugging(kbd) :
    kbd.press(Keycode.SHIFT)
    time.sleep(0.1)
    kbd.send(Keycode.F5)

def GoToImplementation(kbd) :
    kbd.press(Keycode.CONTROL)
    time.sleep(0.1)
    kbd.send(Keycode.F12)

def FindReferences(kbd) :
    kbd.press(Keycode.SHIFT)
    time.sleep(0.1)
    kbd.send(Keycode.F12)

def RunTests(kbd) :
    kbd.press(Keycode.CONTROL)
    kbd.press(Keycode.R)
    kbd.release(Keycode.R)
    kbd.send(Keycode.T)