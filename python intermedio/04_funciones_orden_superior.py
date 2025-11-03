# 1. Crea una funciÃ³n que reciba una funciÃ³n y un nÃºmero, y devuelva el resultado de aplicar la funciÃ³n al nÃºmero.
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
lista=list(range(0,11))
map(lambda i  )

# 5. Usa filter() con lambda para quedarte solo con los nÃºmeros pares.

# 6. Usa reduce() con lambda para obtener la suma total de una lista.

# 7. Escribe una funciÃ³n que devuelva una funciÃ³n que reciba un nombre y devuelva â€œHola, â€.

# 8. Crea una funciÃ³n que reciba una lista y una funciÃ³n, y cuente cuÃ¡ntos elementos cumplen con la funciÃ³n.

# 9. Crea una funciÃ³n que reciba dos funciones y un nÃºmero, y las aplique en orden.

# 10. Crea una funciÃ³n que reciba una lista y una funciÃ³n, y aplique esa funciÃ³n a cada elemento usando un bucle (sin map).