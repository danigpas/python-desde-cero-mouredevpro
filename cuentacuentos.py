import re


def cuenta_palabras(texto,busqueda):
    busqueda=busqueda.lower()
    texto=texto.lower()
    palabras= re.findall(r'\b\w+\b',texto)
    return print(palabras.count(busqueda))