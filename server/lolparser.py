#!/usr/bin/env python

def interpret(final, to_interpret):
    for line in to_interpret:
        if line.find("include") != -1:
            final.append(parse_it("html/" + line.split("'")[1]))
        else:
            final.append(line) ### TODO : big parsing here
    return final

def parse_it(filename):
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
            interpret(final, to_interpret)
        else:
            final.append(lines[i])
        i = i + 1
    return "\n".join(final)
