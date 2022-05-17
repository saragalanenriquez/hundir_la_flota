# Hundir la Flota
#### Data Science Full-Time abril 2022

## Descripción del proyecto:
1. Creación de tableros mediante numpy arrays.
2. Función inicial para colocar barcos de cualquier eslora.
3. Otra función que llama a la anterior para crear un numero de barcos de determinada eslora.
4. Las casillas de los tableros vacíos están rellenas de ~, que represneatn el agua. Los barcos están representados con la letra B. Los disparos a un barco están representados con la X y los disparos al agua con una A.
5. El buble while principal es que inicia los siguientes mientras que queden B (barcos) en el tablero.
6. El primer bucle interno realiza los disparos pidiendo inputs al usuario por filas y columnas (coordenadas), teniendo como condición que haya barcos en el tablero del adversario.
7. El segundo bucle interno realiza disparos aleatorios por parte del adversario, teniendo como condición que haya barcos en el tablero del jugador. 
8. Meidante el flujo de control final se indica quien es el ganadr de la partida y cuando acaba esta.

Hemos dividido el código en tres scripts:
1. Variables: aquí hemos asignado los tableros a nuestras variables principales.
2. Funciones: en este script hemmos definido las funciones que colocan los barcos en los tableros.
3. Main: en este script hemos importado los dos anteriores y hemos desarrollado todo el código necesario para la ejecución del juego.

## Librerias y recursos:
Hemos utilizado la libreria numpy y random, además de las propias creadas para el desarrollo del código, varibales y funciones.
Como recurso extra a los vistos en clase, hemos utilizado los métodos de numpy array any y all, para construir la condición de nuestro while.

## Commit:
El planteamiento general del desarrollo del código se ha realizado de manera conjunta.
* Toni: Lógica interna de los bucles.
* Sara: Creación de las funciones y variables, introducción de textos e instrucciones, corrección de posibles fallos al insertar inputs erróneos, organización de archivos y redacción de README.
* En todas las tareas relacionadas con el proyecto la aportación ha sido conjunta en mayor o menor parte. 

## Archivos adjuntos:
* scr: aquí se encuentran todos los scripts creados, tanto correctos como erróneos, utilizados a lo largo del derarrollo del proyecto.
* notebooks: aquí se encuentran todos los notebooks creados, tanto correctos como erróneos, utilizados a lo largo del derarrollo del proyecto. Hemos trabajdo también notebooks debido a problemas con los scripts en el ordenador de Toni.
---

### Autores:
Toni Suau Maget - <tonisuau30@gmail.com>

Sara Galán Enríquez - <saragalanenriquez@gmail.com>
