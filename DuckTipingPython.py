'''
La funcion Polimorfica

Funcion que puede recibir un tipo de dato de herencia polimorfica

'''

# Polimorfismo
class Animal:
    def hacer_sonido(self):
        print('Hago un pitido')

class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar')

class Gato(Animal):
    def hacer_sonido(self):
        print('Puedo maullar')

# Funcion polimorfica: Esta misma podra recibir un obejto de tipo animal que es el padre de todas las clases
def hacer_sonido_animal(animal):  # duck typing: El tipo de objeto de determina segun su comportamiento
    animal.hacer_sonido()

print('----> Ejemplo Polimorfismo <----')
print('Clase Padre Animal: ')
animal1 = Animal()
hacer_sonido_animal(animal1)
# Definimos un objeto de la clase Perro
print('\nClase Hija Perro: ')
perro1 = Perro()
hacer_sonido_animal(perro1)
# Definimos un objeto de la clase Gato
print('\nClase Hija Gato: ')
gato1 = Gato()
hacer_sonido_animal(gato1)