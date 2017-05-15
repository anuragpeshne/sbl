#! /usr/bin/env python

from sys import stdin

def isDigit(c):
    return ord(c) >= ord('0') and ord(c) <= ord('9')

# (+ 2 3)
# parse-sexp
# parse-nextExp
def parse(inp, loc):
    ast = []
    while loc < len(inp) and inp[loc] != ')':
        if inp[loc] == '(':
            ast.append(parse(inp), loc + 1)
        elif inp[loc] == ')':
            return ast
        elif isDigit(inp[loc]):
            tokens.append(scanNum(inp, loc + 1))
        elif isChar(inp[loc]):
            string = scanStr()
            if string == 'lambda':
                tokens.append(LAMBDA)
            else:
                tokens.append(IDEN(string))
        else:
            raise Error("unknown char" + inp[loc])

    return ast

def parse():
    for token in tokens:
        if token == LPAREN:
            parse(tokens)

if __name__ == "__main__":
    compile_()
