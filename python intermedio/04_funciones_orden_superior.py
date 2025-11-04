# 1. Crea una funciÃ³n que reciba una funciÃ³n y un nÃºmero, y devuelva el resultado de aplicar la funciÃ³n al nÃºmero.
from functools import reduce


def funcion(numero):
    return numero + 5

def ejemplo (numero, funcion):
    return funcion(numero)

# 2. Crea una funciÃ³n que reciba dos nÃºmeros y una funciÃ³n, y devuelva el resultado de sumar los dos nÃºmeros y aplicar la funciÃ³n.
def tres_parametros(num1, num2, funcion):
    num3 = num1 + num2
    return funcion(num3)

# 3. Crea una funciÃ³n que devuelva otra funciÃ³n que sume un nÃºmero fijo.

def tres_parametros(num1, num2, funcion):
    num3 = num1 + num2
    return funcion(num3)

# 4. Usa map() con lambda para multiplicar cada nÃºmero de una lista por 10.
lista=[12,3,45,123,12,43,53,2]
mapita = list(map(lambda i : i * 10,lista ))
print(mapita)

# 5. Usa filter() con lambda para quedarte solo con los nÃºmeros pares.

filtro = list(filter(lambda i :i if i % 2 == 0 else None, lista))
print(filtro)

# 6. Usa reduce() con lambda para obtener la suma total de una lista.

reduccione=reduce(lambda num1, suma : num1 + suma ,lista)
print(reduccione)

# 7. Escribe una funciÃ³n que devuelva una funciÃ³n que reciba un nombre y devuelva â€œHola, â€.

def saludo(nombre):
    return f'Hola , {nombre}'

def fun1(nombre):
    return saludo(nombre)

print(fun1('pakito'))

# 8. Crea una funciÃ³n que reciba una lista y una funciÃ³n, y cuente cuÃ¡ntos elementos cumplen con la funciÃ³n.

def mayor_a_10(num):
    return num > 10

def fun4 (lista : list,funcion):
    contador = 0
    for num in lista:
        if funcion(num) : contador += 1
    return contador

print(fun4([12,4,5,67,213,1,34,55],mayor_a_10))

# 9. Crea una funciÃ³n que reciba dos funciones y un nÃºmero, y las aplique en orden.

def por10(number):
    return number * 10

def entre2(numh):
    return numh/2

def dos_fun_y_number(fun1, fun2, number):
    result=fun1(number)
    return fun2(result)

print(dos_fun_y_number(por10,entre2,200))

# 10. Crea una funciÃ³n que reciba una lista y una funciÃ³n, y aplique esa funciÃ³n a cada elemento usando un bucle (sin map).

def suma_10(num):
    return num + 10

def fun4 (lista : list,funcion):
    resultado = 0
    for num in lista:
        resul = resultado + funcion(num)
        resultado = resul 
    
    return resultado

print(fun4([12,4,5,67,213,1,34,55],suma_10))