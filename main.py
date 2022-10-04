from register import *
import os.path

def carga_vector():
    register = []
    if not os.path.exists('reservas.csv'):
        print('Archivo no encontrado')
    else:
        m = open('reservas.csv', 'rt')
        t = os.path.getsize('reservas.csv')
        while m.tell() < t:
            linea = m.readline()
            linea = linea.split(',')
            # print(linea)
            if linea[0] != '\n':
                aux = Reserva(str(linea[0]), str(linea[1]), int(linea[2]), int(linea[3]), int(linea[4]), float(linea[5]))
                register.append(aux)
        else:
            m.close()
    return register

def mostrar_datos(vec):
    for i in range(len(vec)):
        to_string(vec[i], True)

def validate(vec, id):
    for ob in vec:
        while ob.id == id:
            id = input('Por favor introduzca otro codigo diferente: ')
        else:
            return True, id


def validate_tipo(n):
    while n < 0 or n > 3:
        n = int(input('Por favor cargue un tipo de cumpleaños valido: '))
    return n


def data():
    nombre = str(input('Por favor ingrese el nombre del cumpleañero: '))
    edad = int(input('Por favor ingrese la edad del cumpleañero: '))
    tipo = int(input('Por favor ingrese el tipo de cumpleaños: '))
    tipo = validate_tipo(tipo)
    cant_in = int(input('Por favor ingrese la cantidad de invitados: '))
    monto = float(input('Por favor ingrese el monto final del cumpleaños: '))

    return nombre, edad, tipo, cant_in, monto

def agregar(vec):
    if not os.path.exists('reservas.csv'):
        print('Archivo no encontrado')
    else:
        m = open('reservas.csv', 'at', encoding='utf8')
        id = input('Por favor introduzca un codigo de reserva: ')
        t = validate(vec, id)
        if t[0]:
            aux = data()
            m.write(t[1])
            m.write(',')
            for i in range(6):
                m.write(str(aux[i]))
                if i != 6:
                    m.write(',')
        m.close()


def monto(vec):
    aux = ['salón', 'salón y animación', 'salón, animación y comida niños', 'salón, animación, comida niños y sorpresitas']
    s = [0] * 4
    for item in vec:
        s[item.tipo] += item.monto
    for i in range(len(aux)):
        print(f'{aux[i]}- {s[i]}')
    t = s[0]
    for i in range(len(s)):
        if t < s[i]:
            t = i
    print(f'El tipo de cumpleaños con mas recaudacion es: {aux[t]}')


def nuevo_vector(vec):
    e = int(input('Por favor ingrese una edad minima: '))
    a = int(input('Por favor ingrese una cantidad de asistentes minima: '))
    aux = []
    for item in vec:
        if e > item.edad and a > item.cant_invitados:
            aux.append(item)
    for i in range(len(aux)):
        to_string(aux[i])

    return aux


def sobrescribir(vec):
    if not os.path.exists('reservas.csv'):
        print('Archivo no encontrado')
    else:
        m = open('reservas.csv', 'wt', encoding='utf8')
        for v in vec:
            m.write(f'{v.id}, {v.nombre}, {v.edad}, {v.tipo}, {v.cant_invitados}, {v.monto}\n')
        m.close()

def main():
    op = int(input('Por favor elija una opcion: \n1) Mostrar datos\n2) Agregar reserva\n3) Mayor monto\n4) Nuevo vector\n5) Salir del programa\n'))
    flag = True
    new_vec = []
    while flag:
        vec = carga_vector()
        if op == 1:
            mostrar_datos(vec)
            op = int(input('Por favor elija una opcion: \n1) Mostrar datos\n2) Agregar reserva\n3) Mayor monto\n4) Nuevo vector\n5) Salir del programa\n'))
        elif op == 2:
            agregar(vec)
            op = int(input('Por favor elija una opcion: \n1) Mostrar datos\n2) Agregar reserva\n3) Mayor monto\n4) Nuevo vector\n5) Salir del programa\n'))
        elif op == 3:
            monto(vec)
            op = int(input('Por favor elija una opcion: \n1) Mostrar datos\n2) Agregar reserva\n3) Mayor monto\n4) Nuevo vector\n5) Salir del programa\n'))
        elif op == 4:
            new_vec = nuevo_vector(vec)
            op = int(input('Por favor elija una opcion: \n1) Mostrar datos\n2) Agregar reserva\n3) Mayor monto\n4) Nuevo vector\n5) Salir del programa\n'))
        elif op == 5:
            sobrescribir(new_vec)
            print('Adios!!')
            flag = False


if __name__ == '__main__':
    main()
