-- phpMyAdmin SQL Dump
-- version 4.7.7
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Feb 08, 2018 at 06:59 PM
-- Server version: 10.1.30-MariaDB
-- PHP Version: 7.2.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Restaurant`
--

-- --------------------------------------------------------

--
-- Table structure for table `Menu`
--

CREATE TABLE `Menu` (
  `Menu_id` int(11) NOT NULL,
  `Menu_name` varchar(200) NOT NULL,
  `Restaurant_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Menu`
--

INSERT INTO `Menu` (`Menu_id`, `Menu_name`, `Restaurant_id`) VALUES
(1, 'Breakfast', 7);

-- --------------------------------------------------------

--
-- Table structure for table `MenuItem`
--

CREATE TABLE `MenuItem` (
  `item_id` int(11) NOT NULL,
  `item_name` varchar(200) NOT NULL,
  `item_cost` int(11) NOT NULL,
  `Menu_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `MenuItem`
--

INSERT INTO `MenuItem` (`item_id`, `item_name`, `item_cost`, `Menu_id`) VALUES
(1, 'paneer', 100, 1);

-- --------------------------------------------------------

--
-- Table structure for table `RestaurantTable`
--

CREATE TABLE `RestaurantTable` (
  `Restaurant_id` int(11) NOT NULL,
  `Restaurant_name` varchar(100) NOT NULL,
  `Restaurant_address` varchar(1000) NOT NULL,
  `Restaurant_contact` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `RestaurantTable`
--

INSERT INTO `RestaurantTable` (`Restaurant_id`, `Restaurant_name`, `Restaurant_address`, `Restaurant_contact`) VALUES
(1, 'Udipi1235', '1015 E UNIVERSITY DR', 1234567890),
(7, 'Udipi1', '1015 E UNIVERSITY DR', 1234567890),
(8, 'Udipi12', '1015 E UNIVERSITY DR', 1234567890),
(9, 'Udipi123', '1015 E UNIVERSITY DR', 1234567890);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Menu`
--
ALTER TABLE `Menu`
  ADD PRIMARY KEY (`Menu_id`),
  ADD KEY `fk_restid` (`Restaurant_id`);

--
-- Indexes for table `MenuItem`
--
ALTER TABLE `MenuItem`
  ADD PRIMARY KEY (`item_name`,`Menu_id`),
  ADD KEY `fk_menuid` (`Menu_id`);

--
-- Indexes for table `RestaurantTable`
--
ALTER TABLE `RestaurantTable`
  ADD PRIMARY KEY (`Restaurant_id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Menu`
--
ALTER TABLE `Menu`
  ADD CONSTRAINT `fk_restid` FOREIGN KEY (`Restaurant_id`) REFERENCES `RestaurantTable` (`Restaurant_id`);

--
-- Constraints for table `MenuItem`
--
ALTER TABLE `MenuItem`
  ADD CONSTRAINT `fk_menuid` FOREIGN KEY (`Menu_id`) REFERENCES `Menu` (`Menu_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
