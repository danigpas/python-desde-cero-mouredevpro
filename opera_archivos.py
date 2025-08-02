def escribir_archivo(name,contenido):
    with open(name,'w') as archivo:
        archivo.write(contenido)

def leer_archivo(name):
    with open(name,'r') as archivo:
        print(archivo.read())

