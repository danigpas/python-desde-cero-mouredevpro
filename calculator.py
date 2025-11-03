def sumar(num1, sum2):
    return num1 + sum2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1,num2):
    return num1 * num2

def dividir(num1, num2):
    try:
        return num1 / num2
    except Exception as e:
        print(f'Error al intentar dividir los numeros {e}')

def sum_all(*args):
    return sum(args)