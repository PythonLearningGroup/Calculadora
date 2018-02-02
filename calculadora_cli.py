#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from tokenize import tokenize


def validate_token(token):
    return token.isnumeric() or is_operator(token)


def validate_tokens(tokens):
    for token in tokens:
        if not validate_token(token):
            return False
    return True


def is_operator(character):
    return character == '*' or character == '/' or character == '+' or character == '-'


def evaluate(expresion):
    non_valid_expresion_error_message = "expresion inválida"
    tokens = tokenize(expresion)
    if validate_tokens(tokens):
        try:
            out = eval(expresion)
            print("resultado: " + str(out))
            return out
        except SyntaxError:
            print(non_valid_expresion_error_message)
        except ZeroDivisionError:
            print("Division por cero no esta definida")

    else:
        print(non_valid_expresion_error_message)

# if len(sys.argv) > 1:
#     evaluate(sys.argv[1])
# else:
#     print("usage: calculadora_cli.py <expresion>")