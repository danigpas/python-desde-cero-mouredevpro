from math import pi, pow

def area_circulo(r):
    return pi * (pow(r,2))

#suponemos que es cuadrilatero, si es rectangulo seria lado * altura
def area_cuadrado(lado):
    return lado * lado
