"""
Archivo: Util_BlackJack.py
Descripcion: Interfaz grafica de Blackjack.
Autores: Victor Hugo Inda Miramontes, Diego Rafael Nava Hernandez
Fecha: 10/11/2026
"""

######################################################################
# Importación de módulos y funciones
######################################################################
import tkinter as tk

from Util_BlackJack import (
    partida,
    turno_jugador,
    turno_dealer,
    determinar_ganador,
    puntuacion
)

mano_jugador, mano_dealer, baraja, estado = partida()

######################################################################
# Configuración de la ventana principal
######################################################################
ventana = tk.Tk()
ventana.title("BlackJack")
ventana.geometry("800x600")
ventana.resizable(False, False)

ventana.configure(bg="#176B45")

######################################################################
# Creación de las zonas del dealer y jugador
######################################################################

# Zona del dealer
zona_dealer = tk.LabelFrame(
    ventana,
    text="DEALER: ?",
    font=("Arial", 14, "bold"),
    bg="#176B45",
    fg="white"
   ) 
    
zona_dealer.pack(pady=20, padx=20, fill="both", expand=True)    
  


# Zona del jugador
zona_jugador = tk.LabelFrame(
    ventana,
    text=f"JUGADOR: {puntuacion(mano_jugador)}",
    font=("Arial", 14, "bold"),
    bg="#176B45",
    fg="white"
)


zona_jugador.pack(pady=20, padx=20, fill="both", expand=True)


etiqueta_estado = tk.Label(
    ventana,
    text="Partida en curso",
    font=("Arial", 14, "bold"),
    bg="#176B45",
    fg="white"
)
etiqueta_estado.pack(pady=8)

################################################################################
# Funciones de interacción de los botones
################################################################################
def accion_pedir():
    """
    Gestiona la acción de pedir una carta durante el turno del jugador.

    Solicita una carta, actualiza la representación gráfica de la mano
    y comprueba si el jugador supera los 21 puntos.

    Si el jugador se pasa, muestra las cartas del dealer y desactiva
    los botones de pedir carta y plantarse.
    """
    resultado = turno_jugador(mano_jugador, baraja, "pedir")
    zona_jugador.config(text=f"JUGADOR: {puntuacion(mano_jugador)}")

    lienzo_jugador.delete("all")
    dibujar_mano(lienzo_jugador, mano_jugador)

    if resultado == "jugador_se_paso":
        etiqueta_estado.config(text="¡Te pasaste! Gana el dealer")

        lienzo_dealer.delete("all")
        dibujar_mano(lienzo_dealer, mano_dealer)
        
        zona_dealer.config(text=f"DEALER: {puntuacion(mano_dealer)}")

        boton_pedir.config(state="disabled")
        boton_plantarse.config(state="disabled")


def accion_plantarse():
    """
    Finaliza el turno del jugador y ejecuta el turno automático del dealer.

    Actualiza la representación gráfica de las cartas del dealer,
    determina el ganador de la partida y muestra el resultado.

    Finalmente, desactiva los botones de pedir carta y plantarse.
    """
    turno_jugador(mano_jugador, baraja, "plantarse")

    # Turno automático del dealer
    turno_dealer(mano_dealer, baraja)

    # Mostrar todas las cartas del dealer
    lienzo_dealer.delete("all")
    dibujar_mano(lienzo_dealer, mano_dealer)
    
    # Mostrar la puntuacion del dealer
    zona_dealer.config(text=f"DEALER: {puntuacion(mano_dealer)}")

    # Determinar ganador
    resultado = determinar_ganador(mano_jugador, mano_dealer)

    if resultado == "jugador_gana":
        etiqueta_estado.config(text="¡Ganaste!")

    elif resultado == "dealer_gana":
        etiqueta_estado.config(text="¡Ganó el dealer!")

    elif resultado == "empate":
        etiqueta_estado.config(text="¡Empate!")

    # Desactivar botones
    boton_pedir.config(state="disabled")
    boton_plantarse.config(state="disabled")

