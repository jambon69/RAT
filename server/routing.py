#!/usr/bin/env python

import lolparser

def get(param):
    if param == "/":
        return lolparser.parse_it("html/index.html")
    elif param == "/index":
        return lolparser.parse_it("html/index.html")
    else:
        return lolparser.parse_it("html/404.html")

def post(param):
    pass
