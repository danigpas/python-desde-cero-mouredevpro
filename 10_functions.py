# 1. Crea una funciÃ³n llamada "personalized_greeting" que reciba un nombre como argumento e imprima "Hola, <nombre>". Si no se proporciona ningÃºn nombre, debe saludar diciendo "Hola, desconocido".
def personalized_greeting(nombre='desconocido'):
    print(f'Hola, {nombre}')

personalized_greeting('perico')
personalized_greeting()

# 2. Escribe una funciÃ³n llamada "multiply" que reciba dos nÃºmeros como argumentos y retorne el resultado de multiplicarlos.

def multiply(number_1, number_2):
    return number_1 * number_2

print(multiply(3, 6))

# 3. Crea una funciÃ³n llamada "is_even" que reciba un nÃºmero entero como argumento y retorne True si es par y False si es impar.

def is_even(number):
    if number % 2 == 0:
        return True
    else :
        return False
    
print(is_even(46))
print(is_even(43))

# 4. Escribe una funciÃ³n llamada "convert_to_uppercase" que reciba una cadena de texto y la retorne en mayÃºsculas.

def conver_to_uppercase(text):
    return text.upper()

print(conver_to_uppercase('holaaaaaa'))

# 5. Crea una funciÃ³n llamada "arbitrary_sum" que reciba un nÃºmero arbitrario de nÃºmeros como argumentos y retorne la suma de todos ellos.

def arbitrary_sum(*numbers):
    sum = 0
    for number in numbers:
        sum = sum + number
    
    return sum

print(arbitrary_sum(1,4,5,6,6,6,66,78,65,45))

# 6. Escribe una funciÃ³n llamada "generate_full_greeting" que reciba dos argumentos: nombre y apellido, y retorne el saludo completo "Hola, <nombre> <apellido>". Los argumentos deben ser pasados por clave.

def generate_full_greeting(nombre, apellido):
    return f'Hola , {nombre} {apellido}'

print(generate_full_greeting('dani','gonzalez'))

# 7. Crea una funciÃ³n llamada "power" que reciba dos nÃºmeros: base y exponente, y retorne el resultado de elevar la base al exponente.

def power(base, exponente):
    return base **exponente

print(power(2,3))

# 8. Escribe una funciÃ³n llamada "calculate_average" que reciba tres nÃºmeros y retorne su promedio.

def calculate_average(one, two, three):
    return (one + two + three)/ 3

print(calculate_average(4,6,8))

# 9. Crea una funciÃ³n llamada "count_characters" que reciba una cadena de texto y retorne el nÃºmero de caracteres que contiene.

def count_characters(text):
    suma = 0
    for char in text:
        suma +=1
    return suma

print(count_characters('hola, esto es un texto'))

# 10. Escribe una funciÃ³n llamada "display_messages" que reciba un nÃºmero indefinido de cadenas y las imprima en mayÃºsculas, una por una, tal como se hizo en el archivo proporcionado.

def display_messages(*cadenas):
    for cadena in cadenas:
        print(cadena)

display_messages('hola','adios','buenas','y por fin acabó')