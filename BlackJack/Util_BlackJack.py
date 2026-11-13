"""
Module: Util_BlackJack.py

Descripción:
    Módulo que contiene las funciones y constantes necesarias
    para gestionar la lógica de una partida de Blackjack.

Incluye:
    - Creación y validación de la baraja.
    - Barajado y extracción de cartas.
    - Cálculo de puntuaciones.
    - Gestión de turnos.
    - Determinación del resultado de la partida.
"""
"""
Archivo: Util_BlackJack.py
Descripcion: Modulo necesario para la logica de la interfaz grafica de Blackjack.
Autores: Victor Hugo Inda Miramontes, Diego Rafael Nava Hernandez
Fecha: 10/11/2026
"""

PALOS = ('♥', '♦', '♣', '♠')
""" Todos los palos o simbolos de la baraja inglesa """

DENOMINACIONES = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
""" Todas la denominaciones de la baraja inglesa """

###################################################################################################################################

def crear_baraja() -> list[tuple[str, str]]:
    """
    Retorna una lista (baraja) de 52 2-tuplas (cartas) que contienen cada una de las denominaciones y palos de la baraja inglesa con el formato (denominacion, palo).
    
    Returns:
    
        list[tuple[str, str]]: Las 52 cartas de la baraja inglesa
        
    Examples:
    
        >>> crear_baraja()
        [('A', '♥'), ('A', '♦'), ('A', '♣'), ('A', '♠'), ('2', '♥'), ('2', '♦'), ('2', '♣'), ('2', '♠'), ('3', '♥'), ('3', '♦'), ('3', '♣'), ('3', '♠'), ('4', '♥'), ('4', '♦'), ('4', '♣'), ('4', '♠'), ('5', '♥'), ('5', '♦'), ('5', '♣'), ('5', '♠'), ('6', '♥'), ('6', '♦'), ('6', '♣'), ('6', '♠'), ('7', '♥'), ('7', '♦'), ('7', '♣'), ('7', '♠'), ('8', '♥'), ('8', '♦'), ('8', '♣'), ('8', '♠'), ('9', '♥'), ('9', '♦'), ('9', '♣'), ('9', '♠'), ('10', '♥'), ('10', '♦'), ('10', '♣'), ('10', '♠'), ('J', '♥'), ('J', '♦'), ('J', '♣'), ('J', '♠'), ('Q', '♥'), ('Q', '♦'), ('Q', '♣'), ('Q', '♠'), ('K', '♥'), ('K', '♦'), ('K', '♣'), ('K', '♠')]
    
    """
    
    return [(denom, palo) for denom in DENOMINACIONES for palo in PALOS]

###################################################################################################################################

def validar_baraja(baraja: list[tuple[str, str]]) -> None:
    """
    Dada una lista, valida que sea una lista de cartas de la baraja inglesa con el formato list[tuple[str, str]]), donde el elemento 0 de la tupla esta en DENOMINACIONES y el elemento 1 de la tupla esta en PALOS.
    
    Args:
        
        baraja (list[tuple[str, str]]): Baraja que se va a validar.
        
    Raises:
        
        TypeError: Si alguno de los datos de la baraja es invalido.
        ValueError: Si la longitud o valor de alguno de los datos de la baraja es invalido.
    
    Examples:
    
        >>> validar_baraja([('6', '♠'), "Hola mundo", 23])
        Traceback (most recent call last):
        ...
        TypeError: Tipo inesperado para elemento en baraja, se esperaba una tupla
        
        >>> validar_baraja([('C', '♠', 'A'), ('Q', '♦'), ('A', '♣')])
        Traceback (most recent call last):
        ...
        ValueError: La longitud de la tupla no coincide, se esperaba una 2-tupla
        
        >>> validar_baraja([('9', '♣'), ('J', 'X'), ('K', '♦'), ('2', '♣'), ('6', '♦')])
        Traceback (most recent call last):
        ...
        ValueError: Palo invalido para elemento[1] de tupla en baraja
        
        >>> validar_baraja([('10', '♥'), ('8', '♥'), ('8', '♦'), ('7', '♣'), ('5', '♠'), ('J', '♦'), ('10', '♣')])
        None
    """
    
    if not isinstance(baraja, list):
        raise TypeError("Tipo inesperado para baraja, se esperaba una lista")
    for carta in baraja:
        if not isinstance(carta, tuple):
            raise TypeError("Tipo inesperado para elemento en baraja, se esperaba una tupla")
        if len(carta) != 2:
            raise ValueError("La longitud de la tupla no coincide, se esperaba una 2-tupla")
        denom, palo = carta
        if not isinstance(denom, str):
            raise TypeError("Tipo inesperado para elemento[0] de tupla en baraja, se esperaba una cadena")
        if not isinstance(palo, str):
            raise TypeError("Tipo inesperado para elemento[1] de tupla en baraja, se esperaba una cadena")
        if denom not in DENOMINACIONES:
            raise ValueError("Denominacion invalida para elemento[0] de tupla en baraja")
        if palo not in PALOS:
            raise ValueError("Palo invalido para elemento[1] de tupla en baraja")
        
