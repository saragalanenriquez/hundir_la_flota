# Primero importamos todoas las librerias  que vamos a necesitar
import numpy as np
import random
import variables as v
import funciones as f


# Mensajes de bienvenida e instrucciones
print('¡Bienvenido a Hundir la Flota!')
print('Vamos con las reglas del juego.')
print('Deberás introducir las coordenas, fila y columna, hasta intentar hundir todos los barcos del adversario.')


# Tableros jugador
print('Este es tu tablero con las posiciones de tus barcos:\n', f.colocar_barcos(v.tablero_jugador_barcos))
print('En este tablero verás tus disparos realizados al adversario:\n', v.tablero_jugador_disparos)


# Tableros maquina
f.colocar_barcos(v.tablero_maquina_barcos)
v.tablero_maquina_disparos


print('¡Empieza a jugar!')
print('¡Mucha suerte!')


# Bucle disparos
while np.any(v.tablero_jugador_barcos=='B', axis=(0,1)) and np.any(v.tablero_maquina_barcos=='B', axis=(0, 1)):
    while np.any(v.tablero_maquina_barcos=='B', axis=(0, 1)):
        disparo_jugador = (int(input('Introuce el número de fila (entre el 0 y el 9):')), int(input('Introuce el número de columna (entre el 0 y el 9):')))
        v.tablero_jugador_disparos
        try:
            if v.tablero_maquina_barcos[disparo_jugador]=='B':
                v.tablero_jugador_disparos[disparo_jugador]='X'
                v.tablero_maquina_barcos[disparo_jugador]='X'
                print('¡Tocado!¡Le has dado a un barco del adversario!')
                print('Así están tus barcos:\n', v.tablero_jugador_barcos)
                print('Estos son tus disparos realizados: \n', v.tablero_jugador_disparos)
                print('¡Repites turno!')
                continue
            
            elif v.tablero_maquina_barcos[disparo_jugador]=='~':
                v.tablero_jugador_disparos[disparo_jugador]='A'
                v.tablero_maquina_barcos[disparo_jugador]='A'
                print('Le has dado al agua')
                print('Así están tus barcos:\n', v.tablero_jugador_barcos)
                print('Estos son tus disparos realizados: \n', v.tablero_jugador_disparos)

            else:
                print('Ya has probado con esas coordenadas, introduce otras diferentes.')
                continue
            break            
        except:
            print('Las coordenadas introducidas están fuera del tablero, intentalo otra vez (con números del 0 al 9)')
            continue

    while np.any(v.tablero_jugador_barcos=='B', axis=(0,1)):
        disparo_maquina = (random.randrange(10), random.randrange(10))
        if v.tablero_jugador_barcos[disparo_maquina]=='B':
            v.tablero_maquina_disparos[disparo_maquina]='X'
            v.tablero_jugador_barcos[disparo_maquina]='X'
            continue

        elif v.tablero_jugador_barcos[disparo_maquina]=='~':
            v.tablero_maquina_disparos[disparo_maquina]='A'
            v.tablero_jugador_barcos[disparo_maquina]='A'
        else:
            continue
        break


print('Fin del juego')

if np.all(v.tablero_maquina_barcos=='B', axis=(0, 1)):
    print('Has perdido, el enemigo te ha ganado esta vez.')
else:
    print('¡Has ganado! ¡Enhorabuena!')

