from tickets import ejecutar_tickets
from tateti import ejecutar_tateti
import os
import subprocess


def limpiar_pantalla():
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)


while True:
    limpiar_pantalla()

    print("===================================")
    print("      TRABAJO INTEGRADOR PYTHON")
    print("===================================")
    print("1 - Sistema de Tickets")
    print("2 - Ta-Te-Ti")
    print("3 - Salir")
    print("===================================")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        ejecutar_tickets()

    elif opcion == "2":
        ejecutar_tateti()

    elif opcion == "3":
        salir = input("¿Está seguro que desea salir? (S/N): ")

        if salir.upper() == "S":
            print("Hasta la proxima !")
            break

    else:
        print("\nOpción inválida.")
        input("Presione ENTER para continuar...")