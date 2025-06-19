# 1. Crea una tupla con los valores (10, 20, 30, 40, 50) e imprÃ­mela.
tupla=(10,20,30,40,50)
print(tupla)
# 2. Accede al segundo elemento de la tupla (100, 200, 300, 400, 500) y muÃ©stralo.
tupla_cienes=(100,200,300,400,500)
print(tupla_cienes[1])
# 3. Intenta modificar el primer elemento de la tupla (1, 2, 3) a 10 y observa el resultado.
tupla_uno=(1,2,3)
#tupla_uno[0]=10 -> Da error porque una tupla una vez creada es inmutable, por lo tanto no se puede alterar su valor en ningun indice

print(tupla_uno)
# 4. Cuenta cuÃ¡ntas veces aparece el nÃºmero 3 en la tupla (1, 2, 3, 3, 4, 5, 3).
tupla_4=(1, 2, 3, 3, 4, 5, 3)
print(tupla_4.count(3))
# 5. Encuentra el Ã­ndice de la primera apariciÃ³n de la cadena "Python" en la tupla ("Java", "Python", "JavaScript", "Python").
tupla_textos=("Java", "Python", "JavaScript", "Python")
print(tupla_textos.index("Python"))
# 6. Concatena dos tuplas: (1, 2, 3) y (4, 5, 6) e imprime la tupla resultante.
tupla_peq_1=(1,2,3)
tupla_peq_2=(4,5,6)
tupla_peq_max=tupla_peq_1+tupla_peq_2
print(tupla_peq_max)
# 7. Crea una subtupla con los elementos desde la posiciÃ³n 2 hasta la 4 (sin incluir la 4) de la tupla (10, 20, 30, 40, 50).
tupla_sub=tupla[2:3]
print(tupla_sub)
# 8. Convierte la tupla ("rojo", "verde", "azul") en una lista, cambia el segundo elemento a "amarillo" y vuelve a convertirla en una tupla. Imprime la tupla resultante.
tupla_colores= ("rojo", "verde", "azul")
lista_colores=list(tupla_colores)
print(f'el tipo de la lista {lista_colores} es ',type(lista_colores))
# 9. Elimina una tupla llamada my_tuple usando del y luego intenta imprimirla para ver el resultado.
my_tuple = (1,2,3,3,3,3,4)
del my_tuple
#print (my_tuple) -> da error porque al eliminarla no existe ninguna variable con ese nombre y el interprete te dice my_tuple is not defined NameError

# 10. Crea una tupla con un solo elemento (el nÃºmero 100) e imprÃ­mela. AsegÃºrate de usar la sintaxis correcta para crear una tupla con un solo elemento.
tupla_unica=(100,)
print(tupla_unica)
print(type(tupla_unica))