###################################################################################################################################

def barajear(baraja: list[tuple[str, str]]) -> None:
    """
    Reordena al azar las posiciones de las cartas dentro de una baraja.
    
    Args:
        
        baraja (list[tuple[str, str]]): La baraja que se va a barajear.
        
    Raises:
    
        TypeError: Si alguno de los datos de la baraja es invalido.
        ValueError: Si la longitud o valor de alguno de los datos de la baraja es invalido.
        
    Examples:
    
        >>> baraja = crear_baraja()
        >>> barajear(baraja)
        >>> baraja
        [('5', '♦'), ('3', '♣'), ('Q', '♥'), ('K', '♠'), ('2', '♠'), ('10', '♥'), ('8', '♥'), ('8', '♦'), ('7', '♣'), ('5', '♠'), ('J', '♦'), ('10', '♣'), ('3', '♠'), ('6', '♣'), ('Q', '♣'), ('4', '♥'), ('4', '♣'), ('J', '♣'), ('9', '♣'), ('J', '♥'), ('K', '♦'), ('2', '♣'), ('6', '♦'), ('7', '♠'), ('6', '♠'), ('Q', '♦'), ('A', '♣'), ('2', '♥'), ('10', '♠'), ('4', '♦'), ('9', '♠'), ('4', '♠'), ('K', '♣'), ('5', '♣'), ('9', '♦'), ('A', '♦'), ('A', '♠'), ('7', '♦'), ('6', '♥'), ('3', '♦'), ('7', '♥'), ('5', '♥'), ('J', '♠'), ('Q', '♠'), ('A', '♥'), ('K', '♥'), ('10', '♦'), ('2', '♦'), ('9', '♥'), ('8', '♣'), ('8', '♠'), ('3', '♥')]
        
        >>> baraja = [('6', '♠'), ('Q', '♦'), ('A', '♣'), ('2', '♥'), ('10', '♠')]
        >>> barajear(baraja)
        >>> baraja
        [('A', '♣'), ('10', '♠'), ('Q', '♦'), ('2', '♥'), ('6', '♠')]
        
    """
    
    validar_baraja(baraja)
        
    from random import shuffle
    
    shuffle(baraja)

###################################################################################################################################

def sacar_carta(baraja: list[tuple[str, str]]) -> tuple[str, str]:
    """
    Elimina la ultima carta de una baraja y lo retorna.
    
    Args:
        
        baraja(list[tuple[str, str]]): La baraja a la cual se le va a sacar su ultima carta.
        
    Returns:
    
        tuple[str, str]: La carta que se saco de la baraja.
        
    Raises:
    
        TypeError: Si alguno de los datos de la baraja es invalido.
        ValueError: Si la longitud o valor de alguno de los datos de la baraja es invalido.
        
    Examples:
        
        >>> baraja = [('7', '♠'), ('10', '♠'), ('Q', '♥')]
        >>> sacar_carta(baraja)
        ('Q', '♥')
        >>> baraja
        [('7', '♠'), ('10', '♠')]
        
        >>> baraja = crear_baraja()
        >>> sacar_carta(baraja)
        ('K', '♠')
        
    """
    
    validar_baraja(baraja)
    
    return baraja.pop()

