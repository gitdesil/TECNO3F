import os
import subprocess

# Definición de colores ANSI
COLOR_X = "\033[96m"       # Cian / Celeste
COLOR_O = "\033[92m"       # Verde
COLOR_GUIA = "\033[90m"    # Gris oscuro para los números guía
COLOR_BORDES = "\033[93m"  # Amarillo para los títulos y marcos
RESET = "\033[0m"          # Restablecer color por defecto

def limpiar_pantalla():
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)

def obtener_ficha_coloreada(ficha):
    """Devuelve la ficha con su color correspondiente para el tablero."""
    if ficha == "X":
        return f"{COLOR_X}X{RESET}"
    elif ficha == "O":
        return f"{COLOR_O}O{RESET}"
    else:
        # Si es un número guía, lo pintamos de gris
        return f"{COLOR_GUIA}{ficha}{RESET}"

def mostrar_tablero(tablero):
    # Formateamos cada posición del tablero con su respectivo color
    t = [obtener_ficha_coloreada(casilla) for casilla in tablero]
    
    print("\n")
    print(f"     {t[0]} | {t[1]} | {t[2]} ")
    print("    ---|---|---")
    print(f"     {t[3]} | {t[4]} | {t[5]} ")
    print("    ---|---|---")
    print(f"     {t[6]} | {t[7]} | {t[8]} ")
    print("\n")

def verificar_ganador(tablero):
    # Lista de las 8 combinaciones posibles con todos sus índices exactos
    if (tablero[0] == tablero[1] == tablero[2]) or \
       (tablero[3] == tablero[4] == tablero[5]) or \
       (tablero[6] == tablero[7] == tablero[8]) or \
       (tablero[0] == tablero[3] == tablero[6]) or \
       (tablero[1] == tablero[4] == tablero[7]) or \
       (tablero[2] == tablero[5] == tablero[8]) or \
       (tablero[0] == tablero[4] == tablero[8]) or \
       (tablero[2] == tablero[4] == tablero[6]):
        return True
    return False

def ejecutar_tateti():
    tablero = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    turno = "X"
    movimientos = 0
    ganador_detectado = False

    while movimientos < 9:
        limpiar_pantalla()
        print(f"{COLOR_BORDES}========================================={RESET}")
        print(f"{COLOR_BORDES}           JUEGO DEL TA-TE-TI            {RESET}")
        print(f"{COLOR_BORDES}========================================={RESET}")
        mostrar_tablero(tablero)
        
        # Coloreamos el indicador de turno actual
        ficha_turno = f"{COLOR_X}X{RESET}" if turno == "X" else f"{COLOR_O}O{RESET}"
        print(f"Turno del Jugador ({ficha_turno})")
        eleccion = input("Escriba el número de casilla (1-9): ")

        if eleccion not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print(f"\n\033[91m¡Movimiento inválido!{RESET} Debe ingresar un número del 1 al 9.")
            input("Presione ENTER para intentar de nuevo...")
            continue

        indice = int(eleccion) - 1

        if tablero[indice] == "X" or tablero[indice] == "O":
            print(f"\n\033[91m¡Casilla ocupada!{RESET} Por favor, elija otra posición.")
            input("Presione ENTER para intentar de nuevo...")
            continue

        # Guardamos la jugada en texto plano para las validaciones lógicas
        tablero[indice] = turno
        movimientos += 1

        if verificar_ganador(tablero):
            ganador_detectado = True
            break

        turno = "O" if turno == "X" else "X"

    # Fin del juego
    limpiar_pantalla()
    print(f"{COLOR_BORDES}========================================={RESET}")
    print(f"{COLOR_BORDES}       ¡EL JUEGO HA TERMINADO!           {RESET}")
    print(f"{COLOR_BORDES}========================================={RESET}")
    mostrar_tablero(tablero)

    if ganador_detectado:
        ficha_ganadora = f"{COLOR_X}X{RESET}" if turno == "X" else f"{COLOR_O}O{RESET}"
        print(f"   🎉 ¡Felicitaciones! Ganó el Jugador ({ficha_ganadora}).")
    else:
        print("   🤝 ¡Empate! Se completaron todos los casilleros.")
        
    print(f"{COLOR_BORDES}========================================={RESET}")
    input("\nPresione ENTER para regresar al menú principal...")
