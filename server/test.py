#!/usr/bin/env python

import pyscreenshot as ImageGrab
from PIL import Image
from cStringIO import StringIO
import sys

if __name__ == "__main__":
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()

    print "lol"
    print "lul"
    
    sys.stdout = old_stdout

    print "----- \n" + mystdout.getvalue()
