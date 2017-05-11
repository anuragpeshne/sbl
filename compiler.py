#! /usr/bin/env python

from sys import stdin

if __name__ == "__main__":
    compile_()

def compile_():
    tokens = []
    for c in stdin.read():
        if c == '(':
            tokens.append(LPAREN)
        else if c == ')':
            tokens.append(RPAREN)
        else if isDigit(c):
            tokens.append(NUM(scanNum()))
        else if isChar(c):
            string = scanStr()
            if string == 'lambda':
                tokens.append(LAMBDA)
            else:
                tokens.append(IDEN(string))
        else:
            raise Error("unknown char" + c)

    return tokens

def parse():
    for token in tokens:
        if token == LPAREN:
            parse(tokens)
