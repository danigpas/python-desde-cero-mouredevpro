# 1. Crea una funciÃ³n que intente dividir dos nÃºmeros proporcionados por el usuario. Usa try-except para capturar cualquier error de divisiÃ³n (por ejemplo, divisiÃ³n por cero).

def dividir(num1 , num2):
    try:
        resultado= num1 / num2
    except Exception as e:
        print(f"Error al dividir: {e}")

    return resultado


# 2. Crea una funciÃ³n que tome una cadena e intente convertirla en un nÃºmero entero. Usa try-except para capturar cualquier error en la conversiÃ³n.

def cadena_to_int(cadena):
    try:
        return int(cadena)
    except Exception as e:
        print(f"Error al dividir: {e}")
        

# 3. Crea una funciÃ³n que abra un archivo, lea su contenido y maneje posibles errores (por ejemplo, archivo no encontrado). Usa try-except para gestionar las operaciones de archivos de forma segura.

def leer_archivo(path):
    try:
        with open(path,'r') as archivo:
            print(archivo.read())
    except Exception as e:
        print(f'error al abrir el archivo en el path {path}')



# 4. Crea una funciÃ³n que realice mÃºltiples operaciones (suma, resta, divisiÃ³n, multiplicaciÃ³n) con dos nÃºmeros. Usa try-except-else-finally para manejar errores y asegurar que se imprima un mensaje final, independientemente de los errores.

def operaciones(num1,num2):
    try:
        result = num1 /num2
        print(result)
    except Exception as e:
        result = num1* num2
        print(f'multiplicacion = {result}')
    else:
        result= num1 + num2
        print(f'suma = {result}')
    finally:
        result = num1 -  num2
        print(f'resta = {result}')

# 5. Crea una funciÃ³n que le pida al usuario su edad y lance un ValueError si la entrada no es un nÃºmero entero positivo. Usa el manejo de excepciones para gestionar la entrada y lanzar excepciones personalizadas cuando sea necesario.

def muestra_edad():
    try:
        edad = int(input('introduzca su edad por favor'))
        if edad <= 0:
            raise ValueError('la edad debe de ser mayor a cero')
        return edad
    except ValueError as e:
        print('por favor debe de introducir un numero entero positivo')



# 6. Crea una funciÃ³n que intente acceder a un elemento de una lista por Ã­ndice. Usa try-except para manejar el caso donde el Ã­ndice estÃ© fuera de rango.

def indice_lista(indice,lista):
    try:
        return lista[indice]
    except IndexError as ind:
        print('el indice esta fuera de rango, error')
    except Exception as e:
        print(f'error al acceder al indice {indice} de la lista {lista}')

# 7. Crea una funciÃ³n que use try-except para manejar mÃºltiples excepciones: ZeroDivisionError, ValueError y TypeError.

def manejo_multiples_excepciones(num1, num2):
    try:
        result = num1/num2
        print(result)
    except ZeroDivisionError as zero:
        print('error, no se puede dividir por cero')
    except ValueError as value:
        print(f'error el valor no es correcto -> {value}')
    except TypeError as typo:
        print(f'error, el tipo de dato no es correcto -> {typo}')

# 8. Crea una funciÃ³n que simule una transacciÃ³n. Lanza una excepciÃ³n personalizada llamada InsufficientFundsError si el saldo es menor que la cantidad a retirar.

class InsufficientFundsError(Exception):
    """Excepción lanzada cuando no hay fondos suficientes para realizar la operación."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Fondos insuficientes: saldo actual {balance}, intento de retiro {amount}")

def realizar_transaccion(saldo, cantidad_retirar):
    try:
        print(f"Intentando retirar {cantidad_retirar} de un saldo {saldo}")
        if saldo < cantidad_retirar:
            raise InsufficientFundsError(saldo, cantidad_retirar)
        saldo -= cantidad_retirar
        print(f"✅ Transacción exitosa. Saldo restante: {saldo}")
    except InsufficientFundsError as e:
        print(f"❌ Error en transacción: {e}")


# 9. Crea una funciÃ³n que intente convertir una lista de cadenas en enteros. Maneja cualquier error que surja cuando una cadena no pueda convertirse.

def convert_list_to_int(lista):
    int_list=[]
    
    for element in lista:
        try:
            int_list.append(int(element))
        except ValueError as e:
            print(f'Error a la hora de transformar el elemento {element} de la lista {lista}')
    return int_list

# 10. Crea una funciÃ³n que calcule la raÃ­z cuadrada de un nÃºmero. Lanza un ValueError si el nÃºmero es negativo.
import math

def raiz_cuadrada(number):
    try:
        raiz = math.sqrt(number)
    except ValueError as e:
        print(f'error , el numero es negativo ')
