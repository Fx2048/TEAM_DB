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

![image](https://github.com/user-attachments/assets/7d1f97b7-a501-4d27-8245-022b5840c3a4)
![image](https://github.com/user-attachments/assets/ee35b4d9-4ba2-4d3e-a111-05ecb3283e51)


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

![image](https://github.com/user-attachments/assets/5d8cabe5-be01-430b-8468-86e9a87348e2)
![image](https://github.com/user-attachments/assets/b6c777d3-0046-431a-9333-da310c666126)
![image](https://github.com/user-attachments/assets/e3cf5577-8193-4ad2-b36a-89e8a68f33a7)

## 3.- Sistema de Puntos de Vida (HP)

### Salud Inicial:
<p align="justify">
Tanto el Pokémon del jugador como del oponente comienzan con un número determinado de puntos de vida (PH), donde la partida termina cuando uno de los Pokemones llega a cero puntos de vida.
</p>

### Reducción de PH:
<p align="justify">
Cuando el Pokémon es atacado, su PH se reduce según la potencia del ataque, donde si el ataque es efectivo (por ejemplo, si el tipo del ataque tiene ventaja sobre el otro tipo del Pokémon), el daño resulta ser mayor favoreciendo al oponente o al usuario mismo.
</p>

![image](https://github.com/user-attachments/assets/b19e14b6-788b-431d-b6cb-b5bb3de68732)
![image](https://github.com/user-attachments/assets/1944b28c-d356-4472-bb9c-db3a2e7e7f97)

## 4.- Fin de la partida

### Condiciones de ganar o perder:
<p align="justify">
La partida culmina cuando uno de los dos pokemones pierde todos sus puntos de vida, donde si el Pokémon del jugador derrota al oponente, esté se declara ganador; de lo contrario, si el Pokémon del jugador se queda sin vida, el jugador pierdey termina la partida.
</p>

### Resultados y estadística:
<p align="justify">
Al finalizar la batalla, se puede mostrar una pantalla, donde al jugador se le declara como ganador o perdedor, para luego preguntar si quiere volver a iniciar la partida o no, asimismo, las estadísticas como los ataques realizados por los competidore y este se guardará en el historial de partida en la base de datos creada.
</p>

![image](https://github.com/user-attachments/assets/c0029601-22aa-41be-a6b8-d01dc3197ef2)


## 5.- Elementos visuales y sonoros

### Interfaz simple:
<p align="justify">
La interfaz del juego muestra la selección del Pokémon, los PH actuales de ambos Pokémon, las opciones de ataque y el estado de las pociones restantes, además, utiliza imágenes coloridas para representar tanto a los Pokémon, como el fondo donde se da la batalla hasta que esta termine.
</p>

![image](https://github.com/user-attachments/assets/20bc9af7-26c2-4355-8e20-b4298f612fd8)
![image](https://github.com/user-attachments/assets/13b7b1ce-2f49-484f-a26d-e50ccfd282ce)

### Efecto de sonido:
<p align="justify">
Para iniciar la partida se le coloca un sonido para que el juego resulte ser atrativo durante toda la partida, para asi mejorar la experiencia del jugador.
</p>

https://github.com/user-attachments/assets/42dcc2c9-5fcf-4811-afdb-a6d9f75639bd

que se ha avanzado
en que tuvo dificultades

que hizo para solucionarlo
