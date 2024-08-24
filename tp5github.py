"""Llevar un registro de todos los datos de alumnos de la escuela (Nombre,
Apellido, fecha de nacimiento, DNI, Nombre de Tutor, registro de todas las
notas, cantidad de faltas, cantidad de amonestaciones recibidas."""



benjaminavila = {"Nombre": "Benjamín",
                 "Apellido": "Ávila",
                 "DNI": 47608367,
                 "Fecha de nacimiento": "7 de noviembre de 2006",
                 "Tutor": "Gabriela Ossola",
                 "Notas": [10,9,8],
                 "Faltas": 1,
                 "Amonestaciones": 0}

facundoferro = {"Nombre": "Facundo",
                 "Apellido": "Ferro Podestá",
                 "DNI": 47420069,
                 "Fecha de nacimiento": "20 de abril de 2007",
                 "Tutor": "Josefina Gangi",
                 "Notas": [1,5,10],
                 "Faltas": 15,
                 "Amonestaciones": 15}

chichina = {"Nombre": "Sol",
                 "Apellido": "Rodriguez",
                 "DNI": 47810421,
                 "Fecha de nacimiento": "11 de septiembre de 2005",
                 "Tutor": "Roberto Rodriguez",
                 "Notas": [6,6,6],
                 "Faltas": 5,
                 "Amonestaciones": 2}

norma = {"Nombre": "Norma Elizabeth",
                 "Apellido": "Vázquez",
                 "DNI": 18902421,
                 "Fecha de nacimiento": "31 de octubre de 1960",
                 "Tutor": "María Fernández",
                 "Notas": [8,8,9],
                 "Faltas": 0,
                 "Amonestaciones": 5}

Alumnos = [benjaminavila, facundoferro, chichina, norma]

def agregaralumnos(datos):
    global alumnonuevo
    if comando >= 5:
        nombre = input("Ingrese el nombre del alumno a agregar: ")
        apellido = input("Ingrese el apellido del alumno a agregar: ")
        dni = int(input("Ingrese el DNI del alumno a agregar: "))
        fechanac = input("Ingrese la fecha de nacimiento del alumno a agregar de manera coloquial: ")
        tutor = input("Ingrese el tutor del alumno a agregar: ")
        notas = []
        for i in range(3):
            trimestres = int(input("Ingrese las notas de los trimestres del alumno: "))
            notas.append(trimestres)
        faltas = int(input("Ingrese la cantidad de faltas del alumno a agregar: "))
        amonestaciones = int(input("Ingrese la cantidad de amonestaciones del alumno a agregar: "))
        alumnonuevo = {"Nombre": nombre,
                       "Apellido":apellido,
                       "DNI": dni,
                       "Fecha de nacimiento": fechanac,
                       "Tutor": tutor,
                       "Notas": notas,
                       "Faltas": faltas,
                       "Amonestaciones": amonestaciones}
        Alumnos.append(alumnonuevo)


def modificar(Alumnos):
    alumno_a_mod = input("Ingrese el nombre del alumno a modificar: ")
    for alumno in Alumnos:
        if alumno["Nombre"] == alumno_a_mod:
            apartado = input("¿Qué apartado quiere modificar? ")
            if apartado in alumno:
                modificacion = input("Ingrese el nuevo valor: ")
                if apartado == "Notas":
                    nuevas_notas = list(map(int, modificacion.split(',')))
                    alumno[apartado] = nuevas_notas
                else:
                    alumno[apartado] = modificacion
                print(f"El apartado '{apartado}' ha sido actualizado con éxito.")
                return
            else:
                print("Ese apartado no existe.")
                return

    print("El alumno no está en la lista.")


def eliminar(Alumnos):
    alumno_elim = input("Ingrese el nombre del alumno a eliminar: ")
    for alumno in Alumnos:
        if alumno["Nombre"] == alumno_elim:
            Alumnos.remove(alumno)
            print(f"El alumno '{alumno_elim}' ha sido eliminado con éxito.")
            return
    print("El alumno no está en la lista.")



while True: 
    comando = int(input("¿Qué alumno quiere ver? Seleccione un número del 1 al 4.\nSi quiere agregar un alumno pulse 5, si quiere modificar\nalgún dato pulse 6, si quiere expulsar alumnos pulse 7: "))

    if comando < 5:
        apartado = input("¿Qué apartado del alumno quiere ver?: ")
        print(Alumnos[comando-1][apartado])
    elif comando == 5:
        agregaralumnos(Alumnos)
        apartado = input("¿Qué apartado del alumno quiere ver?: ")
        print(Alumnos[-1][apartado])

    elif comando == 6:
        modificar(Alumnos)

    elif comando == 7:
        eliminar(Alumnos)