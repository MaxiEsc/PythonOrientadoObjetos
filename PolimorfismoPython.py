'''
Repasando que el polimorfismo es el comportamiento en multiples clases hereditarias
Por lo que debemos cumplir con las siguientes condiciones:

-Herencia entre la clases seleccionadas
-Sobreescritura entre las clases

Basicamente estariamos usando un ejemplo de interface (Como en java) para llevar a cabo este comportamiento.
Osea suponga una clase animal como en los pasados ejemplos y cada tipo de animal posee la interfaz de hacer su ruido caracterristico por lo que
entonce los perros en ruido caracteristico devolveran sonidos caninos, los gatos sonidos gatunos, etc.

Lo interesante es que el metodo que se mandara a llamar en el momento que se cree el objeto es la clase con mejor jerarquia
por lo que en este caso no tomara el sonido de la clase padre pero si con el tipo del que se haya quedado ese objeto

'''

# Polimorfismo
class Animal:
    def hacer_sonido(self):
        print('Hago un pitido')

class Perro(Animal):
    # pass
    def hacer_sonido(self):
        print('Puedo ladrar')

class Gato(Animal):
    def hacer_sonido(self):
        print('Puedo maullar')

print('----> Ejemplo Polimorfismo <----')
print('Clase Padre Animal: ')
animal1 = Animal()
animal1.hacer_sonido()
# Definimos un objeto de la clase Perro
print('\nClase Hija Perro: ')
perro1 = Perro()
perro1.hacer_sonido()  # Polimorfismo
# Definimos un objeto de la clase Gato
print('\nClase Hija Gato: ')
gato1 = Gato()
gato1.hacer_sonido()