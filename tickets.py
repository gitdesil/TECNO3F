import random
import os
import sys
import subprocess


def limpiar_pantalla():
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)


def menu():
    print("==============================")
    print("     SISTEMA DE TICKETS")
    print("==============================")
    print("1 - Alta Ticket")
    print("2 - Leer Ticket")
    print("3 - Salir")

    opcion = input("Seleccione una opción: ")
    return opcion

def alta_ticket():

    while True:

        nombre = input("Nombre: ")
        sector = input("Sector: ")
        asunto = input("Asunto: ")
        problema = input("Problema: ")

        # Generar un número de ticket que no exista
        while True:

            numero = random.randrange(1000, 10000)

            ruta = "tickets/" + str(numero) + ".txt"

            if not os.path.isfile(ruta):
                break

        archivo = open(ruta, "w")

        archivo.write("Numero de Ticket: " + str(numero) + "\n")
        archivo.write("Nombre: " + nombre + "\n")
        archivo.write("Sector: " + sector + "\n")
        archivo.write("Asunto: " + asunto + "\n")
        archivo.write("Problema: " + problema + "\n")

        archivo.close()

        print()
        print("========================")
        print("TICKET CREADO")
        print("========================")
        print("Número:", numero)
        print("Nombre:", nombre)
        print("Sector:", sector)
        print("Asunto:", asunto)
        print("Problema:", problema)
        print()
        print("Recuerde guardar el número del ticket.")
        print()

        respuesta = input("¿Desea crear otro ticket? (S/N): ")

        if respuesta.upper() != "S":
            break

def leer_ticket():

    while True:

        numero = input("Ingrese el número del ticket: ")

        ruta = "tickets/" + numero + ".txt"

        if os.path.isfile(ruta):

            archivo = open(ruta, "r")

            print("\n========================")
            print("    TICKET ENCONTRADO")
            print("========================\n")

            print(archivo.read())

            archivo.close()

        else:

            print("\nNo existe un ticket con ese número.")

        print()

        respuesta = input("¿Desea leer otro ticket? (S/N): ")

        if respuesta.upper() != "S":
            break
        
# Programa principal 
def ejecutar_tickets():
    # Aseguramos que la carpeta exista antes de operar
    if not os.path.exists("tickets"):
        os.makedirs("tickets")
    while True:
        limpiar_pantalla()
        opcion = menu()
        if opcion == "1":
            limpiar_pantalla()
            alta_ticket()
            input("\nPresione ENTER para continuar...")
        elif opcion == "2":
            limpiar_pantalla()
            leer_ticket()
            input("\nPresione ENTER para continuar...")
        elif opcion == "3":
            respuesta = input("\n¿Está seguro que desea volver al menú principal? (S/N): ")
            if respuesta.upper() == "S":
                return # <-- regresa a main.py en lugar de cerrar la terminal
        else:
            print("\nOpción incorrecta.")
            input("\nPresione ENTER para continuar...")