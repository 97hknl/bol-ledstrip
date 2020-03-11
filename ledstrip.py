import utime
import math
from color import colors
from neopixel import NeoPixel

class LedStrip:

    def __init__(self, pin, number):
        self._pin = pin
        self._colors = []
        self._number = number
        self._strip = NeoPixel(pin, number)
        self.clear()

    def clear(self):
        self.all((0,0,0))

    def add(self, color):
        self.flash(3, colors['GREEN'])
        self._colors.append(color)
        self.clear()

        i = 0
        leds_per_color = math.ceil(self._number / len(self._colors))

        for color in self._colors:
            for num in range(0, leds_per_color):
                if(i < self._number):
                    self.set_color(i, color)
                    i = i + 1

        self.update()

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

    def flash(self, n, color):
        for i in range(0, n):
            self.clear()
            for led in range(0, self._number):
                self.set_color(led, color, 0.5)


    def set_color(self, i, rgb, brightness = 0.1):
        self._strip[i] = tuple(
            [int(brightness * clr) for clr in rgb]
        )
        self.update()

    def update(self):
        self._strip.write()