def accion_rejugar():
    """
    Inicia una nueva partida mediante la función partida().

    Reinicia las manos y la baraja, actualiza los lienzos y comprueba
    si alguno de los participantes obtiene Blackjack natural.

    Habilita o deshabilita los botones de acción según el estado
    de la nueva partida.
    """
    global mano_jugador, mano_dealer, baraja, estado

    mano_jugador, mano_dealer, baraja, estado = partida()

    lienzo_jugador.delete("all")
    lienzo_dealer.delete("all")

    dibujar_mano(lienzo_jugador, mano_jugador)
    dibujar_mano_dealer(lienzo_dealer, mano_dealer)
    
    zona_jugador.config(text=f"JUGADOR: {puntuacion(mano_jugador)}")
    zona_dealer.config(text="DEALER: ?")

    if estado == "en_curso":
        etiqueta_estado.config(text="Partida en curso")

        boton_pedir.config(state="normal")
        boton_plantarse.config(state="normal")

    else:
        lienzo_dealer.delete("all")
        dibujar_mano(lienzo_dealer, mano_dealer)

        boton_pedir.config(state="disabled")
        boton_plantarse.config(state="disabled")
        
        zona_dealer.config(text=f"DEALER: {puntuacion(mano_dealer)}")

        if estado == "jugador_blackjack":
            
            etiqueta_estado.config(text="¡Blackjack del jugador! Ganaste")

        elif estado == "dealer_blackjack":
            
            etiqueta_estado.config(text="¡Blackjack del dealer! Perdiste")
            
        elif estado == "empate":
            
            etiqueta_estado.config(text="¡Blackjack de ambos! Empate")
    
#############################################################################    
# Creación de los botones
#############################################################################

zona_botones = tk.Frame(ventana, bg="#176B45")

boton_pedir = tk.Button(
    zona_botones,
    text="Pedir carta",
    command=accion_pedir
)
boton_pedir.pack(side="left", padx=10)

boton_plantarse = tk.Button(
    zona_botones,
    text="Plantarse",
    command=accion_plantarse
)
boton_plantarse.pack(side="left", padx=10)

boton_rejugar = tk.Button(
    zona_botones,
    text="Rejugar",
    command=accion_rejugar
)
boton_rejugar.pack(side="left", padx=10)

zona_botones.pack(pady=10)

#################################################################
# Creación de los lienzos
#################################################################
lienzo_dealer = tk.Canvas(
    zona_dealer,
    bg="#176B45",
    highlightthickness=0,
    height=180,
    width=760
)
lienzo_dealer.pack(fill="both", expand=True)

lienzo_jugador = tk.Canvas(
    zona_jugador,
    bg="#176B45",
    highlightthickness=0,
    height=180,
    width=760
)
lienzo_jugador.pack(fill="both", expand=True)

####################################################################################
# Funciones para dibujar las cartas
####################################################################################

def dibujar_carta(lienzo, x, y, valor, palo):
    """
    Dibuja una carta individual en un lienzo de Tkinter.

    Args:
        lienzo: Canvas donde se representará la carta.
        x (int): Coordenada horizontal inicial.
        y (int): Coordenada vertical inicial.
        valor (str): Denominación de la carta.
        palo (str): Símbolo del palo de la carta.

    La carta muestra su denominación en las esquinas y el símbolo
    del palo en el centro. Los corazones y diamantes se representan
    en rojo; los tréboles y picas, en negro.
    """
    ancho = 100
    alto = 145

    color = "red" if palo in ("♥", "♦") else "black"

    # Cuerpo de la carta
    lienzo.create_rectangle(
        x, y,
        x + ancho, y + alto,
        fill="white",
        outline="black",
        width=2
    )

    # Valor en la esquina superior izquierda
    lienzo.create_text(
        x + 12, y + 15,
        text=valor,
        fill=color,
        font=("Arial", 14, "bold")
    )

    # Símbolo central
    lienzo.create_text(
        x + ancho // 2,
        y + alto // 2,
        text=palo,
        fill=color,
        font=("Arial", 42, "bold")
    )

    # Valor invertido en la esquina inferior derecha
    lienzo.create_text(
        x + ancho - 12,
        y + alto - 15,
        text=valor,
        fill=color,
        font=("Arial", 14, "bold"),
        angle=180
    )
    
