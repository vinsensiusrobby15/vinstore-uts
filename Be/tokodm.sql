-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 27 Okt 2023 pada 09.07
-- Versi server: 10.4.27-MariaDB
-- Versi PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tokodmmysql`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `tokodm`
--

CREATE TABLE `tokodm` (
  `no` int(20) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `price` int(25) NOT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
COMMIT;


INSERT INTO `tokodm` (`id`, `nama`, `price`) VALUES
(1, 1, 'Joki Rank Legend-Mythic', 150000),
(2, 1, 'Joki Rank Mythic-Glory', 200000),
(3, 1, 'Joki Classic 100 Match', 50000),
(4, 2, 'Top Up 100 Diamond', 15000),
(5, 2, 'Top Up 500 Diamond', 60000),
(6, 2, 'Top Up 1000 Diamond', 100000);
(7, 3, 'Starlight Member Normal', 35000)
(8, 3, 'Starlight Member Premium', 120000)
(9, 3, 'Weekly Pass', 120000)

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
