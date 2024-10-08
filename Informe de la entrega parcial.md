<p align="center">
  <img src="https://github.com/JefHuiza/Fundamentos-de-Dise-o/assets/156036185/d3c66dfb-5faa-419b-bf1b-d897ea110ce7" width="70%">
</p>

# Informe de la entrega parcial: Juguemos con Pokemones 

 ### Intregantes del equipo:
 
 - Acevedo Valer Milagros Soledad
 - Bernal Belisario Brigitte
 - Condori Mamani Nardy Liz
 - Quispe Baldeon Melissa

# Introducción 
<p align="justify">
Realizar videojuegos con python es una experiencia accecible y flexible, debido a la simplicidad del lenguaje como también a la disponibilidad de bibliotecas que existen para desarrollarlo como PYGAME, que es una libreria que nos facilita la creación de gráficos, animaciones y la gestión de eventos con un usuario.
</p>  
<p align="justify">
Por todo lo explicado anteriormente nuestro proyecto consiste en el desarrollo de un videojuego interactivo utilizando el lenguaje de programación Python y la libreria Pygame para la creación de gráficos y manejo de eventos. Asímismo, el juego esta diseñado para ofrecer una experiencia dinámica e interactiva, combinando todos los elementos visuales posibles en tiempo real, juntamente con la interacción del usuario a través de controles personalizaos.
</p>
<p align="justify">
Un aspecto clave de este proyecto es la integración de una base de datos, lo que nos permite almacenar y  gestionar toda información relevante que se presenta durante la ejecución del juego, asimismo, identificar el progreso del jugador, tales como victorias, puntuaciones y todas las configuraciones personalizadas. Esta base de datos también nos facilita la posibilidad de llevar un registro de todos los usuarios, como logros y estadísticas que se realizan dentro del juego.
</p>
<p align="justify">
La arquitectura del juego se basa en la modularidad, lo que nos permite abarcar futuras expansiones y actualizaciones, tales como añadir nuevos niveles de juego, personajes de ser necesario, asimismo, incluir funcionalidades si se requieren. Este videojuego está diseñado para ser multiplataforma, aprovachando la portabilidad de Python y la escalabilidad de las bases de datos, los que nos permite que funcione en una variedad de dispositivos y entornos.
</p>

# Desarrollo 
<p align="justify">
Después de haber hecho un pequeño contexto de como nos ayuda python, además, de usar librerias como pygame pasamos a explicar en que consiste nuestro videojuego, el juego que hemos realizado tiene la temática de "Juguemos con Pokemones", donde el videojuego se centra en la selección de un Pokémon por parte del usuario, con un oponente que es elegido de manera aleatoria, ya que tiene una mecánica de batalla simplificada, donde se puede utilizar ataques y pociones, ahora explicamos la estructura del videojuego de la siguiente manera:
</p>
<p align="justify">
Tal como se habia meencionado con anterioridad la mecánica del juego se basa en una serie de turnos, donde el jugador puede elegir entre diferentes tipos de ataques y usar pocones para recuperar vida, ddo que el objetivo es reducir la vida del oponente a 0 antes de que el propio Pokémon sea derrotado.
</p>

## 1.- Selección del Pokémon 

### Elección del jugador:
<p align="justify">
Al incio de la partida, el jgador tendrá la opción de seleccionar su Pokémon de una lista predefinida que incluye diferentes especies con variados tipos de ataques, donde cada Pokémon tiene su propia cantidad de vida de acuerdo al tipo que puede ser mas o menos que uno y otros
</p>

### Oponente Aleatorio:
<p align="justify">
Una vez de haber seleccionado nuestro Pokémon, el juego automáticamente elige un oponente al azar de una base de datos de Pokémon, asegurando que cada partida sea única, asimismo, el oponente tiene sus propios puntos de vida y ataques.
</p>

<div align="center">

| Pokémon elegir | Oponente|
|----------------|----------|
|<img src="https://github.com/user-attachments/assets/7d1f97b7-a501-4d27-8245-022b5840c3a4" alt="ESP32 DEVKIT V1" width="300"/> | <img src="https://github.com/user-attachments/assets/ee35b4d9-4ba2-4d3e-a111-05ecb3283e51" alt="ESP32 DEVKIT V1" width="300"/>|

</div>

## 2.- Mecánica de Batalla

### Turnos:
<p align="justify">
La partida se desarrolla en turnos alternos, donde el jugador primero elige su acción (ataque o uso de poción) seguido por el ataque del oponente.
</p>

### Tipos de Ataque:
<p align="justify">
Cada Pokémon tiene varias opciones de ataque, donde cada una cuenta con diferentes potencias y tipos (físicos y especiales), asismismo, algunos ataques pueden causar más daño dependiendo del tipo e Pokémon o pueden tener efectos especiales como paralizar al oponente o viciversa.
</p>