def dibujar_mano(lienzo, mano):
    """
    Dibuja todas las cartas de una mano en un lienzo de Tkinter.

    Args:
        lienzo: Canvas donde se dibujarán las cartas.
        mano (list[tuple[str, str]]): Lista de cartas que se representarán.

    Las cartas se distribuyen horizontalmente y se centran
    en el lienzo.
    """
    for indice, carta in enumerate(mano):
        denominacion, palo = carta
        x = (800 - (len(mano) * 120 - 20)) // 2 + indice * 120
        y = 30
        dibujar_carta(lienzo, x, y, denominacion, palo)
        
def dibujar_mano_dealer(lienzo, mano):
    """
    Dibuja la mano del dealer ocultando sus cartas posteriores a la primera.

    Args:
        lienzo: Canvas donde se dibujará la mano.
        mano (list[tuple[str, str]]): Lista de cartas del dealer.

    La primera carta se muestra normalmente y las siguientes
    se representan mediante el reverso de una carta.
    """
    for indice, carta in enumerate(mano):
        denominacion, palo = carta
        x = (800 - (len(mano) * 120 - 20)) // 2 + indice * 120
        y = 30
        if indice == 0:
            dibujar_carta(lienzo, x, y, denominacion, palo)
        else:
            dibujar_reverso(lienzo, x, y)
    

def dibujar_reverso(lienzo, x, y):
    """
    Dibuja el reverso de una carta en un lienzo de Tkinter.

    Args:
        lienzo: Canvas donde se representará el reverso.
        x (int): Coordenada horizontal inicial.
        y (int): Coordenada vertical inicial.

    Utiliza rectángulos y un polígono para crear el diseño
    del reverso de la carta.
    """
    ancho = 100
    alto = 145
    
    lienzo.create_rectangle(
        x, y,
        x + ancho, y + alto,
        fill="darkblue",
        outline="white",
        width=2
    )
    
    lienzo.create_rectangle(
        x + 8, y + 8,
        x + ancho - 8, y + alto - 8,
        fill="darkblue",
        outline="white",
        width=2
    )
    
    centro_x = x + ancho // 2
    centro_y = y + alto // 2
    
    lienzo.create_polygon(
    centro_x, centro_y - 30,
    centro_x + 20, centro_y,
    centro_x, centro_y + 30,
    centro_x - 20, centro_y,
    fill="white",
    outline="white"
)

###############################################################################
# Inicio y configuración de la partida
###############################################################################

dibujar_mano(lienzo_jugador, mano_jugador)
dibujar_mano_dealer(lienzo_dealer, mano_dealer)
    
if estado == "en_curso":
    etiqueta_estado.config(text="Partida en curso")

elif estado == "jugador_blackjack":
    zona_dealer.config(text=f"DEALER: {puntuacion(mano_dealer)}")
    etiqueta_estado.config(text="¡Blackjack del jugador!")

elif estado == "dealer_blackjack":
    zona_dealer.config(text=f"DEALER: {puntuacion(mano_dealer)}")
    etiqueta_estado.config(text="¡Blackjack del dealer!")

else:
    zona_dealer.config(text=f"DEALER: {puntuacion(mano_dealer)}")
    etiqueta_estado.config(text="¡Empate!")
    
if estado != "en_curso":
    lienzo_dealer.delete("all")
    dibujar_mano(lienzo_dealer, mano_dealer)

    boton_pedir.config(state="disabled")
    boton_plantarse.config(state="disabled")

# Ejecución del bucle principal de Tkinter
ventana.mainloop()