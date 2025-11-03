# 1. Genera una lista utilizando comprensiÃ³n con los nÃºmeros del 0 al 10.

lista = [i for i in range(11)]
# 2. Crea una lista utilizando comprensiÃ³n con los cuadrados de los nÃºmeros del 1 al 10.
lista_2 = [i*i for i in lista]
# 3. Genera una lista utilizando comprensiÃ³n con los nÃºmeros pares del 0 al 20.
def is_par(number : int):
    if number % 2 == 0 :
        return number
    

lista_3 = [ is_par(i)  for i in range(21) if is_par(i) != None]
print(lista_3)
# 4. Convierte una lista de temperaturas en Celsius a Fahrenheit utilizando comprensiÃ³n.
lista_celsius = [12,34,12,11,43,34,33,32]
lista_farenheit = [i+32 for i in lista_celsius]
# 5. Crea una lista utilizando comprensiÃ³n con los caracteres de una cadena.

lista_palabra = [i for i in 'palabra']
print (lista_palabra)
# 6. Filtra una lista de palabras y deja solo las que tienen mÃ¡s de 4 letras utilizando comprensiÃ³n.
lista_palabras = ['hola','donpepito','pepe','donjose']
lista_menor4 = [i for i in lista_palabras if len(i) > 4]
print(lista_menor4)
# 7. Aumenta en 5 cada nÃºmero de una lista con comprensiÃ³n usando una funciÃ³n externa.

def add_5 (number : int):
    return number + 5

list_add5 = [add_5(i) for i in range(20)]
print(list_add5)
# 8. Crea una lista de booleanos que indique si cada nÃºmero es mayor que 10 utilizando comprensiÃ³n.

def is_true (number : int):
    if number > 10 :
        return True
    else : return False

numeros = [12,4,3,5,123,123,34,54,3,121,10,12]

list_bigger10 = [is_true(i) for i in numeros]
print(list_bigger10)

# 9. Multiplica solo los nÃºmeros impares por 3 en una lista utilizando comprensiÃ³n.
list_impares = [i *3 for i in numeros if i % 2 != 0]
print(list_impares)

# 10. Usa comprensiÃ³n de listas anidada para generar una matriz 3x3 con nÃºmeros del 1 al 9.

matriz_1 = [i for i in range(10)]
matriz_2 = [i for i in range(10)]
matriz_3 = [i for i in range(10)]

matriz = matriz_1 + matriz_2 + matriz_3

print(matriz)

matrix = [[row * 3 + col + 1 for col in range(3)] for row in range(3)]
print(matrix)