# 1. Escribe un programa que verifique si un nÃºmero es positivo, negativo o cero.
numero =5

if numero > 0:
    print('el numero es positivo')
elif numero < 0:
    print('el numero es negativo')
else:
    print('el numero es cero')
    
# 2. Solicita al usuario que ingrese su edad y muestra un mensaje indicando si es mayor de edad(18 aÃ±os o mÃ¡s) o menor de edad.
edad=int(input('Ingrese su edad por favor'))

if edad < 18:
    print('el usuario es menor de edad')
else :
    print('el usuario es mayor de edad')
    
# 3. Escribe un programa que verifique si una cadena de texto estÃ¡ vacÃ­a y muestre un mensaje en consecuencia.

txt_vacio=""
if txt_vacio:
    print('la variable no está vacia')
else:
    print('la cadena de texto es vacia')
        
# 4. Crea un programa que solicite dos nÃºmeros al usuario y compare cuÃ¡l es mayor. Si son iguales, muestra un mensaje indicando la igualdad.
num_1= int(input('ingrese un numero por favor'))
num_2= int(input('ingrese otro numero por favor'))

if num_1 > num_2:
    print(f'el numero : {num_1} es mayor que {num_2}')
elif num_2 > num_1:
        print(f'el numero : {num_2} es mayor que {num_1}')
else:
    print(f'los numeros : {num_2}, {num_1} son iguales')
    
# 5. Escribe un programa que verifique si un nÃºmero es divisible por 3 y por 5 al mismo tiempo.
if numero % 5 == 0 and numero % 3 == 0:
    print('el numero es divisible entre tres y cinco')
else:
    print('el numero no es divisible ni entre 3 ni entre 5')
# 6. Solicita al usuario que ingrese un nÃºmero y verifica si es par o impar.

if numero % 2 == 0:
    print('el numero es par')
else :
    print('el numero es impar')

# 7. Escribe un programa que determine si una persona puede votar en funciÃ³n de su edad(mayor o igual a 18). Si tiene 16 o 17 aÃ±os, indica que puede votar con permiso especial.
if edad >= 18:
    print('el usuario peude votar')
elif edad == 17 or edad == 16:
    print('el usuario puede votar con permiso de sus padres')
else:
    print('el usuario no puede votar') 

# 8. Crea un programa que solicite una contraseÃ±a al usuario y verifique si coincide con una contraseÃ±a predefinida. Si no coincide, muestra un mensaje de error.
contraseña = input('ingrese una contraseña `pr favor')
ejemplo_pass='12345'
if contraseña == ejemplo_pass:
    print('macho te he pillado la contraseña')
else:
    print('Error, contraseña no adivinada por el programador ')
# 9. Escribe un programa que determine si un nÃºmero estÃ¡ entre 10 y 20 (ambos incluidos).

numero_entre= int(input ('ingrese un numero por favor'))
if numero_entre >= 10 and numero_entre <=20:
    print('enhorabuena su numero esta enrre 10 y 20')
    
# 10. Escribe un programa que simule un semÃ¡foro: solicita al usuario que ingrese un color(rojo, amarillo, verde) y muestra un mensaje indicando si debe detenerse, estar alerta o avanzar.

color = input ('por favor ingrese uno de estos tres colores (rojo, amarillo, verde)')

if color.upper() =='VERDE':
    print('puedes avanzar que está en verde, vamonoo')
elif color.upper() == 'AMARILLO':
    print('avanza con cuidado que esta en amarillo , OJO')
elif color.upper() == 'ROJO':
    print('quiero parao que está en rojo')
else :
    print('zoquete has escrito mal el color, bajate del coche que se lo lleva la grua')