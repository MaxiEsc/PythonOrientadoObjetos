'''Clase heredada del dispositivo de entrada'''

from DispositivoEntrada import DispositivoEntrada

class Raton(DispositivoEntrada):

    contador_Ratones = 0

    def __init__(self, marca, tipo_entrada ):
        Raton.contador_Ratones += 1
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return f'''Marca :{self.marca} --> Tipo Entrada: {self.tipo_entrada}'''

if __name__ == '__main__':
    raton1 = Raton('HP', 'USB')
    print(raton1)
    raton2 = Raton('Acer', 'Bluetooth')
    print(raton2)