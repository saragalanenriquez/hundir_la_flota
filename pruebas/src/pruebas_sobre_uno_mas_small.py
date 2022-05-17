import random
import numpy as np
tablero_jugador_barcos = np.full(fill_value='~', shape=(3, 3))
tablero_jugador_disparos = np.full(fill_value='~', shape=(3, 3))
tablero_maquina_barcos = np.full(fill_value='~', shape=(3, 3))
tablero_maquina_disparos = np.full(fill_value='~', shape=(3, 3))
1

tablero_jugador_barcos[1:2, 1:2]='B'
tablero_jugador_barcos[0:1, 1:2]='B'
print('jugador barcos: \n', tablero_jugador_barcos)
tablero_maquina_barcos[2:3, 2:3]='B'
tablero_maquina_barcos[1:2, 2:3]='B'
print('maquina barcos: \n', tablero_maquina_barcos)


# Bucle disparos
while np.any(tablero_jugador_barcos=='B', axis=(0,1)) or np.any(tablero_maquina_barcos=='B', axis=(0, 1)):
    while True:
        disparo_jugador = (int(input('Num fila del 0 al 2:')), int(input('4Num columna del 0 al 2:')))
        tablero_jugador_disparos
        if tablero_maquina_barcos[disparo_jugador]=='B':
            tablero_jugador_disparos[disparo_jugador]='X'
            print('Tocado')
            print('jugador barcos:\n', tablero_jugador_barcos)
            print('jugador disparos: \n', tablero_jugador_disparos)
            continue
        
        elif tablero_maquina_barcos[disparo_jugador]=='~':
            tablero_jugador_disparos[disparo_jugador]='A'
            print('jugador barcos:\n')
            print(tablero_jugador_barcos)
            print('jugador disparos: \n', tablero_jugador_disparos)
            break
        else:
            # Podriamos probar un try except pero uffff
            print('mal')
            continue
    while True:
        disparo_maquina = (random.randrange(10), random.randrange(10))
        if tablero_jugador_barcos[disparo_maquina]=='B':
            tablero_maquina_disparos[disparo_maquina]='X'
            print('Tocado')
            print('maquina disparos: \n', tablero_maquina_disparos)
            continue

        elif tablero_jugador_barcos[disparo_maquina]=='~':
            tablero_maquina_disparos[disparo_maquina]='A'
            print('maquina disparos: \n', tablero_maquina_disparos)
            break