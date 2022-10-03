class Reserva:
    def __init__(self, id, nombre, edad, tipo, cant_invitados, monto):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo
        self.cant_invitados = cant_invitados
        self.monto = monto


def to_string(self, n=False):
    re = ['salón', 'salón y animación', 'salón, animación y comida niños', 'salón, animación, comida niños y sorpresitas']
    if n:
        print(f'Numero de reserva: {self.id}| Nombre del cumpleañero: {self.nombre}| Edad: {self.edad}| Tipo de servicio: {re[self.tipo]} |'
          f' Cantidad de invitados: {self.cant_invitados}| Monto: {self.monto}')
    else:
        print(f'Numero de reserva: {self.id}| Nombre del cumpleañero: {self.nombre}| Edad: {self.edad}| Tipo de servicio: XXX |'
          f' Cantidad de invitados: {self.cant_invitados}| Monto: {self.monto}')
