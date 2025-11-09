import re
# 1. Busca si una cadena empieza por "Hola".

string = 'Hola bona tarda mi nombre es aldany'
string2 = 'pixon te llamas daniel'

print(re.match('Hola',string))

print(re.match('Hola',string2))

# 2. Busca la palabra "Python" en una cadena aunque estÃ© en minÃºsculas.
palabra= 'Estamos picando codigo en este curso con Python, el lenguaje de fastapi entre otros frameworks (de python claro)'

print(re.search('python',palabra,re.I))#con el re.I (simplificacion de ignorecase) lo que hacemos es decirle que busque el patron tanto en mayusculas como en minisculas como ambos combinadas, vaya que omita el caso de distincion por mayus o minus

# 3. Encuentra todas las apariciones de la palabra "curso" en una cadena.
cole = 'pues estoy en primero de daw, pero aun asi en este curso tengo asignaturas que en teoria son de segundo curso. Fue un lio la matricula al ser la primera vez que CUrSo este grado de forma online'

print(re.findall('curso',cole,re.I))

# 4. Reemplaza todas las apariciones de "lecciÃ³n" por "LECCIÃ“N".

ejemplo = 'para esta leccion vamos a hacer uso del metodo sub, vamos a ver si la leccion no es muy pesada'

print(re.sub('leccion', 'LECCION',ejemplo))

# 5. Divide un texto en partes separadas por comas.

print(re.split('leccion',ejemplo))

# 6. Busca la primera palabra que comience con "A" o "a".
patron = r'\b[aA]\w*'
print(re.search(patron,ejemplo))

# 7. Encuentra todas las palabras en una cadena que terminen en "ciÃ³n".

frase_larga = 'pues parece que hablamos de colores como el cian, aunque yo soy mas del naranja hay gente que tiene toda su casa de color cian, en fin, para gustos colores, ah espera que aparecian nuevos retos como los perdian jaja'

el_patron = r'\w*cian\b'

print(re.findall(el_patron,frase_larga))

# 8. Verifica si una cadena contiene solo nÃºmeros.

numero = '12342345234532442343214'
patron_numerico = r'^\d+$'

print( re.fullmatch(patron_numerico,numero))

# 9. Reemplaza todos los nÃºmeros de una cadena por el texto "[nÃºmero]".
frase_con_numeros = 'vale si tengo 2 manzanas y me como 3 que soy ? un puto mago cohone'
patron_nuevo = r'\d+'
reemplazo = '[numero]'
print(re.sub(patron_nuevo,reemplazo,frase_con_numeros))

# 10. Encuentra todas las palabras de 4 letras exactas en una cadena.
patron_finalll=r'\b[a-zA-Z]{4}\b'
print(re.findall(patron_finalll,frase_con_numeros))