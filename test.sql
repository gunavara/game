-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Aug 04, 2016 at 06:48 PM
-- Server version: 10.1.13-MariaDB
-- PHP Version: 5.6.23

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `test`
--

-- --------------------------------------------------------

--
-- Table structure for table `players`
--

CREATE TABLE `players` (
  `id` int(11) NOT NULL,
  `username` varchar(50) DEFAULT NULL,
  `hero_class` varchar(20) DEFAULT NULL,
  `health_points` varchar(20) DEFAULT NULL,
  `hero_min_dmg` varchar(20) DEFAULT NULL,
  `hero_max_dmg` varchar(20) DEFAULT NULL,
  `hero_min_block` varchar(20) DEFAULT NULL,
  `hero_max_block` varchar(20) DEFAULT NULL,
  `player_xp` varchar(3) DEFAULT NULL,
  `queststage` varchar(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `players`
--

INSERT INTO `players` (`id`, `username`, `hero_class`, `health_points`, `hero_min_dmg`, `hero_max_dmg`, `hero_min_block`, `hero_max_block`, `player_xp`, `queststage`) VALUES
(1, 'Joro', 'Warrior', '55', '1', '3', '2', '4', '30', '3'),
(2, 'Dancho', 'Warrior', '100', '1', '3', '2', '4', NULL, NULL),
(3, 'JorjoArmani', 'Warrior', '100', '1', '3', '2', '4', NULL, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `players`
--
ALTER TABLE `players`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `players`
--
ALTER TABLE `players`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
