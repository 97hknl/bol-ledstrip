import utime
from neopixel import NeoPixel

class LedStrip:

    def __init__(self, pin, number):
        self._pin = pin
        self._number = number
        self._strip = NeoPixel(pin, number)
        self.clear()

    def clear(self):
        self.all((0,0,0))

    def all(self, color):
        for i in range(self._number):
            self.set_color(i, color)
        self.update()


    def blink(self, n, color):
        on=False
        for i in range(n * 2):
            on=not(on)
            if on:
                self.all(color)
            else:
                self.clear()
            utime.sleep(0.25)


    def set_color(self, i, rgb, brightness = 0.1):
        self._strip[i] = tuple(
            [int(brightness * clr) for clr in rgb]
        )
        self.update()

    def update(self):
        self._strip.write()
