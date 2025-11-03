# 1. Crea una lambda que sume dos nÃºmeros.
result = lambda num1, num2 : num1 + num2
print(result(4,5))
# 2. Crea una lambda que calcule el cuadrado de un nÃºmero.
result = lambda num1 : num1**2
print(result(4))
# 3. Crea una lambda que devuelva el mayor de dos nÃºmeros.
result = lambda num1, num2 : num1 if num1 > num2  else  num2
print(result(4,5))
# 4. Crea una lambda que sume 10 a un nÃºmero dado.
result = lambda num1 : num1 + 10
print(result(5))
# 5. Crea una lambda que devuelva el Ãºltimo carÃ¡cter de una cadena.
result = lambda str1 : str1[-1]
print(result('antonio'))
# 6. Crea una lambda que indique si una palabra tiene mÃ¡s de 6 letras.
result = lambda palabra : True if len(palabra) > 6 else False
print(result('tralalerotralala'))
# 7. Crea una lambda que convierta una cadena a minÃºsculas.
result = lambda palabra : palabra.lower()
print(result('PEPE'))
# 8. Crea una lambda que devuelva True si un nÃºmero es positivo.
result = lambda number : True if number >= 0 else False
print(result(4))
# 9. Crea una lambda que devuelva "Cadena vacÃ­a" si el string estÃ¡ vacÃ­o.
result = lambda palabra : "Cadena vacia" if not palabra else None
print(result(''))
# 10. Crea una lambda que calcule el precio final con un impuesto aÃ±adido del 21%.
result = lambda precio : precio * 1.21
print(result(45))