### Uso de Pociones:
<p align="justify">
El jugador tiene 3 pociones disponibles que pueden usarse para recuperar una cantidad fija de vida, por ende, usar una poción es una acción que se realiza ando esta en su turno, por lo que el jugador debe decidir cuándo es más estratégico utilizarlo.
</p>

<div align="center">
  
| Turnos            | Ataques       |    Posion        |
|---------------|-------------|-----------|
|  ![image](https://github.com/user-attachments/assets/5d8cabe5-be01-430b-8468-86e9a87348e2) |   ![image](https://github.com/user-attachments/assets/b6c777d3-0046-431a-9333-da310c666126) |   ![image](https://github.com/user-attachments/assets/e3cf5577-8193-4ad2-b36a-89e8a68f33a7) |

</div>

## 3.- Sistema de Puntos de Vida (HP)

### Salud Inicial:
<p align="justify">
Tanto el Pokémon del jugador como del oponente comienzan con un número determinado de puntos de vida (PH), donde la partida termina cuando uno de los Pokemones llega a cero puntos de vida.
</p>

### Reducción de PH:
<p align="justify">
Cuando el Pokémon es atacado, su PH se reduce según la potencia del ataque, donde si el ataque es efectivo (por ejemplo, si el tipo del ataque tiene ventaja sobre el otro tipo del Pokémon), el daño resulta ser mayor favoreciendo al oponente o al usuario mismo.
</p>

<div align="center"> 
  
| Vida inicial| Reducción de PH | 
|-----------------|--------------|
|<img src="https://github.com/user-attachments/assets/66b4ca59-803e-4348-9b81-1f2cbf26b8ff" alt="ESP32 DEVKIT V1" width="300"/>|<img src="https://github.com/user-attachments/assets/b19e14b6-788b-431d-b6cb-b5bb3de68732" alt="ESP32 DEVKIT V1" width="300"/>|

</div>

## 4.- Fin de la partida

### Condiciones de ganar o perder:
<p align="justify">
La partida culmina cuando uno de los dos pokemones pierde todos sus puntos de vida, donde si el Pokémon del jugador derrota al oponente, esté se declara ganador; de lo contrario, si el Pokémon del jugador se queda sin vida, el jugador pierdey termina la partida.
</p>

<div align="center">
  
| Ganar o perder|
|----------------|
| <img src="https://github.com/user-attachments/assets/1944b28c-d356-4472-bb9c-db3a2e7e7f97" alt="ESP32 DEVKIT V1" width="300"/>|

</div>

### Resultados y estadística:
<p align="justify">
Al finalizar la batalla, se puede mostrar una pantalla, donde al jugador se le declara como ganador o perdedor, para luego preguntar si quiere volver a iniciar la partida o no, asimismo, las estadísticas como los ataques realizados por los competidore y este se guardará en el historial de partida en la base de datos creada.
</p>

<div align="center">
  
|Una vez haber finalizado la partida|
|-----------------------------------|
|<img src="https://github.com/user-attachments/assets/c0029601-22aa-41be-a6b8-d01dc3197ef2" alt="ESP32 DEVKIT V1" width="300"/>|

</div>

## 5.- Elementos visuales y sonoros

### Interfaz simple:
<p align="justify">
La interfaz del juego muestra la selección del Pokémon, los PH actuales de ambos Pokémon, las opciones de ataque y el estado de las pociones restantes, además, utiliza imágenes coloridas para representar tanto a los Pokémon, como el fondo donde se da la batalla hasta que esta termine.
</p>

<div align="center">
  
| Fondo de la interfaz | Fondo de la barra de vida del HP|
|---------------------|----------------------------------|
|<img src="https://github.com/user-attachments/assets/20bc9af7-26c2-4355-8e20-b4298f612fd8" alt="ESP32 DEVKIT V1" width="300"/>|<img src="https://github.com/user-attachments/assets/13b7b1ce-2f49-484f-a26d-e50ccfd282ce" alt="ESP32 DEVKIT V1" width="300"/>|

</div>

### Efecto de sonido:
<p align="justify">
Para iniciar la partida se le coloca un sonido para que el juego resulte ser atrativo durante toda la partida, para asi mejorar la experiencia del jugador.
</p>

https://github.com/user-attachments/assets/42dcc2c9-5fcf-4811-afdb-a6d9f75639bd

[Código del videojuego en Python](https://github.com/Fx2048/TEAM_DB/blob/82ecffe17f555a120992f4a40a9e398c76627ee4/juegopoke.py)

## Avance

<p align="justify">
Como se puede evidenciar todo el avance que se logro hasta este momento es la creación de la interfaz de la segunda ventana, que nos muestra el juego en sí, pero eso no indica que este completamente terminado, dado que la interfaz de los botones se encuentran en la misma ventana, lo cual necesita corregir y esta en proceso continuo de actualización, asimismo, una de las partes que se logro avanzar fue relacionado con las tablas correspondientes a la base de datos de acuerdo al videojuego, ya que es ahi donde se tiene informacion sobre las llaves primarias y foráneas dentro del juego que se muestra a continuación:
</p>

<div align="center">
  
|Diagrama de la base de datos de JUEGOPOKE| Tablas de la base de datos|
|-----------------------------------------|--------------------------------|
|![diagrama](https://github.com/user-attachments/assets/5cf0c931-225c-4920-b902-70e01597d33e)|  ![Imagen de WhatsApp 2024-09-29 a las 22 14 37_1f5e7f98](https://github.com/user-attachments/assets/9d5ac1f1-fbe2-4db1-af0f-a70c52ba8939)|

</div>

<p align="justify">
Este diagrama muestra la base de datos que mantiene información sobre las habilidades de los Pokémon y sus traducciones en diferentes idiomas si es necesario. La tabla "habilidades" almacena todas las habilidades, junto con su nombre, generación y si pertenece a la serie principal. Los nombres de las habilidades se guardan en el archivo "habilidad_nombres", mientras que los efectos detallados se guardan en el archivo "habilidad_efectos". Los cambios en los efectos se registran en la sección "capacidad_efecto_cambios", que están conectados a los grupos de versiones de "version_groups". En "flavor_text_entries" se almacenan descripciones adicionales, así como versiones durante el juego solo si es necesario. Cada Pokémon tiene información básica guardada en la tabla "pokemon", mientras que "pokemon_abilities" asocia a los Pokémon con sus habilidades, indicando si hay una habilidad oculta. Además, se agregó un historial para guardar los resultados después de haber realizado una partida, donde se guardará información sobre los resultados finales como victoria o derrota, incluyedo información necesaria y relevante de acuerdo a la partida, tales como la fecha y hora donde se dio o inicio el juego. Finalmente, la tabla "users gestiona los datos de los usuarios del sistema, que pasa a estar relacionada con el diagrama multijugador. Esta estructura nos permite una gestión multigeneracional de las habilidades y sus efectos en los Pokémon.
</p>

[Código para la creación de tablas en SQL](https://github.com/Fx2048/TEAM_DB/blob/82ecffe17f555a120992f4a40a9e398c76627ee4/bdpokemon.sql)


<div align="center">
  
|Diagrama para el usuario multijugador|
|------------------------|
|<img src="https://github.com/user-attachments/assets/4ca4c15f-e838-4f03-bec0-e4446d94c3b8" alt="ESP32 DEVKIT V1" width="800"/>|


</div>

<p align="justify">
Este diagrama muestra la estructura de la base de datos diseñado para gestionar partidas que se den de manera multijugador, donde cada tabla tiene una función específica para cumplir ese rol. La tabla GAMES gestiona toda la información sobre las partidas que se vayan a dar, incluyendo el estado del juego, el turno actual y la fecha de inicio, mientras que USERS guarda los datos de los jugadores, como el nombre de usuario, correo electrónico y contraseña, asimismo, GAME_PLAYERS pasa a ser una tabla intermedia que conecta a los jugadores con los juegos, permitiendo saber qué jugadores están participando y en qué partida, además de almacenar el estado del jugador en la partida (como "activo" o "eliminado"). La tabla ACTION registra las acciones que los jugadores realizan durante el juego, como moverse o atacar, junto con la marca de tiempo que indica cuándo ocurrieron. Finalmente, VOTES gestiona los votos que los jugadores emiten durante una partida, guardando la decisión de cada jugador (como "sí" o "no") y el momento en que se emitió el voto. Las relaciones entre estas tablas permiten un control detallado sobre los juegos, los jugadores, las acciones realizadas y las decisiones tomadas, asegurando una correcta gestión de las partidas multijugador.
</p>

[Código para las votaciones en SQL ](https://github.com/Fx2048/TEAM_DB/blob/c8feb8190338e940808b809816576fb311c1d6ae/bd_votaciones.sql)

## Dificultades

### Perdida de datos en la base de datos:
<p align="justify">
Una de las primeras dificultades que hemos presentado es acerca del tiempo que la base de datos se encuentra, dado que siempre después de 48 horas se elimina automáticamente y tenemos que volver a crear uno nuevo, y nuevamente generar las tablas correspondientes a la base de datos, por ello, cabe mencionar que en el diagrama mostrado en este informe no se evidencia la tabla correspondiente al historial para las partidas y eso se debe a que en la base de datos donde se creó este se eliminó, y al no tomar las medidas pertinentes como guardar los datos se perdió, pero obviamente, eso no es excusa alguna para no tratar de solucionar ése problema y vamos en busca de ello. Adicional a ello hemos presentado dificultades en poder conectar el juego realizado en python con la base de datos, más que todo por el codigo del videojuego que no lo tenemos al 100%.
</p>

<div align="center">
  
|Mensaje después de 48 horas|
|---------------------------|
|<img src="https://github.com/user-attachments/assets/e3261bbf-964f-47a5-bb2c-35b642368534" alt="ESP32 DEVKIT V1" width="500"/>|
|<img src="https://github.com/user-attachments/assets/15e018f7-b96b-401f-942f-03d4a63cc246" alt="ESP32 DEVKIT V1" width="500"/>|

</div>
<p align="justify">
Para solucionar esta dificultad no hemos encontrado algo que nos ayude a mantener los datos, dado que el problema surge por condiciones que nos ofrece el plan gratuito de railway, lo cual una de las cosas que estariamos por emplear es la opción de migrar a un nuevo plan de pago, dado que eso seria más estable si queremos que nuestra base de datos esté siempre activa o otro caso seria monitorear y reiniciar automáticamente la base de datos, donde detecte si la base de datos está inactiva o cerrada, y que la reinicie automáticamente, lo cual no seria tan factible por el hecho de que requeriría de un script en un servidor que monitoree la conexión a la base de datos cada cierto tiempo, y ver si asi no podemos perder todos los datos que se pueden llegar a recolectar. 
</p>

### Problemas en diseñar a primera ventana:
<p align="justify">
Otras de las dificultades que hemos presentado en la elaboración de nuestro videojuego es la creación de la primera ventana, que contiene los botones personalizados y la información correspondiente a las votaciones realizadas por el usuario, ya que como se puede visualizar no lo reconoce y presenta un error en ambas ventanas, donde todo está completamente en rojo, y casi parecido con la segunda ventana, a pesar de haber incluido diferentes formas de código, siempre tenemos el problema de que no se puede tener ambas ventanas de manera simultanea, donde vamos viendo como resolverlo, aunque hemos tenido un pequeño avance, que aún presenta problemas, en reconocer los botones y actuar con ellos, durante la partida.
</p>

<div align="center">
  
|Problems en crear la ventana 1| Avance|
|------------------------------|---------|
|<img src="https://github.com/user-attachments/assets/7014ac29-3b73-4863-b164-b2a00bdc8ba2" alt="ESP32 DEVKIT V1" width="500"/>| <img src="https://github.com/user-attachments/assets/778a842a-fe43-49ca-9908-133090299bbc" alt="ESP32 DEVKIT V1" width="500"/>  |

</div>

<p align="justify">
Para poder solucionar el problema en la creación de la ventana 1, se trato de utilizar un programa para ejecutar varias ventanas desde el mismo procesador usando un "Multiprocesamiento Intermediate Showcase", donde habia un script que nos permitiría mostrar varias ventanas simultáneamente con una sincronización adecuada utilizando multiprocesamiento, juntamente con pygame, pero el problema surgio al momento de la implementación del código, de por si producía ambas ventanas al mismo tiempo, pero este no reconocia las imagenes que se les colocaba, asi que básicamente lo único que mostraba era un fondo negro, ya que lo primero que se buscaba era estar seguros de que normal pudiera reconocer las imágenes y de ahí poder emplearlo con el videojuego, pero a pesar de ello no hubo avance alguno, y aún asi estamos en la busqueda de nuevas soluciones que nos ayuden para poder conectar ambas ventanas, o en todo caso perfeccionar el script con el multiprocesamiento.
</p>

```
import os
import sys
from multiprocessing import Lock, Pipe, Process
from multiprocessing.connection import Connection
from random import randint

import pygame

pygame.init()
```
# Conclusión
<p align="justify">
Podemos concluir que nos encontramos muy lejos de decir que ya hemos culminado el trabajo, ya que presentamos problemas donde deberían ser menos, y para ello necesitamos encontrar más soluciones de lo que hemos utilizado hasta el momento y asi poder agregar todo lo que nos hace falta para culminar el trabajo, y presentarlo de la mejor manera posible, pero de eso se trata conocer lo que es la prueba y el error, ya que de acuerdo a ello iremos mejorando en próximas instancias y saber como actuar en este tipo de situaciones, ya que mientras no tengamos realizado la ventana 1 no podremos pasar al tema de votaciones por parte del usuarios y poder continuar con el juego, asimismo, poder conectarlo con la base de datos para que haga la recolección de acuerdo a las partidas.
</p>