###################################################################################################################################

def puntuacion(baraja: list[tuple[str, str]]) -> int:
    """
    Calcula cuantos puntos vale una baraja.
    
    Args:
    
        baraja(list[tuple[str, str]]): La baraja a la cual se le calculara la puntuacion.
    
    Returns:
        
        int: La puntuacion de la baraja.
        
    Raises:
    
        TypeError: Si alguno de los datos de la baraja es invalido.
        ValueError: Si la longitud o valor de alguno de los datos de la baraja es invalido.
        
    Examples:
        
        >>> baraja = crear_baraja()
        >>> puntuacion(baraja)
        340
        
        >>> baraja = [('A', '♠'), ('10', '♥'), ('3', '♥')]
        >>> puntuacion(baraja)
        14
        
        >>> baraja = ['Hola mundo', True]
        Traceback (most recent call last):
        ...
        TypeError: Tipo inesperado para elemento en baraja, se esperaba una tupla
        
    """
    
    validar_baraja(baraja)
        
    puntos = 0 
    ases = 0
    # Checar cada carta de la baraja.
    for carta in baraja:
        denom = carta[0]
        # Segun la denominacion, añadir puntos.
        if denom == 'A':
            puntos += 11
            ases += 1
        elif denom in ['J', 'Q', 'K']:
            puntos += 10
        else:
            puntos += int(denom)
    # Si los puntos se pasan de 21 y tiene ases, cambiar el valor de los ases segun convenga.
    while puntos > 21 and ases > 0:
        puntos -= 10
        ases -= 1
        
    return puntos
###################################################################################################################################
def  repartir_cartas():
    """
    Crea una baraja, la mezcla y reparte dos cartas al jugador y dos al dealer.

    Returns:
        tuple: Una tupla con los siguientes elementos:
            - list[tuple[str, str]]: Mano inicial del jugador.
            - list[tuple[str, str]]: Mano inicial del dealer.
            - list[tuple[str, str]]: Cartas restantes de la baraja.
                
    """
    baraja = crear_baraja()
    barajear(baraja)

    mano_jugador = []
    mano_dealer = []
    for _ in range(2):
        mano_jugador.append(sacar_carta(baraja))
        mano_dealer.append(sacar_carta(baraja))
    return mano_jugador, mano_dealer, baraja
###################################################################################################################################
def blackjack_natural(mano: list[tuple[str, str]]) -> bool:
    """
    Comprueba si una mano tiene Blackjack natural.

    Un Blackjack natural ocurre cuando las dos cartas iniciales
    contienen un as y una carta con valor de 10 puntos.

    Args:
        mano (list[tuple[str, str]]): Mano que se desea comprobar.

    Returns:
        bool: True si la mano tiene Blackjack natural; False en caso contrario.
            
    """
    # Esto unicamente al principio de la partida
    
    if len(mano) == 2:
        es_As = False 
        es_valor10 = False 
        for carta in mano:
            denom = carta[0]
            if denom == "A":
                es_As = True 
            if denom in ("10", "J", "Q", "K"):
                es_valor10 = True
                
        if es_As == True and es_valor10 == True:
            return True
        else:
            return False
    return False
###################################################################################################################################
def pedir_carta(mano_jugador: list[tuple[str, str]] , baraja: list[tuple[str, str]]) -> bool:
    """
    Extrae una carta de la baraja y la añade a la mano del jugador.

    Args:
        mano_jugador (list[tuple[str, str]]): Mano del jugador.
        baraja (list[tuple[str, str]]): Cartas disponibles para robar.

    Returns:
        bool: True si el jugador supera los 21 puntos; False en caso contrario.
            
    """
    
    mano_jugador.append(sacar_carta(baraja))
    
    puntos = puntuacion(mano_jugador)
    
    return puntos > 21
