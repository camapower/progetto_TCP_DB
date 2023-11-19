-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Nov 20, 2023 alle 00:02
-- Versione del server: 10.4.28-MariaDB
-- Versione PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `5b_tpsit`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `dipendenti_andrea_camassa`
--

CREATE TABLE `dipendenti_andrea_camassa` (
  `id` int(11) NOT NULL,
  `nome` varchar(45) DEFAULT NULL,
  `cognome` varchar(45) DEFAULT NULL,
  `eta` int(11) NOT NULL,
  `pos_lavorativa` varchar(45) DEFAULT NULL,
  `data_ass` date NOT NULL,
  `residenza` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `dipendenti_andrea_camassa`
--

INSERT INTO `dipendenti_andrea_camassa` (`id`, `nome`, `cognome`, `eta`, `pos_lavorativa`, `data_ass`, `residenza`) VALUES
(1, 'Federico', 'Marini', 29, 'Web Developer', '2023-04-09', 'Lucca'),
(2, 'Ludovica', 'Rinaldi', 35, 'Infermiera', '2023-06-15', 'Pescara'),
(3, 'Gianluca', 'Villa', 41, 'Ingegnere del Software', '2023-01-28', 'Vicenza'),
(4, 'Marta', 'Marchi', 27, 'Grafico', '2023-08-11', 'Aosta'),
(5, 'Niccolò', 'Rizzi', 31, 'Commercialista', '2023-03-20', 'Nuoro'),
(6, 'Mario', 'Rossi', 35, 'Programmatore', '2022-01-15', 'Roma'),
(7, 'Paola', 'Bianchi', 28, 'Progettista Grafico', '2021-03-20', 'Milano'),
(8, 'Luca', 'Verdi', 42, 'Manager delle Vendite', '2020-05-10', 'Napoli'),
(9, 'Laura', 'Russo', 29, 'Infermiera', '2023-02-05', 'Torino'),
(10, 'Giovanni', 'Ferrari', 38, 'Ingegnere del Software', '2021-07-12', 'Firenze'),
(11, 'Chiara', 'Gallo', 31, 'Architetto', '2021-08-28', 'Palermo'),
(12, 'Andrea', 'Conti', 45, 'Avvocato', '2019-12-02', 'Bologna'),
(13, 'Sara', 'Marino', 26, 'Assistente Amministrativo', '2023-09-15', 'Genova'),
(14, 'Marco', 'Greco', 34, 'Medico', '2022-04-18', 'Bari'),
(15, 'Francesca', 'Esposito', 30, 'Insegnante', '2021-06-03', 'Catania'),
(16, 'Lorenzo', 'Galli', 37, 'Ingegnere Elettrico', '2020-09-22', 'Venezia'),
(17, 'Valentina', 'Mancini', 27, 'Analista dei Dati', '2023-01-08', 'Verona'),
(18, 'Antonio', 'Martini', 41, 'Direttore Marketing', '2020-03-14', 'Trieste'),
(19, 'Elena', 'Barbieri', 33, 'Psicologo', '2022-11-30', 'Perugia'),
(20, 'Davide', 'Santoro', 29, 'Ristoratore', '2021-10-05', 'Cagliari'),
(21, 'Roberta', 'Pellegrini', 39, 'Insegnante', '2020-08-19', 'Messina'),
(22, 'Fabio', 'Orlando', 34, 'Ingegnere Meccanico', '2022-07-07', 'Ancona'),
(23, 'Silvia', 'Bertoli', 28, 'Web Developer', '2021-05-12', 'Lecce'),
(24, 'Simone', 'Moretti', 43, 'Farmacista', '2019-04-01', 'Reggio Calabria'),
(25, 'Cristina', 'Vitale', 32, 'Analista Finanziario', '2023-05-25', 'Potenza'),
(26, 'Alberto', 'Caruso', 36, 'Architetto', '2021-09-28', 'Aosta'),
(27, 'Elisa', 'Riva', 30, 'Project Manager', '2021-04-03', 'Trento'),
(28, 'Riccardo', 'Lombardi', 40, 'Avvocato', '2020-02-12', 'Udine'),
(29, 'Greta', 'Marchetti', 29, 'Graphic Designer', '2022-06-15', 'Bolzano'),
(30, 'Matteo', 'Silvestri', 35, 'Medico', '2019-11-11', 'Cosenza'),
(31, 'Alessia', 'Fabbri', 31, 'Infermiera', '2023-07-17', 'La Spezia'),
(32, 'Leonardo', 'Costa', 46, 'Ingegnere delle Telecomunicazioni', '2020-10-09', 'Alessandria'),
(33, 'Chiara', 'Romano', 30, 'Copywriter', '2021-12-27', 'Ragusa'),
(34, 'Marco', 'Serra', 38, 'Manager delle Risorse Umane', '2020-07-21', 'Siracusa'),
(35, 'Elena', 'Galli', 33, 'Psicoterapeuta', '2022-08-04', 'Novara');

-- --------------------------------------------------------

--
-- Struttura della tabella `zone_di_lavoro_andrea_camassa`
--

CREATE TABLE `zone_di_lavoro_andrea_camassa` (
  `id_z` int(11) NOT NULL,
  `nome_z` varchar(45) DEFAULT NULL,
  `numero_clienti` varchar(45) DEFAULT NULL,
  `cod_nc` int(11) NOT NULL,
  `colore_z` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `zone_di_lavoro_andrea_camassa`
--

INSERT INTO `zone_di_lavoro_andrea_camassa` (`id_z`, `nome_z`, `numero_clienti`, `cod_nc`, `colore_z`) VALUES
(1, 'zona 1', '10', 6, 'verde'),
(2, 'zona 2', '6', 1, 'azzurro'),
(3, 'zona 3', '12', 25, 'tiffany'),
(4, 'zona 4', '9', 30, 'rosso'),
(5, 'zona 5', '15', 22, 'marrone');

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `dipendenti_andrea_camassa`
--
ALTER TABLE `dipendenti_andrea_camassa`
  ADD PRIMARY KEY (`id`);

--
-- Indici per le tabelle `zone_di_lavoro_andrea_camassa`
--
ALTER TABLE `zone_di_lavoro_andrea_camassa`
  ADD PRIMARY KEY (`id_z`),
  ADD KEY `vincolo1` (`cod_nc`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `dipendenti_andrea_camassa`
--
ALTER TABLE `dipendenti_andrea_camassa`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT per la tabella `zone_di_lavoro_andrea_camassa`
--
ALTER TABLE `zone_di_lavoro_andrea_camassa`
  MODIFY `id_z` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Limiti per le tabelle scaricate
--

--
-- Limiti per la tabella `zone_di_lavoro_andrea_camassa`
--
ALTER TABLE `zone_di_lavoro_andrea_camassa`
  ADD CONSTRAINT `vincolo1` FOREIGN KEY (`cod_nc`) REFERENCES `dipendenti_andrea_camassa` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
