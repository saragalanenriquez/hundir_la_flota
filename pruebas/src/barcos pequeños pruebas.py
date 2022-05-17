import numpy as np
import random
tablero_jugador_barcos = np.full(fill_value='~', shape=(3, 3))
tablero_jugador_disparos = np.full(fill_value='~', shape=(3, 3))
tablero_maquina_barcos = np.full(fill_value='~', shape=(3, 3))
tablero_maquina_disparos = np.full(fill_value='~', shape=(3, 3))


tablero_jugador_barcos[1:2, 0:2]='B'
print('jugador barcos: \n', tablero_jugador_barcos)
tablero_maquina_barcos[1:2, 1:3]='B'
print('maquina barcos: \n', tablero_maquina_barcos)


while np.any(tablero_jugador_barcos=='B', axis=(0,1)) and np.any(tablero_maquina_barcos=='B', axis=(0,1)):
    while np.any(tablero_maquina_barcos=='B', axis=(0,1)):
        disparo_jugador = (int(input('Num fila del 0 al 2:')), int(input('Num columna del 0 al 2:')))
        tablero_jugador_disparos
        try:
            if tablero_maquina_barcos[disparo_jugador]=='B':
                tablero_jugador_disparos[disparo_jugador]='X'
                tablero_maquina_barcos[disparo_jugador]='X'
                print('Has dado al un barco')
                print('jugador barcos:\n', tablero_jugador_barcos)
                print('jugador disparos: \n', tablero_jugador_disparos)
                continue
            
            elif tablero_maquina_barcos[disparo_jugador]=='~':
                tablero_jugador_disparos[disparo_jugador]='A'
                tablero_maquina_barcos[disparo_jugador]='A'
                print('Agua')
                print('jugador barcos:\n', tablero_jugador_barcos)
                print('jugador disparos: \n', tablero_jugador_disparos)

            else:
                print('Ya has probado esas coordenadas, introduce ahora otras diferentes')
                continue
            break
        except:
            print('Las coordenadas introducidas están fura del tablero, intentalo otra vez con unas menores')
            continue

    while np.any(tablero_jugador_barcos=='B', axis=(0,1)):
        disparo_maquina = (random.randrange(2), random.randrange(2))
        if tablero_jugador_barcos[disparo_maquina]=='B':
            print(disparo_maquina)
            tablero_maquina_disparos[disparo_maquina]='X'
            tablero_jugador_barcos[disparo_maquina]='X'
            print('La maquina te ha dado')
            print('jugador barcos:\n', tablero_jugador_barcos)
            continue

        elif tablero_jugador_barcos[disparo_maquina]=='~':
            tablero_maquina_disparos[disparo_maquina]='A'
            tablero_jugador_barcos[disparo_maquina]='A'
            print('Disparo de la maquina al agua')
            print('jugador barcos:\n', tablero_jugador_barcos)
        else:
            continue
        break

print('fin de la Partida')


if np.any(tablero_maquina_barcos=='B', axis=(0,1)):
    print('gana la maquina') 
else:
    print('has ganado')