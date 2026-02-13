# Asteroids LYMCE
## Introducción y Definición del Proyecto
El presente proyecto consiste en el desarrollo de un videojuego de disparos espacial basado en el clásico Asteroids, pero rediseñado con nuevos elementos y lógica de eventos en tiempo real.
A diferencia de la versión original, esta implementación introduce mecánicas de progresión de dificultad, un sistema de gestión de estados complejo y una narrativa de "urgencia global". El objetivo principal es sobrevivir a 10 niveles de densidad creciente de asteroides, culminando en un enfrentamiento contra una entidad de gran escala (Boss Arepa) y evitando una colisión planetaria catastrófica activada por la inactividad del jugador.
## Arquitectura del Sistema
El software se ha estructurado de forma modular para garantizar la escalabilidad y facilitar la depuración. La organización se divide en los siguientes pilares:
### Núcleo y Control de Flujo (core)
El archivo engine con la clase GameEngine actúa como el "cerebro" del programa. Se encarga del ciclo de vida del juego, gestionando la actualización de físicas y el renderizado de gráficos a través de la librería Pygame. Implementa una máquina de estados que permite transicionar de forma limpia entre el menú de inicio, la partida activa, las pantallas de información y los estados de fin de juego (Victoria/Derrota).
Aparte de eso se le agrega el hecho que aca se encuentran algunas funciones implementadas como lo son un teletransporte para el jugador, un sistema de subida de nivel y los agragados del Easter Egg
### Entidades y Herencia (entities)
Para optimizar el código, se utilizó una clase abstracta base denominada ElementEntity.
•	Importancia: Define un contrato obligatorio donde cada objeto en pantalla debe tener una posición, una velocidad y métodos de actualización (update) y dibujo (draw).
•	Especialización: De esta clase derivan el Player (jugador), los Asteroid (enemigos) y las Bullet (proyectiles), permitiendo un manejo uniforme de la física vectorial.
### Gestión de Recursos (managers)
Se implementaron dos gestores especializados para optimizar el uso de memoria RAM:
•	ImageManager: Utiliza un diccionario interno para almacenar imágenes ya cargadas. Si el motor solicita una imagen que ya se usó, el mánager entrega la copia en memoria en lugar de leer el disco duro nuevamente.
•	SoundManager: Diferencia entre efectos de sonido (disparos, explosiones) y pistas musicales de larga duración, permitiendo un ambiente sonoro dinámico sin comprometer el rendimiento.
## Mecánicas Avanzadas e Innovaciones
### Progresión de Niveles y Dificultad Dinámica
El juego presenta 10 niveles de dificultad. La clase Asteroid calcula su velocidad final basándose en el nivel actual del jugador y su propio tamaño. A menor tamaño del asteroide, mayor es su velocidad vectorial, simulando una mayor inercia y dificultad de impacto.
Al alcanzar el Nivel 10, el sistema limpia la pantalla para generar al "Boss", un asteroide de gran escala con una rutina de dibujado propia y una barra de vida independiente de 100 puntos.
### El Easter Egg: Evento de Colisión Global
Una de las funcionalidades más distintivas es el EasterEggHandler. Si el sistema detecta que el jugador permanece inactivo por más de 10 segundos, el estado del juego cambia radicalmente.
•	Lógica: Se activa una animación donde la Tierra aparece en el horizonte inferior. Los asteroides pierden su trayectoria aleatoria y son forzados a una velocidad vertical constante hacia el planeta. Si el jugador no reacciona, se dispara un mensaje de "Colisión Global", terminando la partida.
### Sistema de Cheats y Buffer de Entrada
El CheatManager implementa un buffer de memoria que registra las últimas teclas pulsadas. Si la secuencia coincide con el código secreto ("lymce"), el motor teletransporta al jugador directamente al nivel final. Esto se logró mediante un filtrado de eventos de teclado que no interfiere con el movimiento normal de la nave.
## Funcionalidad de los Componentes de Interfaz (elements)
El juego se apoya en vistas secundarias para mejorar la experiencia del usuario:
•	InstructionsView: Expone los controles básicos y revela mecánicas avanzadas, como el teletransporte (L-SHIFT), el cual solo está disponible tras superar el nivel 5, incentivando la progresión.
•	CreditsView: Atribuye la autoría del proyecto y define el contexto del motor gráfico utilizado.
## Conclusión

En conclusión, la implementación del juego Asteroids LYMCE demuestra una sólida comprensión de los principios de ingeniería de software y diseño de sistemas interactivos. A través de este desarrollo, se ha logrado transformar un concepto arcade clásico en una plataforma de simulación compleja que integra mecánicas de progresión no lineales y una gestión de recursos altamente eficiente.
El proyecto destaca por su capacidad de equilibrar la fidelidad de las físicas vectoriales con innovaciones disruptivas, como el sistema de niveles escalables hasta el enfrentamiento con un jefe final de gran escala y la mecánica de colisión global ante la inactividad. Estas adiciones no solo elevan la dificultad técnica del software, sino que introducen una narrativa de urgencia que redefine la interacción del usuario con el entorno.
Tambien, debido a que se acaba lo que es el periodo de clases no se le pudo implementar lo que son sprites y imagenes a los elementos del juego como tal pero si se cumplio con la parte de lso easter eggs y los elementos de suma importancioa para la culminacion del juego de Asteroird LYMCE.

