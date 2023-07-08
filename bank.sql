DROP DATABASE IF EXISTS `bank`;
CREATE DATABASE IF NOT EXISTS `bank` 
USE `bank`;

DROP TABLE IF EXISTS `accounts`;
CREATE TABLE IF NOT EXISTS `accounts` (
  `account_name` varchar(25) DEFAULT NULL,
  `account_pin` varchar(4) DEFAULT NULL,
  `account_number` varchar(19) DEFAULT NULL,
  `balance` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

DROP TABLE IF EXISTS `historic`;
CREATE TABLE IF NOT EXISTS `historic` (
  `account_number` varchar(19) DEFAULT NULL,
  `action` varchar(19) DEFAULT NULL,
  `destination` varchar(19) DEFAULT NULL,
  `amount` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;