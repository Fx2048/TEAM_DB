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

Después de haber hecho un pequeño contexto de como nos ayuda python, además, de usar librerias como pygame pasamos a explicar en que consiste nuestro videojuego, el juego que hemos realizado tiene la temática de "Juguemos con Pokemones", donde el videojuego se centra en la selección de un Pokémon por parte del usuario, con un oponente que es elegido de manera aleatoria, ya que tiene una mecánica de batalla simplificada, donde se puede utilizar ataques y pociones, ahora explicamos la estructura del videojuego de la siguiente manera:

Tal como se habia meencionado con anterioridad la mecánica del juego se basa en una serie de turnos, donde el jugador puede elegir entre diferentes tipos de ataques y usar pocones para recuperar vida, ddo que el objetivo es reducir la vida del oponente a 0 antes de que el propio Pokémon sea derrotado.

## 1.- Selección del Pokémon 

### Elección del jugador:

Al incio de la partida, el jgador tendrá la opción de seleccionar su Pokémon de una lista predefinida que incluye diferentes especies con variados tipos de ataques, donde cada Pokémon tiene su propia cantidad de vida de acuerdo al tipo que puede ser mas o menos que uno y otros

### Oponente Aleatorio:

Una vez de haber seleccionado nuestro Pokémon, el juego automáticamente elige un oponente al azar de una base de datos de Pokémon, asegurando que cada partida sea única, asimismo, el oponente tiene sus propios puntos de vida y ataques.

## 2.- Mecánica de Batalla

### Turnos:

La partida se desarrolla en turnos alternos, donde el jugador primero elige su acción (ataque o uso de posición) seguido por el ataque del oponente.

### Tipos de Ataque:

Cada Pokémon tiene varias opciones de ataque, donde cada una cuenta con diferentes potencias y tipos (físicos y especiales), asismismo, algunos ataques pueden causar más daño dependiendo del tipo e Pokémon o pueden tener efectos especiales como paralizar al oponente o viciversa.

### Uso de Pociones:

El jugador tiene 3 pociones disponibles que pueden usarse para recuperar una cantidad fija de vida, por ende, usar una poción es una acción que se realiza ando esta en su turno, por lo que el jugador debe decidir cuándo es más estratégico utilizarlo.

## 3.- Sistema de Puntos de Vida (PV)

### Salud Inicial:

Tanto el Pokémon del jugador como del oponente comienzan con un número determinado de puntos de vida (PV), donde la partida termina cuando uno de los Pokemones llega a cero puntos de vida.

### Reducción de PV:

Cuando el Pokémon es atacado, su PV se reduce según la potencia del ataque, 


que se ha avanzado
en que tuvo dificultades

que hizo para solucionarlo
