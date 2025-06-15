# 1. Declara y asigna valores a las siguientes variables:
# â€¢	name: una cadena que contenga tu nombre.
# â€¢	age: un nÃºmero entero que represente tu edad.
# â€¢	height: un nÃºmero flotante que represente tu altura.
# â€¢	Imprime cada variable en una lÃ­nea separada.

name='daniel'
age = 26
height=1.90
print(name)
print(age)
print(height)
# 2. Convierte la variable edad de entero a cadena y concatenala con un texto que diga cuÃ¡ntos aÃ±os tienes.

age = str(age)
print('tengo',age,'años')
# 3. Declara una variable booleana is_student que indique si eres estudiante o no. Usa True o False segÃºn corresponda e imprÃ­mela.
is_student=False

print('soy estudiante?',is_student)
# 4. Usa la funciÃ³n len() para calcular cuÃ¡ntos caracteres tiene tu nombre completo, almacenado en una variable.
longitud_nombre=len(name)
print('mi nombre tiene:',longitud_nombre,'caracteres')
# 5. Declara tres variables en una sola lÃ­nea que representen tu nombre, apellido y ciudad de origen. Luego, imprime estos valores.
name,surname,city='daniel','gonzalez pascual', 'malaga'
print(name,surname,city)
# 6. Usa la funciÃ³n input() para solicitar al usuario su color favorito y almacÃ©nalo en una variable color. Luego, imprime el valor ingresado.
color=input('introduzca su color favorito por favor')
print('el resultado es:',color)
# 7. Declara una variable fruit e inicialÃ­zala con un valor. Luego, cambia el valor de la fruta a otro diferente y vuelve a imprimirla.
fruit='melon'
print(fruit)
fruit='orange'
print(fruit)
# 8. Convierte un nÃºmero decimal, almacenado en la variable price, a un nÃºmero entero y luego imprÃ­melo.
number=3.14
number=int(number)
print(number)
# 9. Declara una variable llamada address_len y almacena en ella la cantidad de caracteres de una direcciÃ³n usando la funciÃ³n len(). Imprime el resultado.
address_len='calle pescabicho 4'
print(len(address_len))
# 10. Usa un tipo de dato forzado para declarar una variable phone, asegurÃ¡ndote de que siempre serÃ¡ un nÃºmero. Luego, cambia su valor a un nÃºmero diferente y verifica el tipo de la variable con type().
phone:int=123
phone=456
print(type(phone))