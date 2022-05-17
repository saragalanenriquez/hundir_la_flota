import numpy as np
import random
import variables as v
import funciones as f


# Tableros jugador
print('jugador barcos:\n', f.colocar_barcos(v.tablero_jugador_barcos))
print('jugador disparos:\n', v.tablero_jugador_disparos)

# Tableros maquina
print('maquina barcos:\n', f.colocar_barcos(v.tablero_maquina_barcos))
print('maquina disparos:\n', v.tablero_maquina_disparos)


# Bucle disparos
while 'B' in v.tablero_jugador_barcos or 'B' in v.tablero_maquina_barcos:
    while True:
        disparo_jugador = (int(input('Num fila del 0 al 9:')), int(input('Num columna del 0 al 9:')))
        v.tablero_jugador_disparos
        if v.tablero_maquina_barcos[disparo_jugador]=='B':
            v.tablero_jugador_disparos[disparo_jugador]='X'
            print('Tocado')
            print('jugador barcos:\n', v.tablero_jugador_barcos)
            print('jugador disparos: \n', v.tablero_jugador_disparos)
            continue
        
        elif v.tablero_maquina_barcos[disparo_jugador]=='~':
            v.tablero_jugador_disparos[disparo_jugador]='A'
            print('jugador barcos:\n')
            print(v.tablero_jugador_barcos)
            print('jugador disparos: \n', v.tablero_jugador_disparos)
            break
        else:
            # Podriamos probar un try except pero uffff
            print('mal')
            continue
    while True:
        disparo_maquina = (random.randrange(10), random.randrange(10))
        if v.tablero_jugador_barcos[disparo_maquina]=='B':
            v.tablero_maquina_disparos[disparo_maquina]='X'
            print('Tocado')
            print('maquina disparos: \n', v.tablero_maquina_disparos)
            continue

        elif v.tablero_jugador_barcos[disparo_maquina]=='~':
            v.tablero_maquina_disparos[disparo_maquina]='A'
            print('maquina disparos: \n', v.tablero_maquina_disparos)
            break