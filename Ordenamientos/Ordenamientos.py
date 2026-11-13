"""
"""

import numpy as np, time, os

VALOR_MIN = 1
VALOR_MAX = 15
RETRASO = 0.2

# -----------------------------------------------------------------

def mostrar_barras(arr, esperar = 0) -> None:
    
    time.sleep(esperar)
    print()
    
    for i in range(VALOR_MAX, 0, -1):      
        for num in arr:
            print("█  " if num >= i else "   ", end="")
        print()
    
    for num in arr:
        print(f"{num:<3}", end="")
        
    print()

# ----------------------------------------------------------------

def mover_iniciopantalla() -> None:
    
    print("\033[H", end="")
    
# ----------------------------------------------------------------

def apagar_cursor() -> None:
    
    print("\033[?25l", end="")
    
# ----------------------------------------------------------------

def encender_cursor() -> None:
    
    print("\033[?25h", end="")
    
# ----------------------------------------------------------------

def ord_burbuja(arr) -> None:
    
    for i in range(arr.size-1, 0, -1):
        ordenado = True 
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
                mover_iniciopantalla()
                mostrar_barras(arr, RETRASO)
                
                ordenado = False
        if ordenado:
            break
        
# -----------------------------------------------------------------

def ord_insercion(arr) -> None:
    
    for i in range(1, arr.size):
        tmp = arr[i]
        
        j = i-1
        while j >= 0 and arr[j] > tmp:
            arr[j+1] = arr[j]
            j -= 1
            
            mover_iniciopantalla()
            mostrar_barras(arr, RETRASO)
            
        arr[j+1] = tmp
        
        mover_iniciopantalla()
        mostrar_barras(arr, RETRASO)
        
# -----------------------------------------------------------------

def ord_seleccion(arr) -> None:
    
    for i in range(arr.size-1):
        pos_min = i
        for j in range(i+1, arr.size):
            if arr[pos_min] > arr[j]:
                pos_min = j
        arr[i], arr[pos_min] = arr[pos_min], arr[i]
        
        mover_iniciopantalla()
        mostrar_barras(arr, RETRASO)

# -----------------------------------------------------------------
# PROCESO PRINCIPAL
# -----------------------------------------------------------------

while True:
    try:
        n = int(input("Numero de elementos del arreglo [10, 30]: "))
        if 10 <= n <= 30:
            break
    except ValueError:
        print("Error: El valor debe ser un entero")
        
nums = np.random.randint(VALOR_MIN, VALOR_MAX+1, size=n)
mostrar_barras(nums)

input("Presione <ENTER> para comenzar con el ordenamiento por burbuja... ")
os.system("cls")
ord_burbuja(np.copy(nums))

input("Presione <ENTER> para comenzar con el ordenamiento por insercion... ")
os.system("cls")
ord_insercion(np.copy(nums))

input("Presione <ENTER> para comenzar con el ordenamiento por seleccion... ")
os.system("cls")
ord_seleccion(np.copy(nums))