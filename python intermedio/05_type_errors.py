# 1. Genera un SyntaxError al imprimir una cadena sin parÃ©ntesis.
#print 'error'

# 2. Genera un NameError intentando usar una variable no definida.
#print(pepe)

# 3. Genera un IndexError accediendo a un Ã­ndice inexistente de una lista.
lista = [1,2,3,4,4]
#print(lista[9])

# 4. Genera un ModuleNotFoundError al importar un mÃ³dulo inexistente.
#import pakitomioo

# 5. Genera un AttributeError accediendo a un atributo que no existe.

import math

#math.bacalao

# 6. Genera un KeyError al acceder a una clave inexistente de un diccionario.

diccionario = {'primero':'el rikitaun','segundo':'el cruzaito','tercero':'el maikel jason'}

#diccionario['cuatro']

# 7. Genera un TypeError usando tipos incorrectos (Ã­ndice string en lista).

#lista['cuatro']

# 8. Genera un ImportError al importar una funciÃ³n que no existe desde un mÃ³dulo.

#from math import PI

# 9. Genera un ValueError intentando convertir un string no numÃ©rico a entero.

nombre = 'julian'
#int(nombre)

# 10. Intenta detectar si un error ocurre usando try-except con un KeyError.

try :
    diccionario['cuatro']
except KeyError as k:
    print(f'esa clave te la has inventado y este error has logrado : {k}')