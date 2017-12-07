#! /bin/python
""" Tokenizer, convierte una expresión matemática en una lista de tokens """

import re
from functools import reduce

def has_digit(arg):
    """ Evalua si existen digitos en el argumento """
    match = re.search(r'\d', arg)
    return bool(match)


def has_operators(arg):
    """ Evalua si existe un operador en el argumento """
    expresiones = (r'\+', r'\-', r'\*', r'\/', r'\(', r'\)')
    resultados = map(lambda x: re.search(x, arg), expresiones)
    return reduce(lambda c, x: c or bool(x), resultados, False)


def unfold_list(lista, retorno=[]):
    """ Funcion que aplana una lista que puede contener listas recursivamente en su interior """
    if not lista:
        return retorno
    if isinstance(lista[0], list):
        retorno += unfold_list(lista[0], [])
    else:
        retorno.append(lista[0])
    return unfold_list(lista[1:], retorno)


def handle_operators(cadena, retorno=[]):
    """ Si encuentra mas de un operador juntos, los separa """
    if not cadena:
        return retorno
    retorno.append(cadena[0])
    return handle_operators(cadena[1:], retorno)


def splitter(arg):
    """ Funcion que maneja a los operadores y los valores mixtos entre operador y numero """
    try:
        return float(arg)
    except ValueError:
        if has_operators(arg) and not has_digit(arg):
            return handle_operators(arg)
        else:
            print("valores mixtos")


def tokenize(expression):
    """ Función encargada de convertir una expresión en una lista de tokens """
    tokens = expression.split(' ')
    tokens = list(map(splitter, tokens))
    return unfold_list(tokens)
