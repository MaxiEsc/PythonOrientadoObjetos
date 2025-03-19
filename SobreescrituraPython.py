'''
La idea de la sobreescritura en la programacion orientada a objetos
es basicamente redefinir el comportamiento original heredado de la clase padre pero almodandola al comportamiento de la clase hija
entonces por asi decirlo tenemos la impronta de a un mismo comportamiento reasignarlo como algo unico de la clase que lo hereda.
'''

class Animal:
    def comer(self):
        print('Como muchas veces el día')

    def dormir(self):
        print('Duermo muchas horas')

class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar')

    # Sobreescritura del metodo dormir
    def dormir(self):
        print('Duermo 15 horas al día')

# Programa principal
print('---> Ejemplo de Herencia con sobreescritura en Python <----')
print('Clase Padre, soy un Animal')
animal1 = Animal()
animal1.comer()
animal1.dormir()

print('\nClase Hija, soy un Perro')
perro1 = Perro()
perro1.comer()
perro1.dormir()  # Se llama el metodo sobreescrito de la clase hija
perro1.hacer_sonido()