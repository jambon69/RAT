#!/usr/bin/env python

import socket
import select

METHODS = ["GET", "POST"]

def fill_web_response(answer):
    response = []
    response.append("HTTP/1.1 200 OK")
    response.append("Content-Type: text/html; charset=UTF-8")
    response.append("Content-Length: " + str(len(answer)))
    response.append("")
    response.append(answer)
    return '\r\n'.join(response)

def web_msg(sock, method, file_requested):
    if method == 'GET' and file_requested == '/':
        answer = open("html/index.php").read()
    else:
        answer = "<html><h1>Site under construction</h1></html>"
    sock.send(fill_web_response(answer))

def analyze_msg(msg):
    split_msg = msg.split('\n')
    firstline = split_msg[0].split()
    if firstline[0] in METHODS and firstline[2].find("HTTP") != -1:
        print split_msg[1].split()[1] + ": " + firstline[0] + " " + firstline[1]
        return 1, firstline[0], firstline[1]
    return 0, 0, 0

def init():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 1337))
    sock.listen(5)
    return sock

def accept(sock_list, sock):
    sock_client, infos_client = sock.accept()
    print "new client : " + str(infos_client)
    sock_list.append(sock_client)
    
def main():
    sock_list = []
    sock = init()
    sock_list.append(sock)
    while True:
        rlist, wlist, xlist = select.select(sock_list, [], [])
        for elem in rlist:
            if elem == sock:
                accept(sock_list, sock)
            else:
                msg = elem.recv(2048)
                if len(msg) == 0:
                    elem.close()
                    sock_list.remove(elem)
                else:
                    msg_type, method, request = analyze_msg(msg)
                    if msg_type == 1:
                        web_msg(elem, method, request)
                    else:
                        print "> " + msg



if __name__ == '__main__':
    main()
