# 1. Usa un bucle while para imprimir los nÃºmeros del 1 al 10.

number=1
while number < 11 :
    
    print(number)
    number+=1

# 2. Usa un bucle for para recorrer la lista[10, 20, 30, 40, 50] e imprime cada nÃºmero.
lista=[10, 20, 30, 40, 50]
for item in lista:
    print(item)

# 3. Escribe un programa que use un bucle while para sumar los nÃºmeros del 1 al 100 e imprime el resultado.
number_two = 0
sum = 0
while number_two < 100 :
    number_two +=1
    sum = number_two + sum
else:
    print(sum)
    
# 4. Escribe un bucle for que imprima cada carÃ¡cter de la cadena "Python".
cadena='python'
for caracter in cadena:
    print(caracter)
    
# 5. Usa un bucle while para encontrar el primer nÃºmero divisible por 7 entre 1 y 50.
number_three = 1
while number_three < 50 and number_three % 7 !=0:
    number_three +=1
else:
    print(number_three)
# 6. Usa un bucle for para recorrer el diccionario {"name": "Brais", "age": 37, "country": "Galicia"} e imprime las claves.

diccionario = {"name": "Brais", "age": 37, "country": "Galicia"}

for clave, valor in diccionario.items():
    print(clave)
    
# 7. Escribe un programa que use un bucle while para imprimir los nÃºmeros pares entre 1 y 20.
numeros = 1 

while numeros <= 20 :
    if numeros %2 == 0 :
        print (numeros)
    numeros +=1
    
# 8. Usa un bucle for con la funciÃ³n range() para imprimir los nÃºmeros del 1 al 10 en orden inverso.

for element in range(10,0, -1):
    print(element)
    
# 9. Escribe un programa que use un bucle for para contar cuÃ¡ntas veces aparece el nÃºmero 30 en la lista[30, 10, 30, 20, 30, 40].
lista_dos = [30, 10, 30, 20, 30, 40]
sum = 0
for numero in lista_dos:
    
    if numero == 30 :
        sum +=1
print(f'El numero 30 aparece {sum} veces')
# 10. Usa un bucle for para recorrer una lista de nombres y detener el bucle cuando se encuentre el nombre "Brais".

lista_nombres = ['pepe', 'paco','dani','brais','antonio']

for nombre in lista_nombres:
    if nombre.upper() == 'BRAIS':
        print('Hemos encontrado el nomnbre de brais')
        break
    print(nombre)