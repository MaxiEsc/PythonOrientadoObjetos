'''
Como En java, Python posee la clase Object como padre de todas las clases,

las mas importantes metodos las clases Object
podemos usar estos metodos
__init__()
__str__()
__eq__()
Que si bien ya hemos estado usando sin ser conciente de ello
Con la palabra Super Podemos acceder al comportamiento de la clase padre de las clases
'''

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    # Sobreescribir el metodo __str__
    def __str__(self):
        return f'''Persona:
        nombre = {self.nombre}
        apellido = {self.apellido}
        Dir. mem. {super.__str__(self)}'''

# Codigo principal
persona1 = Persona('Ana', 'Martinez')
print(persona1) # El metodo __str__ se llama automaticamente desde print
#print(persona1.__str__()) esto es opcional