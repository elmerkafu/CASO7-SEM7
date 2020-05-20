from opciones import *
import os


def menu():
    os.system('clear')
    print("BIENVENIDO AL COLEGIO SAN BOB")
    print("""
        [1]-REGISTRO DOCENTE
        [2]-REGISTRO ALUMNO
        [3]-REGISTRO CLASES ALUMNO
        [4]-REGISTRO DE NOTAS
        [5]-MODIFICAR DATOS
        [6]-MOSTRAR DATOS
        [7]-REPORTE NOTAS SEGUN CURSO
    """)

def submenu1():
    os.system('clear')
    print("BIENVENIDO - MODIFICAR DATOS EN GENERAL")
    print("""
        [1]-MODIFICAR DOCENTE
        [2]-MODIFICAR ALUMNO
        [3]-MODIFICAR CLASES
        [4]-ELIMINAR REGISTRO
    """)

def submenu2():
    os.system('clear')
    print("MOSTRAR REGISTROS")
    print("""
        [1]-MOSTRAR ALUMNOS
        [2]-MOSTRAR DOCENTES
        [3]-MOSTRAR CLASES
    """)

while True:
    menu()
    seleccion = int(input("INGRESE SELECCION :"))

    if seleccion == 1:
        opcion1()
    
    elif seleccion == 2:
        opcion2()

    elif seleccion == 3:
        opcion3()

    elif seleccion == 4:
        opcion4()
    
    elif seleccion == 5:
        submenu1()
        opcion5()

    elif seleccion == 6:
        submenu2()
        opcion6()
    
    elif seleccion == 7:
        opcion7()
    else:
        print('REGRESANDO AL MENU ..')
        input()