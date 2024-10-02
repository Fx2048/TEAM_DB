-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: autorack.proxy.rlwy.net    Database: BD_proyect
-- ------------------------------------------------------
-- Server version	9.0.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Opciones`
--

DROP TABLE IF EXISTS `Opciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Opciones` (
  `id` int NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Resultados`
--

DROP TABLE IF EXISTS `Resultados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Resultados` (
  `id` int NOT NULL AUTO_INCREMENT,
  `opcion_id` int DEFAULT NULL,
  `cantidad` int DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `opcion_id` (`opcion_id`),
  CONSTRAINT `Resultados_ibfk_1` FOREIGN KEY (`opcion_id`) REFERENCES `Opciones` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Votos`
--

DROP TABLE IF EXISTS `Votos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Votos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `opcion_id` int DEFAULT NULL,
  `timestamp` datetime DEFAULT CURRENT_TIMESTAMP,
  `leido` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `opcion_id` (`opcion_id`),
  CONSTRAINT `Votos_ibfk_1` FOREIGN KEY (`opcion_id`) REFERENCES `Opciones` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `abilities`
--

DROP TABLE IF EXISTS `abilities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `abilities` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `is_main_series` tinyint NOT NULL,
  `generation_id` int NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_ability_id` (`id`),
  KEY `generation_id` (`generation_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `generation_id` FOREIGN KEY (`generation_id`) REFERENCES `generations` (`id`),
  CONSTRAINT `user_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ability_effect_changes`
--

DROP TABLE IF EXISTS `ability_effect_changes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ability_effect_changes` (
  `ability_id` int NOT NULL,
  `version_group_id` int NOT NULL,
  `affect` text NOT NULL,
  `language_id` int NOT NULL,
  PRIMARY KEY (`ability_id`,`version_group_id`,`language_id`),
  KEY `version_group_id_idx` (`version_group_id`),
  KEY `language_id_idx` (`language_id`),
  CONSTRAINT `ability_id` FOREIGN KEY (`ability_id`) REFERENCES `abilities` (`id`),
  CONSTRAINT `language_id` FOREIGN KEY (`language_id`) REFERENCES `languages` (`id`),
  CONSTRAINT `version_group_id` FOREIGN KEY (`version_group_id`) REFERENCES `version_groups` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ability_effects`
--

DROP TABLE IF EXISTS `ability_effects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ability_effects` (
  `ability_id` int NOT NULL,
  `language_id` int NOT NULL,
  `affect` text NOT NULL,
  `short_effect` varchar(45) DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`ability_id`,`language_id`,`user_id`),
  KEY `language_id_idx` (`language_id`),
  KEY `user_id_idx` (`user_id`),
  CONSTRAINT `fk_ability_effects_ability_id` FOREIGN KEY (`ability_id`) REFERENCES `abilities` (`id`),
  CONSTRAINT `fk_ability_effects_language_id` FOREIGN KEY (`language_id`) REFERENCES `languages` (`id`),
  CONSTRAINT `fk_ability_effects_user_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ability_names`
--

DROP TABLE IF EXISTS `ability_names`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ability_names` (
  `ability_id` int NOT NULL,
  `language_id` int NOT NULL,
  `name` varchar(50) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`ability_id`,`language_id`,`user_id`),
  KEY `language_id_idx` (`language_id`),
  KEY `user_id_idx` (`user_id`),
  CONSTRAINT `fk_ability_names_ability_id` FOREIGN KEY (`ability_id`) REFERENCES `abilities` (`id`),
  CONSTRAINT `fk_ability_names_language_id` FOREIGN KEY (`language_id`) REFERENCES `languages` (`id`),
  CONSTRAINT `fk_ability_names_user_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `flavor_text_entries`
--

DROP TABLE IF EXISTS `flavor_text_entries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flavor_text_entries` (
  `ability_id` int NOT NULL,
  `version_group_id` int NOT NULL,
  `language_id` int NOT NULL,
  `flavor_text` text NOT NULL,
  PRIMARY KEY (`ability_id`,`version_group_id`,`language_id`),
  KEY `version_group_id_idx` (`version_group_id`),
  KEY `language_id_idx` (`language_id`),
  CONSTRAINT `fk_flavor_text_entries_ability_id` FOREIGN KEY (`ability_id`) REFERENCES `abilities` (`id`),
  CONSTRAINT `fk_flavor_text_entries_language_id` FOREIGN KEY (`language_id`) REFERENCES `languages` (`id`),
  CONSTRAINT `fk_flavor_text_entries_version_group_id` FOREIGN KEY (`version_group_id`) REFERENCES `version_groups` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `generations`
--

DROP TABLE IF EXISTS `generations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `generations` (
  `id` int NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `historial_partidas`
--

DROP TABLE IF EXISTS `historial_partidas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `historial_partidas` (
  `partida_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `pokemon_jugador_id` int DEFAULT NULL,
  `pokemon_oponente_id` int DEFAULT NULL,
  `resultado` varchar(10) DEFAULT NULL,
  `fecha_partida` datetime DEFAULT NULL,
  PRIMARY KEY (`partida_id`),
  KEY `user_id` (`user_id`),
  KEY `pokemon_jugador_id` (`pokemon_jugador_id`),
  KEY `pokemon_oponente_id` (`pokemon_oponente_id`),
  CONSTRAINT `historial_partidas_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `historial_partidas_ibfk_2` FOREIGN KEY (`pokemon_jugador_id`) REFERENCES `pokemon` (`id`),
  CONSTRAINT `historial_partidas_ibfk_3` FOREIGN KEY (`pokemon_oponente_id`) REFERENCES `pokemon` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `languages`
--

DROP TABLE IF EXISTS `languages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `languages` (
  `id` int NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `movimientos`
--

DROP TABLE IF EXISTS `movimientos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movimientos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `poder` int NOT NULL,
  `tipo` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `pokemon`
--

DROP TABLE IF EXISTS `pokemon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pokemon` (
  `id` int NOT NULL,
  `name` varchar(50) NOT NULL,
  `nivel` int NOT NULL,
  `hp_actual` int NOT NULL,
  `hp_maximo` int NOT NULL,
  `ataque` int NOT NULL,
  `defensa` int NOT NULL,
  `velocidad` int NOT NULL,
  `tipos` varchar(255) NOT NULL,
  `imagen` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `pokemon_abilities`
--

DROP TABLE IF EXISTS `pokemon_abilities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pokemon_abilities` (
  `pokemon_id` int NOT NULL,
  `ability_id` int NOT NULL,
  `is_hidden` tinyint NOT NULL,
  `slot` int NOT NULL,
  PRIMARY KEY (`pokemon_id`,`ability_id`),
  KEY `ability_id_idx` (`ability_id`),
  CONSTRAINT `fk_pokemon_abilities_ability_id` FOREIGN KEY (`ability_id`) REFERENCES `abilities` (`id`),
  CONSTRAINT `fk_pokemon_abilities_pokemon_id` FOREIGN KEY (`pokemon_id`) REFERENCES `pokemon` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `pokemon_movimientos`
--

DROP TABLE IF EXISTS `pokemon_movimientos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pokemon_movimientos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `pokemon_id` int NOT NULL,
  `movimiento_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `pokemon_id` (`pokemon_id`),
  KEY `movimiento_id` (`movimiento_id`),
  CONSTRAINT `pokemon_movimientos_ibfk_1` FOREIGN KEY (`pokemon_id`) REFERENCES `pokemon` (`id`) ON DELETE CASCADE,
  CONSTRAINT `pokemon_movimientos_ibfk_2` FOREIGN KEY (`movimiento_id`) REFERENCES `movimientos` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL,
  `username` varchar(45) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `version_groups`
--

DROP TABLE IF EXISTS `version_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `version_groups` (
  `id` int NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-01  0:42:47
