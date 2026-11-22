"""
"""

import numpy as np
import random as rand

JUGADORES = ("O", "X")

# ---------------------------------------------------------------

def movercursor_inicio() -> None:
    
    print("\033[H", end="")

# ---------------------------------------------------------------

def mostrar_tablero(tab) -> None:
    """
    Funcion que imprime el tablero en pantalla.
    
    Funcion que imprime un "tablero" en pantalla, donde el tablero es un arreglo bidimensional con forma 3x3.
    """
    
    if not isinstance(tab, np.ndarray):
        raise TypeError("Tipo invalido para tab, se esperaba un ndarray")
    if tab.shape != (3,3):
        raise ValueError("Forma invalida para tab, se esperaba un arreglo 3x3")
    
    print(f" {tab[0,0]} │ {tab[0,1]} │ {tab[0,2]} ")
    print("───┼───┼───")
    print(f" {tab[1,0]} │ {tab[1,1]} │ {tab[1,2]} ")
    print("───┼───┼───")
    print(f" {tab[2,0]} │ {tab[2,1]} │ {tab[2,2]} ")

# ---------------------------------------------------------------
 
def escribir_tablero(tab, turno, cas) -> bool:
    """
    Funcion que escribe la letra segun el turno dentro del tablero en la casilla indicada, siempre y cuando la casilla este desocupada.
    
    Args:
    
        tab: El tablero en donde se realizara la escritura.
        turno (str): A quien le corresponde el turno (X o O).
        cas (int): La casilla en donde se escribira la letra (1-9).
        
    Returns:
    
        bool: True si la escritura tuvo exito, False si la casilla estaba ocupada.
        
    """
    
    if not isinstance(tab, np.ndarray):
        raise TypeError("Tipo invalido para tab, se esperaba un ndarray")
    if tab.shape != (3,3):
        raise ValueError("Forma invalida para tab, se esperaba un arreglo 3x3")
    if not isinstance(turno, str):
        raise TypeError("Tipo invalido para turno, se esperaba un str")
    if turno not in JUGADORES:
        raise ValueError("Valor invalido para turno, se esperaba 'O' o 'X'")
    if not isinstance(cas, int):
        raise TypeError("Tipo invalido para cas, se esperaba un entero")
    if cas < 1 or cas > 9:
        raise ValueError("Valor invalido para cas, se esperaba un valor entre [1,9]")
    
    # Encontrar los indices segun la casilla indicada.
    i = (cas - 1) // 3
    j = (cas - 1) % 3
        
    if tab[i, j] not in ["O", "X"]:
        tab[i, j] = turno
        return True
    
    return False

# ---------------------------------------------------------------

def determinar_ganador(tab, turno) -> bool:
    """
    Funcion que determina el ganador de la partida segun el tablero.
    
    Args:
    
        tab: El tablero a verificar.
        turno (str): Turno a verificar si gano.
        
    Returns:
    
        bool: True si la letra correspondiente al turno gano, False si no.
    """
    
    if not isinstance(tab, np.ndarray):
        raise TypeError("Tipo invalido para tab, se esperaba un ndarray")
    if tab.shape != (3,3):
        raise ValueError("Forma invalida para tab, se esperaba un arreglo 3x3")
    if not isinstance(turno, str):
        raise TypeError("Tipo invalido para turno, se esperaba un str")
    if turno not in JUGADORES:
        raise ValueError("Valor invalido para turno, se esperaba 'O' o 'X'")
    
    # Checar las filas
    for fila in tab:
        if np.all(fila == turno):
            return True
            
    # Checar las columnas
    for columna in tab.T:
        if np.all(columna == turno):
            return True
        
    # Checar la diagonal principal
    if np.all(np.diag(tab) == turno):
        return True
        
    # Checar la diagonal secundaria
    if np.all(np.diag(np.fliplr(tab)) == turno):
        return True
    
    return False 

# ---------------------------------------------------------------
# Proceso principal  
# ---------------------------------------------------------------

# Configuracion inicial del juego
tablero = np.array([[1,2,3],[4,5,6],[7,8,9]], np.str_)
turno = rand.choice(JUGADORES)
turno_sig = "O" if turno == "X" else "X"

# Evitar checar si hay ganador en los primeros 4 turnos (apartir del quinto turno es posible determinar un ganador).
for _ in range(4):
    # Mostrar tablero
    movercursor_inicio()
    mostrar_tablero(tablero)
    
    
    print(f"\nTurno: {turno}")
    
    # Capturar y validar la casilla
    while True:
        try:
            casilla = int(input("Elije una posicion: "))
            if 1 <= casilla <= 9:
                break
            print("Casilla invalida...")
        except ValueError:
            print("Error: El valor debe ser un entero")
    
    # Verificar que la casilla este desocupada
    exito = escribir_tablero(tablero, turno, casilla) 
    while not exito:
        print("Esa casilla ya esta ocupada...")
        casilla = int(input("Elije una posicion:  \b"))
        exito = escribir_tablero(tablero, turno, casilla)
       
    # Cambiar de turno
    turno, turno_sig = turno_sig, turno
    
num_turnos = 4
    
while num_turnos < 9:
    # Mostrar tablero
    movercursor_inicio()
    mostrar_tablero(tablero)
    
    
    print(f"\nTurno: {turno}")
    
    # Capturar y validar la casilla
    while True:
        try:
            casilla = int(input("Elije una posicion: "))
            if 1 <= casilla <= 9:
                break
            print("Casilla invalida...")
        except ValueError:
            print("Error: El valor debe ser un entero")
    
    # Verificar que la casilla este desocupada
    exito = escribir_tablero(tablero, turno, casilla) 
    while not exito:
        print("Esa casilla ya esta ocupada...")
        casilla = int(input("Elije una posicion:  \r"))
        exito = escribir_tablero(tablero, turno, casilla)
    
    # Determinar si hay ganador
    if determinar_ganador(tablero, turno):
        movercursor_inicio()
        mostrar_tablero(tablero)
        
        print(f"\n=====================================\n=========== GANARON LAS {turno} ===========\n=====================================")
        break
    
    # Cambiar de turno
    turno, turno_sig = turno_sig, turno
    
    num_turnos += 1
   
# Verificar si hubo empate
if num_turnos == 9:
    movercursor_inicio()
    mostrar_tablero(tablero)
        
    print("\n====================================\n=========== GANO EL GATO ===========\n====================================")