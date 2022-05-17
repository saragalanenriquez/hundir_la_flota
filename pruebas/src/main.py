# Primero importamos todoas las librerias  que vamos a necesitar
import numpy as np
import random
import variables as v
import funciones as f


# Mensajes de bienvenida e instrucciones
print('¡Bienvenido a Hundir la Flota!')
print('Vamos con las reglas del juego.')
print('Tienes que ir metiendo el numero de fila y el numero de columna que quieras hasta que consigas acabar con todos los barcos del enemigo...\nO hasta que el acabe con los tuyos.')


# Tableros jugador
print('Este es tu tablero con tus barcos colocados:\n', f.colocar_barcos(v.tablero_jugador_barcos))
print('Y este es el tablero en el que se irán reflejando tus movimientos sobre el tablero del enemigo:\n', v.tablero_jugador_disparos)


# Tableros maquina
# Aqui hay un print para verlo mejor en las pruebas, ELIMINAR
print(f.colocar_barcos(v.tablero_maquina_barcos))
v.tablero_maquina_disparos


print('¡Empieza a jugar!')
print('¡Mucha suerte!')


# Bucle disparos
while np.any(v.tablero_jugador_barcos=='B', axis=(0,1)) and np.any(v.tablero_maquina_barcos=='B', axis=(0, 1)):
    while np.any(v.tablero_maquina_barcos=='B', axis=(0, 1)):
        disparo_jugador = (int(input('Introuce el numero de fila (entre el 0 y el 9):')), int(input('Introuce el numero de columna (entre el 0 y el 9):')))
        v.tablero_jugador_disparos
        try:
            if v.tablero_maquina_barcos[disparo_jugador]=='B':
                v.tablero_jugador_disparos[disparo_jugador]='X'
                v.tablero_maquina_barcos[disparo_jugador]='X'
                print('Has tocado un barco del enemigo')
                print('Así va tu tablero:\n', v.tablero_jugador_barcos)
                print('Así va el tablero del enemigo: \n', v.tablero_jugador_disparos)
                print('¡Repites turno!')
                continue
            
            elif v.tablero_maquina_barcos[disparo_jugador]=='~':
                v.tablero_jugador_disparos[disparo_jugador]='A'
                v.tablero_maquina_barcos[disparo_jugador]='A'
                print('Le has dado al agua')
                print('Así va tu tablero:\n', v.tablero_jugador_barcos)
                print('Así va el tablero del enemigo: \n', v.tablero_jugador_disparos)
                break

            else:
                print('Ya has probado con esas coordenadas, introduce ahora otras diferentes.')
                continue
        except:
            print('Las coordenadas introducidas estan fuera del tablero, intentalo otra vez con unas menores.')
    while np.any(v.tablero_jugador_barcos=='B', axis=(0,1)):
        disparo_maquina = (random.randrange(10), random.randrange(10))
        if v.tablero_jugador_barcos[disparo_maquina]=='B':
            v.tablero_maquina_disparos[disparo_maquina]='X'
            v.tablero_jugador_barcos[disparo_maquina]='X'
            continue

        elif v.tablero_jugador_barcos[disparo_maquina]=='~':
            v.tablero_maquina_disparos[disparo_maquina]='A'
            v.tablero_jugador_barcos[disparo_maquina]='A'
            break
        else:
            continue
    break


print('Fin del juego')

if np.all(v.tablero_maquina_barcos=='B', axis=(0, 1)):
    print('Has perdido, el enemigo te ha ganado esta vez.')
else:
    print('¡Has ganado!')

