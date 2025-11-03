# 1. Crea una lista con los nÃºmeros del 1 al 5 e imprÃ­mela.
lista = [1,2,3,4,5]
print(lista)
# 2. Accede e imprime el tercer elemento de la lista [10, 20, 30, 40, 50].
lista_2 = [10,20,30,40,50]
print(lista_2[3])
# 3. Agrega el nÃºmero 6 al final de la lista [1, 2, 3, 4, 5] e imprÃ­mela.
lista.append(6)
print(lista)
# 4. Inserta el nÃºmero 15 en la posiciÃ³n 2 de la lista [10, 20, 30, 40, 50].
lista_2.insert(2,15)
print(lista_2)
# 5. Elimina el primer valor 30 de la lista [10, 20, 30, 30, 40, 50].
lista_3=[10,20,30,30,40,50]
lista_3.remove(30)
# 6. Usa la funciÃ³n pop() para eliminar el Ãºltimo elemento de la lista [1, 2, 3, 4, 5] y almacÃ©nalo en una variable. Imprime la variable y la lista.
ultimo_elemento =lista.pop()
print(lista)
print(ultimo_elemento)
# 7. Invierte la lista [100, 200, 300, 400, 500] e imprÃ­mela.
lista_cienes=[100,200,300,400,500]
lista_cienes.reverse()
print(lista_cienes)
# 8. Ordena la lista [3, 1, 4, 2, 5] en orden ascendente e imprÃ­mela.
lista_desordenada=[3,1,4,2,5]
lista_desordenada.sort()
print(lista_desordenada)
# 9. Concatena las listas [1, 2, 3] y [4, 5, 6] y almacena el resultado en una nueva lista. Imprime la lista resultante.
lista_peq_1=[1,2,3]
lista_peq_2=[4,5,6]
lista_peq=lista_peq_1+lista_peq_2
print(lista_peq)
# 10. Crea una sublista con los elementos de la lista [10, 20, 30, 40, 50] que van desde la posiciÃ³n 1 hasta la 3 (sin incluir la posiciÃ³n 3).
lista_dieces=[10,20,30,40,50]
lista_final=[lista_dieces[1:3]]
print(lista_final)