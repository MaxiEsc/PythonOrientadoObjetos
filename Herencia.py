'''
En este tema vamos a ver la idea de Herencia
Donde como en lenguajes como c++ por ejemplo es posible compartir esta idea.
Donde se tendra la clase padre y las clases hijas que son subclases que decenderan de la clase padre, como alguna caracteristica.
'''

class Animal:
    def comer(self):
        print('Duerme')
    def dormir(self):
        print('Come')

class Perro(Animal):
    def hacer_Sonido(self):
        print('Ladro')

# Programa principal
print('----> Ejemplo de Herencia en Python <----')
print('Clase Padre, soy un Animal')
animal1 = Animal()
animal1.comer()
animal1.dormir()

print('\nClase Hija, soy un Perro')
perro1 = Perro()
perro1.comer()
perro1.dormir()
perro1.hacer_Sonido()