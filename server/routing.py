#!/usr/bin/env python

import lolparser

def get(param, sock, parameters):
    if param == "/":
        return lolparser.parse_it("html/index.html", parameters)
    elif param == "/index":
        return lolparser.parse_it("html/index.html", parameters)
    else:
        return lolparser.parse_it("html/404.html", parameters)

def post(param, sock, parameters):
    if param == "/screenshot":
        for socket in parameters['sock_list']:
            if socket != sock:
                socket.send("screenshot")
        return lolparser.parse_it("html/index.html", parameters)
