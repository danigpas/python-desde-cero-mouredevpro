# 1. Crea un mÃ³dulo llamado "calculator" que contenga funciones para sumar, restar, multiplicar y dividir dos nÃºmeros. Importa este mÃ³dulo en otro archivo y usa sus funciones.

from calculator import sumar,restar,dividir,multiplicar

print(sumar(3,4))
print(restar(5,5))
print(multiplicar(9,9))
print(dividir(900,10)
)
# 2. Crea un mÃ³dulo llamado "converter" que tenga funciones para convertir temperaturas entre Celsius y Fahrenheit. Escribe un programa que importe este mÃ³dulo y realice conversiones.

from converter import celsius_to_farenheit, farenheit_to_celsius

print(celsius_to_farenheit(35))
print(farenheit_to_celsius(90))
# 3. Crea un mÃ³dulo que contenga una lista de nombres de estudiantes y una funciÃ³n que imprima todos los nombres. Importa este mÃ³dulo en otro archivo y usa la funciÃ³n para mostrar la lista.

import students

students.muesdtra_students(students.students)

# 4. Crea un mÃ³dulo llamado "geometry" que tenga una funciÃ³n para calcular el Ã¡rea de un cÃ­rculo y un cuadrado. Usa este mÃ³dulo en otro archivo para calcular Ã¡reas.

from geometry import area_circulo, area_cuadrado

print(area_circulo(4.5))
print(area_cuadrado(45))


# 5. Escribe un mÃ³dulo que contenga una funciÃ³n que acepte cualquier nÃºmero de argumentos y devuelva su suma. Importa y usa la funciÃ³n en otro archivo.

from calculator import sum_all

print(sum_all(4,4,4,4,5,6,7,6,6,6,2))

# 6. Crea un mÃ³dulo que defina una clase llamada "Car" con propiedades como marca, modelo y aÃ±o. Importa este mÃ³dulo en otro archivo y crea una instancia de la clase "Car".
from coche import Car

fiat = Car('fiat',500,2019)

# 7. Escribe un mÃ³dulo que contenga funciones para leer y escribir en archivos de texto. Crea un programa que use estas funciones para escribir y leer datos.

from opera_archivos import escribir_archivo, leer_archivo

escribir_archivo('ejemplo.txt','holaaaaa')
leer_archivo('ejemplo.txt')

# 8. Crea un mÃ³dulo llamado "statistics" que tenga funciones para calcular la media y la mediana de una lista de nÃºmeros. Usa este mÃ³dulo para calcular estos valores en una lista dada.

from statistics import media, mediana
media(4,5,5,5)
mediana(5,5,5,5,5,55,5,6)


# 9. Crea un mÃ³dulo que contenga una funciÃ³n para contar cuÃ¡ntas veces aparece una palabra en un texto. Escribe un programa que importe el mÃ³dulo y lo use para contar palabras en una cadena.

from cuentacuentos import cuenta_palabras
cuenta_palabras('esto es un cuento dani sobre la gente quie dani conoce p[ero ] no se llama dani ajajajaj dani dnaindndanidaidn','dani')

# 10 Crea un mÃ³dulo llamado "dates" que contenga funciones para obtener la fecha actual y calcular la diferencia entre dos fechas. Usa este mÃ³dulo en un programa para mostrar la fecha actual y la diferencia entre dos fechas especÃ­ficas.

from dates import fecha_actual, diferemcia_fechas

fecha_actual()
diferemcia_fechas('2025-12-25','2024-03-30')