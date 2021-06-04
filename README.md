# pico-rgb-keypad

A project in CircuitPython to get the [Pimoroni Pico RGB Keypad Base](https://shop.pimoroni.com/products/pico-rgb-keypad-base) working as a USB HID.

## Installation
Note: these instructions are written from a Windows perspective. You may have to modify them slightly if using other operating systems.

1. Flash your Pico with CircuitPython.
    - You can download the latest release [here](https://circuitpython.org/board/raspberry_pi_pico/).
    - The code has been tested with versions 6.2.0 and 6.3.0.
1. Download the [AdaFruit circuit python bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/download/20210604/adafruit-circuitpython-bundle-py-20210604.zip).
1. Create a `lib` folder on the Pico and copy over the following files and folders into the lib folder:
    - adafruit_bus_device (folder)
    - adafruit_hid (folder)
    - adafruit_dotstar.py (file)
1. Copy the contents of the `src` folder to the root of the Pico.
1. If this has worked you should see a startup animation on the keys.