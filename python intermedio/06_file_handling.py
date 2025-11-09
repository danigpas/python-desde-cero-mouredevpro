# 1. Crea un archivo de texto y escribe en Ã©l la frase "Hola desde Python".
ruta = './file.txt'
fichero = open(ruta,'w')
fichero.write('Hola desde Python')
fichero.close()

# 2. Abre un archivo y lee todo su contenido.
fichero = open(ruta,'r+')
print(fichero.readlines())
#fichero.close()

# 3. AÃ±ade una nueva lÃ­nea al final del archivo con el texto "LÃ­nea aÃ±adida".
#fichero = open(ruta,'w+')
fichero.write('\nLinea added')
# 4. Lee solo los primeros 10 caracteres del archivo.
fichero.seek(0) #movemos el puntero al inicio del fichero
print(fichero.read(10))
# 5. Usa seek para volver al inicio del archivo y leer desde ahÃ­.
#echo en el paso anterior
# 6. Lee e imprime el contenido lÃ­nea por lÃ­nea usando readline.
fichero.close()
fichero = open(ruta,'r')
print(fichero.readline())
print(fichero.readline())
# 7. Lee todas las lÃ­neas del archivo en una lista y recÃ³rrelas con un bucle.
fichero.close()
fichero=open(ruta,'a+')
fichero.writelines(['\nmi nombre es dani','\ny estoy reforzando mis conceptos de programacion'])
fichero.seek(0)
for linea in fichero.readlines():
    print(linea)
# 8. Crea un archivo nuevo que sobrescriba si ya existe, y escribe varias lÃ­neas.
fichero.close()
fichero = open(ruta,'w+')
fichero.writelines(['\nmi nombre es dani','\ny estoy reforzando mis conceptos de programacion','\n nuevas lienaaaaaass'])
# 9. Usa una funciÃ³n para abrir un archivo, escribir texto y cerrarlo automÃ¡ticamente con with.
fichero.close()

def escribe_y_cierra(texto,ruta):
    with open(ruta,'w') as fichero:
        fichero.writelines(texto)

escribe_y_cierra(['holaaa buenas tardes','\ncomo andamos en este preciosos dia','\nbien gracias, guay con Python'],ruta)

# 10. Lee un archivo lÃ­nea por lÃ­nea y muestra solo las que contienen la palabra "Python".
with open(ruta,'r') as archivo :
    for linea in archivo:
        if 'Python' in linea : print(linea)
