# 1. Declara una variable text con la frase â€œAprendiendo Pythonâ€ y luego imprime la longitud de la cadena usando len().
text = 'Aprendiendo Python'
print(len(text))

# 2. Concatena dos cadenas: â€œHolaâ€ y â€œPythonâ€, y muestra el resultado en una sola lÃ­nea.
print('hola ' + 'python')
# 3. Crea una cadena que incluya un salto de lÃ­nea, y luego imprÃ­mela para ver el resultado.
salto='esto es una cadena\n con un salto de linea'
print(salto)
# 4. Usa el formateo de cadenas con f-strings para imprimir tu nombre, apellido y edad en una cadena de texto.
name='daniel'
surname='Gonzalez pascual'
age=26
print(f'mi nombre es {name} {surname} y tengo {age} años')
# 5. Desempaqueta los caracteres de la palabra â€œPythonâ€ en variables separadas y luego imprÃ­melos uno por uno.
a,b,c,d,e,f='python'
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)


# 6. Extrae un â€œsliceâ€ de la palabra â€œProgramaciÃ³nâ€ para obtener los caracteres desde la posiciÃ³n 3 hasta la 7.
palabra='programacion'
print(palabra[2:7])
# 7. Invierte la cadena â€œPythonâ€ usando slicing y muestra el resultado.
cadena='python'
print(cadena[::-1])
# 8. Convierte la cadena â€œaprendiendo pythonâ€ en mayÃºsculas usando el mÃ©todo adecuado e imprÃ­mela.
learning='aprendiendo python'
print(learning.upper())

# 9. Cuenta cuÃ¡ntas veces aparece la letra â€œnâ€ en la cadena â€œProgramaciÃ³n en Pythonâ€.
cadena_45='Programación en python'
letra='a'
print(cadena_45.count(letra))

# 10. Verifica si la cadena â€œ12345â€ es numÃ©rica usando el mÃ©todo adecuado e imprime el resultado.
is_number='12345'
print(is_number.isnumeric())