#!/usr/bin/env python

import pyscreenshot as ImageGrab
from PIL import Image

if __name__ == "__main__":
    im = ImageGrab.grab()
    im.save("lol.jpg")

    foo = Image.open("lol.jpg")
    foo = foo.resize((300,100),Image.ANTIALIAS)
    foo.save("lol.jpg",quality=70)
