# 1. Crea una clase llamada "Animal" que tenga una propiedad "species" y 
# un mÃ©todo "make_sound" que imprima un sonido genÃ©rico.

class Animal:
    def __init__(self, species):
        self.species = species
    
    def make_sound(self):
        print('siuuuuu')

gallo=Animal('gallo') 
gallo.make_sound()

# 2. Modifica la clase "Animal" para que reciba la especie al crear un objeto y
#  almacÃ©nala en una propiedad pÃºblica. AÃ±ade el mÃ©todo "make_sound" que imprima
#  un sonido dependiendo de la especie.


class Animal2:
    def __init__(self, species):
        self.species = species
    
    def make_sound(self):
        if self.species == 'gallo':
            print('korokorokooooo')
        else:    
            print('siuuuuu')

# 3. Crea una clase llamada "Car" con las propiedades pÃºblicas "brand" y "model".
#  AdemÃ¡s, debe tener una propiedad privada "_speed" que inicialmente serÃ¡ 0.

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#         self.__speed = 0
    
    
# 4. AÃ±ade a la clase "Car" un mÃ©todo llamado "accelerate" que aumente la velocidad
#  en 10 unidades. AÃ±ade tambiÃ©n un mÃ©todo "brake" que reduzca la velocidad en 10
#  unidades. AsegÃºrate de que la velocidad no sea negativa.


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.__speed = 0
    
    def accelerate(self):
        self.__speed += 10
        return self.__speed
    def brake(self):

        self.__speed -= 10
        velocidad = self.__speed
        if velocidad < 0 :
            return 0
        else :
            return velocidad


coche = Car('ford ','focus' )

coche.accelerate()

coche.accelerate()

coche.accelerate()
coche.brake()
coche.brake()
coche.brake()
coche.brake()
coche.brake()
coche.brake()
print(coche.brake())

# 5. Crea una clase "Book" que tenga propiedades como "title" (pÃºblico) y "author"
#  (privado). AÃ±ade un mÃ©todo para obtener el autor y otro para cambiar el tÃ­tulo
#  del libro.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.__author = author
    
    def get_author(self):
        return self.__author
    
    def set_title(self, new_title):
        self.title= new_title
        return new_title
    
nautilus = Book('nautilis','yo')
print(nautilus.get_author())
print(nautilus.set_title('el libro troll'))

# 6. Crea una clase "Estudiante" que tenga como propiedades su nombre, apellido y
#  una lista de notas. AÃ±ade un mÃ©todo para calcular y devolver la nota media del
#  estudiante.

class Estudiante:
    def __init__(self, nombre, apellido, notas):
        self.nombre = nombre
        self.apellido = apellido
        self.notas= list(notas)

    def nota_media(self):
        total=0
        examenes=0
        for nota in self.notas :
            examenes = nota + examenes
            total += 1
        return examenes / total
        
pepe = Estudiante('pepe','perez',[3,5,6,7,8,9,9,9,2,2,5])

print(pepe.nota_media())
print("Notas:", pepe.notas)
print("Media:", pepe.nota_media())

# 7. Crea una clase "BankAccount" con propiedades como "owner" y "balance". AÃ±ade mÃ©todos
#  para depositar y retirar dinero, asegurÃ¡ndote de que no se pueda retirar mÃ¡s de lo
#  que hay en la cuenta.

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def ingresar(self,cantidad):
        self.balance += cantidad
        print(f'se han ingresado {cantidad} de euros')
    
    def retirar(self, cantidad):
        if self.balance < cantidad :
            print( f'no se puede retirar mas dinero de {self.balance} que es el saldo disponible')
        else :
            self.balance -= cantidad
            print(f'se han retirado {cantidad} de euros')
santander = BankAccount('yo', 500)

santander.retirar(500)
print(santander.balance)
santander.ingresar(200)
print(santander.balance)
santander.retirar(300)
print(santander.balance)

# 8. Crea una clase "Point" que represente un punto en el espacio 2D con coordenadas "x"
#  e "y". AÃ±ade un mÃ©todo que calcule la distancia entre dos puntos.

class Point:
    def __init__(self, x , y):
        self.x = x
        self.y = y
    
    def distancia (self, punto2):
        distance_x = abs(self.x - punto2.x)
        distance_y = abs(self.y - punto2.y)
        return (distance_x **2 + distance_y**2)**0.5
punto1 = Point(3,3)
punto2 = Point (4,4)

print(punto1.distancia(punto2))

# 9. Crea una clase "Employee" que tenga propiedades como "name", "hourly_wage" 
# (pago por hora) y "hours_worked". AÃ±ade un mÃ©todo que calcule el pago total basado
#  en las horas trabajadas y el salario por hora.

class Employee :
    def __init__(self, name, hourly_wage, hours_worked):
        self.name = name
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked

    def salario_mensual(self):
        return self.hourly_wage * self.hours_worked
    
carlos = Employee('carlos',8,40)
print(carlos.salario_mensual())

# 10. Crea una clase "Store" que tenga una propiedad "inventory" (una lista de productos).
#  AÃ±ade un mÃ©todo para agregar un producto al inventario y otro para mostrar todos los
#  productos disponibles.

class Store:
    def __init__(self, inventory):
        self.inventory = list(inventory)

    def add_product(self,product):
        self.inventory.append(product)

    def get_inventory(self):
        return self.inventory
    
tiendica = Store(['bola','bate']
)
tiendica.add_product('cepillo')
print(tiendica.get_inventory())