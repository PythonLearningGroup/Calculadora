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
    elif has_operators(lista[0]) or has_digit(lista[0]):
        retorno.append(lista[0])
    return unfold_list(lista[1:], retorno)


def handle_operators(cadena, retorno=[]):
    """ Si encuentra mas de un operador juntos, los separa """
    if not len(cadena):
        return retorno
    retorno.append(cadena[0])
    return handle_operators(cadena[1:], retorno)


def handle_mixed(cadena, index, retorno=[]):
    if not cadena:
        return retorno
    elif len(cadena) == index:
        retorno.append(cadena)
        return retorno

    if has_operators(cadena[index]):
        if not index:
            retorno.append(cadena[index])
        else:
            retorno.append(cadena[:index])
            retorno.append(cadena[index])
        return handle_mixed(cadena[index + 1:], 0, retorno)

    else:
        return handle_mixed(cadena, index + 1, retorno)


def splitter(arg):
    """ Funcion que maneja a los operadores y los valores mixtos entre operador y numero """
    try:
        convercion = float(arg)
        return convercion
    except ValueError:
        if not has_digit(arg):
            return handle_operators(arg, [])
        elif has_digit(arg) and has_operators(arg):
            return handle_mixed(arg, 0, [])
        else:
            return ''

def tokenize(expression):
    """ Función encargada de convertir una expresión en una lista de tokens """
    tokens = expression.split(' ')
    print(tokens)
    tokens = list(map(splitter, tokens))
    return unfold_list(tokens)
    # print(tokens)


print(tokenize('3+4 *w(2+1)'))

