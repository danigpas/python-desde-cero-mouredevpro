# 1. Crea un set con los nÃºmeros del 1 al 5 e imprÃ­melo.
set= {1,2,3,4,5}
print(set)

# 2. AÃ±ade el nÃºmero 6 al set {1, 2, 3, 4, 5} e imprÃ­melo.
set.add(6)
print(set)

# 3. Intenta aÃ±adir el nÃºmero 5 al set {1, 2, 3, 4, 5} nuevamente. Â¿QuÃ© sucede?
set.add(5)
print(set) #Que un set no admite duplicados, no hace nada

# 4. Verifica si el nÃºmero 3 estÃ¡ en el set {1, 2, 3, 4, 5} e imprime el resultado.

set_tres={3}
print(set_tres.issubset(set))

# 5. Elimina el nÃºmero 4 del set {1, 2, 3, 4, 5} e imprime el set resultante.
set.discard(4)
print(set)

# 6. Usa el mÃ©todo clear() para vaciar un set y luego imprime su longitud.
set.clear()
print(len(set))
# 7. Convierte el set {"manzana", "naranja", "plÃ¡tano"} en una lista e imprime el primer elemento de la lista.

set_frutas= {"manzana", "naranja", "platano"}
lista=list(set_frutas)
print(lista[1])
# 8. Realiza la uniÃ³n de dos sets: {1, 2, 3} y {4, 5, 6}, e imprime el set resultante.
set_peq={1,2,3}
set_peq_dos={4,5,6}
print(set_peq.union(set_peq_dos))
# 9. Calcula la diferencia entre los sets {1, 2, 3, 4} y {3, 4, 5, 6} e imprime el resultado.
set_dif={1,2,3,4}
set_dif_2={3,4,5,6}
print(set_dif.difference(set_dif_2))

# 10. Elimina un set llamado my_set usando del y luego intenta imprimirlo para ver el resultado.

my_set={2,3,3,3,3,4,5}
del my_set#No se puede imprimir prque hemos borrado la unica variable con dicho nombre