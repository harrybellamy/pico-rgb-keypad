import board
import busio
import adafruit_dotstar
from adafruit_bus_device.i2c_device import I2CDevice

class ButtonState:

    def __init__(self, num_pixels):
        self.num_pixels = num_pixels
        self.pixels = adafruit_dotstar.DotStar(board.GP18, board.GP19, num_pixels, brightness=0.5, auto_write=True)
        i2c = busio.I2C(board.GP5, board.GP4)
        self.device = I2CDevice(i2c, 0x20)
        self.held = [0] * num_pixels

    def read_button_states(self, x, y):
        pressed = [0] * 16
        with self.device:
            self.device.write(bytes([0x0]))
            result = bytearray(2)
            self.device.readinto(result)
            b = result[0] | result[1] << 8
            for i in range(x, y):
                if not (1 << i) & b:
                    pressed[i] = 1
                else:
                    pressed[i] = 0
        return pressed

    def released(self):
        for i in range(self.num_pixels):
            self.pixels[i] = (0, 0, 0) # Turn pixels off
            self.held[i] = 0  # Set held states to off

    def isNotHeld(self, index):
        return self.held[index] == 0

    def setHeld(self, index):
        self.held[index] = 1

    def getFirstPressedButtonIndex(self):
        pressed = self.read_button_states(0, self.num_pixels)

        for i in range(0, self.num_pixels):
            if pressed[i]:
                return i
        return -1

    def areButtonsPressed(self, indexes):
        print(str(len(indexes)))
        pressed = self.read_button_states(0, self.num_pixels)
        retval = 1
        for i in indexes:
            print("Pressed for " + str(i) + ": " + str(pressed[i]))
            retval = retval & pressed[i]
            
        return retval
