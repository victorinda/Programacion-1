"""
"""

import numpy as np
import random as rand

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
    print(f"───┼───┼───")
    print(f" {tab[1,0]} │ {tab[1,1]} │ {tab[1,2]} ")
    print(f"───┼───┼───")
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
    if turno not in ["O", "X"]:
        raise ValueError("Valor invalido para turno, se esperaba 'O' o 'X'")
    if not isinstance(cas, int):
        raise TypeError("Tipo invalido para cas, se esperaba un entero")
    
    # Encontrar los indices segun la casilla indicada.
    match cas:
        case 1:
            i = 0
            j = 0
        case 2:
            i = 0
            j = 1
        case 3:
            i = 0
            j = 2
        case 4:
            i = 1
            j = 0
        case 5:
            i = 1
            j = 1
        case 6:
            i = 1
            j = 2
        case 7:
            i = 2
            j = 0
        case 8:
            i = 2
            j = 1
        case 9:
            i = 2
            j = 3
        case _:
            raise ValueError("Valor invalido para cas, se esperaba un valor entre [1,9]")
        
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
    if turno not in ["O", "X"]:
        raise ValueError("Valor invalido para turno, se esperaba 'O' o 'X'")
    
    # Checar las filas
    gano = True
    for fila in tab:
        for dato in fila:
            if dato != turno:
                gano = False
                break
    
    if gano:
        return True
            
    # Checar las columnas
    gano = True
    for columna in tab.T:
        for dato in columna:
            if dato != turno:
                gano = False
                break
            
    if gano:
        return True
        
    # Checar la diagonal principal
    gano = True
    for dato in np.diag(tab):
        if dato != turno:
            gano = False
            break
        
    if gano:
        return True
    
    # Checar la diagonal secundaria
    gano = True
    for dato in np.diag(np.fliplr(tab)):
        if dato != turno:
            gano = False
            break
        
    if gano:
        return True
    
    return False 

# ---------------------------------------------------------------
# Proceso principal  
# ---------------------------------------------------------------

tablero = np.array([[1,2,3],[4,5,6],[7,8,9]], str)
turno = rand.choice(["O", "X"])
turno_sig = "X" if turno == "O" else "O"

while True:
    # Mostrar tablero
    movercursor_inicio()
    mostrar_tablero(tablero)
    
    
    print(f"\nTurno: {turno}")
    
    casilla = int(input("Elije una posicion: "))
    
    # Verificar que la casilla este desocupada
    exito = escribir_tablero(tablero, turno, casilla) 
    while not exito:
        print("Esa casilla ya esta ocupada...")
        casilla = int(input("Elije una posicion: "))
        exito = escribir_tablero(tablero, turno, casilla)
    
    # Determinar si hay ganador
    if determinar_ganador(tablero, turno):
        print(f"Ganaron las {turno}!")
        break
    
    # Cambiar de turno
    turno, turno_sig = turno_sig, turno
    