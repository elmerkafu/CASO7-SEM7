from conexiones import Conexion
import os


datosConexion = {
    'url' : 'mongodb://127.0.0.1:27017',
    'database' : 'colegio'   
}

def opcion1():

    os.system('clear')
    print("REGISTRO DE DOCENTES")
    cod_docente = str(input("INGRESE COD_DOCENTE : "))
    nombre = str(input("INGRESE NOMBRES : "))
    apellido = str(input("INGRESE APELLIDOS : "))
    materia = str(input('INGRESE MATERIA A DICTAR'))
    data = {
        'cod_docente' : cod_docente,
        'nombre' : nombre,
        'apellido' : apellido,
        'materia' : materia
    }
    Conexion(**datosConexion).insertarRegistro(
        'profesores',
        data)

def opcion2():

    os.system('clear')
    print("REGISTRO DE ALUMNOS")
    cod_alumno = str(input("INGRESE COD_ALUMNO : "))
    nombre = str(input("INGRESE NOMBRES : "))
    apellido = str(input("INGRESE APELLIDOS : "))
    grado = int(input("INGRESE GRADO : "))
    data = {
        'cod_alumno' : cod_alumno,
        'nombre' : nombre,
        'apellido' : apellido,
        'grado' : grado
    }
    Conexion(**datosConexion).insertarRegistro(
        'alumnos',
        data)

def opcion3():
    os.system('clear')
    print("REGISTRO DE CLASES-ALUMNOS")
    cod_alumno = str(input("INGRESE COD_ALUMNO : "))
    cod_docente = str(input("INGRESE COD_DOCENTE : "))
    salon = str(input("INGRESE NUMERO DE SALON : "))
    materia = str(input("INGRESE MATERIA : "))

    data = {
        'cod_alumno' : cod_alumno,
        'cod_docente' : cod_docente,
        'salon' : salon,
        'materia' : materia
    }
    Conexion(**datosConexion).insertarRegistro(
        'salones',
        data)

def opcion4():
    os.system('clear')
    print("REGISTRO DE NOTAS")    
    cod_alumno = str(input("INGRESE COD_ALUMNO : "))
    curso = str(input("INGRESE CURSO : "))
    tipo = input("INGRESE TIPO DE EVALUACION : ")
    nota = input('INGRESE LA CALIFICACION : ')
    data = {
        'cod_alumno' : cod_alumno,
        'curso' : curso,
        'tipo' : tipo,
        'nota' : nota
    }
    Conexion(**datosConexion).insertarRegistro(
        'notasAlumnos',
        data)

def opcion5():
    numero = int(input("""
        INGRESE LA SELECCION
    """))  
    if numero == 1:

        os.system('clear')
        print("MODIFICAR  DOCENTES")
        cod_docente = str(input("INGRESE COD_DOCENTE : "))
        print("INGRESE DATOS A MODIFICAR")
        nombre = str(input("INGRESE NOMBRES : "))
        apellido = str(input("INGRESE APELLIDOS : "))
        materia = str(input('INGRESE MATERIA A DICTAR : '))
        condicion = {
            'cod_docente' : cod_docente
        }
        change = {
            'nombre' : nombre,
            'apellido' : apellido,
            'materia' : materia
        }   
        Conexion(**datosConexion).actualizarRegistros(
            'profesores',
            condicion,
            change
        )

    elif numero == 2:

        os.system('clear')
        print("MODIFICAR ALUMNOS")
        cod_alumno = str(input("INGRESE COD_ALUMNO : "))
        print("INGRESE DATOS A MODIFICAR")
        nombre = str(input("INGRESE NOMBRES : "))
        apellido = str(input("INGRESE APELLIDOS : "))
        grado = int(input("INGRESE GRADO : "))
        condicion = {
            'cod_alumno' : cod_alumno
        }
        change = {
            'nombre' : nombre,
            'apellido' : apellido,
            'grado' : grado
        }   
        Conexion(**datosConexion).actualizarRegistros(
            'alumnos',
            condicion,
            change
        )  

    elif numero == 3:

        os.system('clear')
        print("MODIFICAR CLASES-ALUMNOS")
        salon = str(input("INGRESE NUMERO DE SALON : "))
        print("INGRESE DATOS A MODIFICAR")
        cod_alumno = str(input("INGRESE COD_ALUMNO : "))
        cod_docente = str(input("INGRESE COD_DOCENTE : "))
        materia = str(input("INGRESE MATERIA : "))
        condicion = {
            'salon' : salon
        }
        change = {
            'cod_alumno' : cod_alumno,
            'cod_docente' : cod_docente,
            'materia' : materia
        }
        Conexion(**datosConexion).actualizarRegistros(
            'salones',
            condicion,
            change
        )
    else:

        os.system("clear")
        print("ELIMINAR REGISTROS")
        print("""
            [1]-DOCENTES
            [2]-ALUMNOS
        """)
        seleccion = input("INGRESE LA SELECCION : ")

        if seleccion == 1:
            os.system('clear')
            cod_alumno = str(input("INGRESE COD_ALUMNO : "))
            condicion = {
                'cod_alumno' : cod_alumno
            }
            Conexion(**datosConexion).eliminarRegistros(
                'alumnos',
                condicion
            )
        else:
            os.system('clear')
            cod_docente = str(input("INGRESE COD_DOCENTE : "))
            condicion = {
                'cod_docente' : cod_docente
            }
            Conexion(**datosConexion).eliminarRegistros(
                'profesores',
                condicion
            )            

def opcion6():
    numero = int(input("""
        INGRESE LA SELECCION A MOSTRAR
    """))

    if numero == 1:
        cod_alumno = str(input("INGRESE COD_ALUMNO A BUSCAR : "))
        data = {
            'cod_alumno': cod_alumno
        }
        datos = Conexion(**datosConexion).mostrarRegistros(
            'alumnos',
            data
        )

    elif numero == 2:
        cod_docente = str(input("INGRESE COD_DOCENTE A BUSCAR : "))
        data = {
            'cod_docente': cod_docente
        }
        datos = Conexion(**datosConexion).mostrarRegistros(
            'profesores',
            data
        )

    else:
        salon = str(input("INGRESE SALON A BUSCAR : "))
        data = {
            'salon': salon
        }
        datos = Conexion(**datosConexion).mostrarRegistros(
            'salon',
            data
        )

    input("PRESIONE ENTER PARA CONTINUAR")

def opcion7():

    os.system('clear')
    print("REPORTE DE NOTAS SEGUN CURSO")
    curso = str(input("INGRESE CURSO : "))
    condicion = { 'curso' : curso }
    Conexion(**datosConexion).mostrarRegistrosPromedios(
        'notasAlumnos',
        condicion
    )
    input("ENTER PARA CONTINUAR")
