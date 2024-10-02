-- Tabla para las opciones de votación
CREATE TABLE Opciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(255) NOT NULL
);

-- Tabla para los votos emitidos
CREATE TABLE Votos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    opcion_id INT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    leido BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (opcion_id) REFERENCES Opciones(id)
);

-- Tabla para almacenar el resultado de la votación
CREATE TABLE Resultados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    opcion_id INT,
    cantidad INT DEFAULT 0,
    FOREIGN KEY (opcion_id) REFERENCES Opciones(id)
);

ALTER TABLE pokemon
ADD COLUMN nivel INT NOT NULL,
ADD COLUMN hp_actual INT NOT NULL,
ADD COLUMN hp_maximo INT NOT NULL,
ADD COLUMN ataque INT NOT NULL,
ADD COLUMN defensa INT NOT NULL,
ADD COLUMN velocidad INT NOT NULL,
ADD COLUMN tipos VARCHAR(255) NOT NULL, -- Para una lista de tipos separada por comas
ADD COLUMN imagen VARCHAR(255) NOT NULL; -- URL o ruta a la imagen del sprite

-- Crear tabla movimientos
CREATE TABLE movimientos (
  id INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL,
  poder INT NOT NULL,
  tipo VARCHAR(50) NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Crear tabla pokemon_movimientos para la relación muchos a muchos
CREATE TABLE pokemon_movimientos (
  id INT NOT NULL AUTO_INCREMENT,
  pokemon_id INT NOT NULL,
  movimiento_id INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (pokemon_id) REFERENCES pokemon(id) ON DELETE CASCADE,
  FOREIGN KEY (movimiento_id) REFERENCES movimientos(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;