#!/usr/bin/env python

from cStringIO import StringIO
import sys

def interpret(final, to_interpret, param):
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    toexec = ""
    for line in to_interpret:
        if line.find("include") != -1:
            final.append(parse_it("html/" + line.split("'")[1], param))
        else:
            toexec += "\n" + line
    exec(toexec)
    sys.stdout = old_stdout
    final.append(mystdout.getvalue())
    return final

def parse_it(filename, param):
    lines = open(filename).read().split('\n')
    final = []
    i = 0
    while i < len(lines):
        if lines[i].find("<?lolpy") != -1:
            to_interpret = []
            i = i + 1
            while i < len(lines) and lines[i].find("?>") == -1:
                to_interpret.append(lines[i])
                i = i + 1
            interpret(final, to_interpret, param)
        else:
            final.append(lines[i])
        i = i + 1
    return "\n".join(final)
