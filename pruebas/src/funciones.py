import variables as v
import random
import numpy as np
def sub_colocar_barcos(tablero, eslora, stop):
    i=0
    while i<stop:

        orient = random.choice(['N', 'S', 'E', 'O'])   
        
        # Posicion inicial del barco, np.array con dos valores, te da las primeras coordenadas
        current_pos = np.random.randint(10, size = 2)
        
        fila = current_pos[0]
        col = current_pos[1]
        
        # Recogemos las 4 posiciones colindantes a current_pos
        coors_posiN = tablero[fila:fila - eslora:-1, col]
        coors_posiE = tablero[fila, col: col + eslora]
        coors_posiS = tablero[fila:fila + eslora, col]
        coors_posiO = tablero[fila, col: col - eslora:-1]
        
        # Comprobamos si esas posiciones son validas
        # Orientacion Norte
        if orient == 'N' and 0 <= fila - eslora < 10 and 'B' not in coors_posiN:
            tablero[fila:fila - eslora:-1, col] = 'B'
            i+=1

        # Orientacion Este
        elif orient == 'E' and 0 <= col + eslora < 10 and 'B' not in coors_posiE:
            tablero[fila, col: col + eslora] = 'B'
            i+=1

        # Orientacion Sur
        elif orient == 'S' and 0 <= fila + eslora < 10 and 'B' not in coors_posiS:
            tablero[fila:fila + eslora, col] = 'B'
            i+=1

        # Orientacion Oeste
        elif orient == 'O' and 0 <= col - eslora < 10 and 'B' not in coors_posiO:
            tablero[fila, col: col - eslora:-1] = 'B'
            i+=1

        # No cumple con las dimensiones del tablero, o hay un barco ahi
        # Probamos con otra coordenada
        else:
            continue
    return tablero



def colocar_barcos(tablero):
    sub_colocar_barcos(tablero, 4, 1)
    sub_colocar_barcos(tablero, 3, 2)
    sub_colocar_barcos(tablero, 2, 3)
    sub_colocar_barcos(tablero, 1, 4)
    return tablero


