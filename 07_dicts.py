# 1. Crea un diccionario con las claves name, age, y country, asignando valores a cada una. Imprime el diccionario.
dict={
    "name":"dani",
    "age": 26,
    "country":'spain'
}
print(dict)

# 2. Accede al valor de la clave name en el diccionario.
print(dict['name'])

# 3. AÃ±ade una nueva clave job con el valor "Programador" al diccionario del punto anterior. Imprime el diccionario actualizado.
dict['job']= 'programador'
print (dict)

# 4. Modifica el valor de la clave age en el diccionario para que sea 38. Imprime el diccionario actualizado.
dict['age']=38
print (dict)

# 5. Elimina la clave country del diccionario e imprime el diccionario resultante.
del dict['country']
print(dict)

# 6. Crea un diccionario donde las claves sean nÃºmeros del 1 al 5 y los valores sean sus cuadrados (ejemplo: 1: 1, 2: 4, ...).
dict_2 = {
    1:1,
    2:4,
    3:9,
    4:16,
    5:25
}
print(dict_2)

# 7. Verifica si la clave age estÃ¡ presente en el diccionario {"name": "Brais", "age": 37, "country": "Galicia"}.

dict_brais= {"name": "Brais", "age": 37, "country": "Galicia"}

print('age' in dict_brais.keys())

# 8. Imprime solo las claves del diccionario.
print(dict_brais.keys())

# 9. Convierte las claves del diccionario en una lista e imprime la lista resultante.
print(list(dict_brais))

# 10. Crea un nuevo diccionario a partir de una lista de claves ["name", "age", "job"] usando fromkeys(), asignando a todas las claves el valor "Desconocido".

lista=["name", "age", "job"]

dict_final={}
dict_final=dict_final.fromkeys(lista,'Desconocido')
print (dict_final)