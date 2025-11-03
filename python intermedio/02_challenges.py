# fizzbuzz
def fizzbuzz():
    for index in range(101):
        if index % 3 == 0:
            if index % 5 == 0:
                print('fizzbuzz')
            else : print ('fizz')
        elif index % 5 == 0:
            print('buzz')  
        else : print(index)

fizzbuzz()


#anagrama

def is_anagrama(uno : str, dos : str):
    
    list_1 = [i for i in uno.upper().strip()]
    list_2 = [i for i in dos.upper().strip()]
    if list_1 == list_2 : return  print('dos palabras iguales no son anagrama')
    if sorted(list_1) == sorted(list_2): #no es necesario comprobar la longitud de las palabras porque al comparar las listas ordenadas, si tienen diferente longitud nunca seran iguales
        return print(f'la palabra {dos} es un anagrama de la palabra {uno}')
    else : return print('no son anagramas')

is_anagrama('roma','rmao')
