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
            aux = Reserva(linea[0], linea[1], linea[2], str(linea[3]), linea[4], linea[5])
            register.append(aux)
        else:
            m.close()
    return register

def mostrar_datos(vec):
    for i in range(len(vec)):
        to_string(vec[i], True)


def agregar():
    pass


def monto():
    pass


def nuevo_vector():
    pass


def sobrescribir():
    pass

def main():
    op = int(input('Por favor elija una opcion: \n1) Mostrar datos\n2) Agregar reserva\n3) Mayor monto\n4) Nuevo vector\n5) Salir del programa\n'))
    flag = True
    while flag:
        if op == 1:
            mostrar_datos(carga_vector())
            op = int(input('Por favor elija una opcion: \n1) Mostrar datos\n2) Agregar reserva\n3) Mayor monto\n4) Nuevo vector\n5) Salir del programa\n'))
        elif op == 2:
            agregar()
            op = int(input('Por favor elija una opcion: \n1) Mostrar datos\n2) Agregar reserva\n3) Mayor monto\n4) Nuevo vector\n5) Salir del programa\n'))
        elif op == 3:
            monto()
            op = int(input('Por favor elija una opcion: \n1) Mostrar datos\n2) Agregar reserva\n3) Mayor monto\n4) Nuevo vector\n5) Salir del programa\n'))
        elif op == 4:
            nuevo_vector()
            op = int(input('Por favor elija una opcion: \n1) Mostrar datos\n2) Agregar reserva\n3) Mayor monto\n4) Nuevo vector\n5) Salir del programa\n'))
        elif op == 5:
            sobrescribir()
            print('Adios!!')
            flag = False


if __name__ == '__main__':
    main()
