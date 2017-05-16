#! /usr/bin/env python

from sys import stdin

class IDENT:
    def __init__(string):
        self.name = string

class LAMBDA:
    def __init__():
        pass

def isDigit(c):
    return ord(c) >= ord('0') and ord(c) <= ord('9')

def scanNum(num, inp):
    num = num * 10 + ord(inp[0])
    if isDigit(inp[1:]):
        return scanNum(num, inp[1:])
    else:
        return num

def isAlpha(c):
    return ((c[0] >= 'A' and c[0] <= 'Z') or
            (c[0] >= 'a' and c[0] <= 'z'))

def scanStr(string, inp):
    string = string + inp[0]
    if isAlpha(inp[0]):
        return scanStr(string, inp[1:])
    else:
        return string

# (+ 2 3)
# parse-sexp
# parse-nextExp
def parse(inp):
    ast = []
    if (len(inp) <= 0 or inp[0] == ')'):
        return ast
    elif inp[0] == '(':
        ast.append(parse(inp[1:]))
    elif isDigit(inp[0]):
        tokens.append(scanNum(0, inp))
    elif isAlpha(inp[0]):
        string = scanStr('', inp)
        if string == 'lambda':
            tokens.append(LAMBDA())
        else:
            tokens.append(IDEN(string))
    else:
        raise SyntaxError("unknown char" + inp[0])

if __name__ == "__main__":
    inp = stdin.read()
    ast = parse(inp)
    print ast
