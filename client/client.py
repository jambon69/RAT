#!/usr/bin/env python

import socket
import sys

def connect(ip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, 1337))
    return sock

def main():
    sock = connect("127.0.0.1")
    while True:
        sys.stdout.write("> ")
        msg = raw_input()
        sock.send(msg)

if __name__ == '__main__':
    main()
