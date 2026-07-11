#Crea una tupla con los meses del año(Una tupla es una colección de datos que no 
# se puede modificar, Se escribe entre paréntesis). 
# pide números al usuario, si el numero esta entre 1 y la longitud máxima de la tupla,
# muestra el contenido de esa #posición sino muestra un mensaje de error. 
# El programa termina cuando el usuario introduce un cero.

meses = (
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre"
)

# El ciclo se repetirá hasta que el usuario escriba 0
while True:

    # Le pedimos un número al usuario
    numero = int(input("Ingrese un número del 1 al 12 (0 para salir): "))

    # Escribe 0 termina el programa
    if numero == 0:
        print("Fin del programa")
        break

    # Si el número está entre 1 y 12
    elif numero >= 1 and numero <= 12:

        # Se resta 1 porque las posiciones empiezan en 0
        print("El mes es:", meses[numero-1])

    # Si el número no es válido
    else:
        print("Error. Ingreso de número fuera de rango.")

#Pide números y mételos en una lista, cuando el usuario meta un 0 ya
#dejaremos de insertar. 
# Por último, muestra los números ordenados de menor a mayor.

# Crear una lista vacía para guardar los números
lista = []

# Repetir hasta que el usuario ingrese 0
while True:

    # Pedir un dato al usuario
    dato = input("Ingrese un número (0 para terminar): ")

    # Verificar si el usuario no escribió nada
    if dato == "":
        print("Error: debe ingresar un número.")
        continue

    # Intentar convertir el dato a un número entero
    try:
        numero = int(dato)
    except ValueError:
        print("Error: solo se permiten números enteros.")
        continue

    # Si el usuario ingresa 0, finalizar el ciclo
    if numero == 0:
        break

    # Agregar el número a la lista
    lista.append(numero)


# Ordenar la lista de menor a mayor
lista.sort()

# Mostrar la lista ordenada
print("\nLos números ordenados son:")
print(lista)

#Crea una tupla con números, pide un numero por teclado e indica cuantas veces se repite.

# Crear una tupla con números

# Pedir un número al usuario con validación
while True:
    dato = input("Ingrese un número: ").strip()

    # Verificar si está vacío
    if dato == "":
        print("Error: Debe ingresar un número.")
        continue

    # Verificar que sea un número entero
    if not dato.isdigit():
        print("Error: Debe ingresar solo números.")
        continue

    numero = int(dato)
    break

# Contar cuántas veces aparece en la tupla
cantidad = numeros.count(numero)

# Mostrar el resultado
if cantidad > 0:
    print(f"El número {numero} se repite {cantidad} veces en la tupla.")
else:
    print(f"El número {numero} no se encuentra en la tupla.")