###################################################################################################################################
def turno_dealer(mano_dealer: list[tuple[str, str]] , baraja: list[tuple[str, str]]) -> None :
    """
    Gestiona automáticamente el turno del dealer.

    El dealer solicita cartas mientras su puntuación sea inferior a 17.

    Args:
        mano_dealer (list[tuple[str, str]]): Mano del dealer.
        baraja (list[tuple[str, str]]): Cartas disponibles para robar.

    """
    puntos = puntuacion(mano_dealer)
    
    while puntos < 17:
        pedir_carta(mano_dealer, baraja)
        puntos = puntuacion(mano_dealer)
        if puntos > 21:
            break 
        
###################################################################################################################################
def turno_jugador(mano_jugador: list[tuple[str, str]], baraja: list[tuple[str, str]], accion: str) -> str:
    """
    Procesa una acción seleccionada por el jugador.

    Las acciones disponibles son pedir una carta o plantarse.

    Args:
        mano_jugador (list[tuple[str, str]]): Mano actual del jugador.
        baraja (list[tuple[str, str]]): Cartas disponibles para robar.
        accion (str): Acción que realizará el jugador.

    Returns:
        str: Estado del turno:
            - "jugador_se_paso": El jugador superó los 21 puntos.
            - "jugador_continua": El jugador puede continuar.
            - "jugador_se_planta": El jugador terminó su turno.

    Raises:
        ValueError: Si la acción proporcionada no es válida.
            
    """
    if accion == "pedir":
        se_paso = pedir_carta(mano_jugador, baraja)
        if se_paso:
            return "jugador_se_paso"
        else:
            return "jugador_continua"
    
    elif accion == "plantarse":
        return "jugador_se_planta"
    
    else:
        raise ValueError("Acción no válida")
    
###################################################################################################################################
def determinar_ganador(mano_jugador, mano_dealer):
    """
    Compara las puntuaciones del jugador y del dealer para determinar
    el resultado de la partida.

    Args:
        mano_jugador: Mano final del jugador.
        mano_dealer: Mano final del dealer.

    Returns:
        str: Resultado de la partida:
            - "jugador_gana": Victoria del jugador.
            - "dealer_gana": Victoria del dealer.
            - "empate": Ambas puntuaciones son iguales.
                
    """
    jugador = puntuacion(mano_jugador)
    dealer = puntuacion(mano_dealer)

    if jugador > 21:
        return "dealer_gana"
    elif dealer > 21:
        return "jugador_gana"
    elif jugador > dealer:
        return "jugador_gana"
    elif dealer > jugador:
        return "dealer_gana"
    else:
        return "empate"

###################################################################################################################################    
def partida():
    """
    Inicia una nueva partida y comprueba si alguno de los participantes
    obtiene Blackjack natural en el reparto inicial.

    Returns:
        tuple: Una tupla con:
            - list[tuple[str, str]]: Mano del jugador.
            - list[tuple[str, str]]: Mano del dealer.
            - list[tuple[str, str]]: Baraja restante.
            - str: Estado inicial de la partida:
                "jugador_blackjack", "dealer_blackjack",
                "empate" o "en_curso".
                    
    """
    mano_jugador, mano_dealer, baraja = repartir_cartas()
    
    jugador = blackjack_natural(mano_jugador)
    dealer =  blackjack_natural(mano_dealer)
    
    if jugador == True and dealer == False:
        estado = "jugador_blackjack"
    elif jugador == False and dealer == True:
        estado = "dealer_blackjack"
    elif jugador == True and dealer == True:
        estado = "empate"
    else:
        estado = "en_curso"
        
    return mano_jugador, mano_dealer, baraja, estado
####################################################################################################################################
if __name__ == "__main__":
    mano_jugador = [('A', '♥'), ('K', '♦')]
    mano_dealer = [('A', '♠'), ('Q', '♣')]

    jugador = blackjack_natural(mano_jugador)
    dealer = blackjack_natural(mano_dealer)

    if jugador and dealer:
        estado = "empate"

    print("Jugador:", jugador)
    print("Dealer:", dealer)
    print("Estado:", estado)