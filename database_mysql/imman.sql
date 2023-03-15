-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 14, 2023 at 03:02 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `imman`
--

-- --------------------------------------------------------

--
-- Table structure for table `course`
--

CREATE TABLE `course` (
  `name` varchar(20) NOT NULL,
  `image` varchar(60) NOT NULL,
  `duration` varchar(20) NOT NULL,
  `fees` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `course`
--

INSERT INTO `course` (`name`, `image`, `duration`, `fees`) VALUES
('C', 'a.jpg', '3months', '2500');

-- --------------------------------------------------------

--
-- Table structure for table `enquiry`
--

CREATE TABLE `enquiry` (
  `slno` varchar(8) NOT NULL,
  `name` varchar(30) NOT NULL,
  `regno` varchar(15) NOT NULL,
  `fname` varchar(30) NOT NULL,
  `dob` varchar(15) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `eduqua` varchar(30) NOT NULL,
  `clg` varchar(40) NOT NULL,
  `dateofadd` varchar(20) NOT NULL,
  `course` varchar(20) NOT NULL,
  `addofcom` varchar(50) NOT NULL,
  `email` varchar(20) NOT NULL,
  `phnoc` varchar(10) NOT NULL,
  `phnop` varchar(10) NOT NULL,
  `fees` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `enquiry`
--

INSERT INTO `enquiry` (`slno`, `name`, `regno`, `fname`, `dob`, `gender`, `eduqua`, `clg`, `dateofadd`, `course`, `addofcom`, `email`, `phnoc`, `phnop`, `fees`) VALUES
('1', 'Mani', '23srm001', 'Srini', '2001-03-08', 'male', 'B.com', 'Tagore Arts College', '2023-02-24', 'Python', 'Reddiarpalayam', 'mani11@gmail.com', '9087598934', '8735409866', '15000'),
('2', 'Uthish', '23srm002', 'Praveen', '2002-05-07', 'male', 'B.Tech', 'Christ College', '2023-03-14', 'C++', 'Muthiyalpet', 'uthish54@gmail.com', '9056383266', '9783471088', '5000'),
('3', 'lokesh', '23srm003', 'Kuppusamy', '2001-02-07', 'male', 'Mca', 'Amalavarpavam', '2021-04-03', 'Java', 'Muthiyalpet', 'lokesh009@gmail.com', '9708463829', '8740928374', '6000');

-- --------------------------------------------------------

--
-- Table structure for table `fees`
--

CREATE TABLE `fees` (
  `slno` varchar(8) NOT NULL,
  `transid` varchar(8) NOT NULL,
  `transdate` varchar(10) NOT NULL,
  `transmonth` varchar(10) NOT NULL,
  `transyear` varchar(10) NOT NULL,
  `transamount` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `fees`
--

INSERT INTO `fees` (`slno`, `transid`, `transdate`, `transmonth`, `transyear`, `transamount`) VALUES
('5', '23srm005', '09', '07', '2022', '4000'),
('6', '23srm004', '16', '02', '2023', '2000'),
('7', '23srm002', '16', '02', '2023', '1000'),
('8', '23srm002', '16', '02', '2023', '500'),
('6', '23srm006', '16', '02', '2023', '5000'),
('7', '23srm007', '17', '02', '2023', '1000'),
('1', '23srm001', '24', '02', '2023', '5000'),
('1', '23srm001', '28', '02', '2023', '1000'),
('1', '23srm001', '28', '02', '2023', '500');

-- --------------------------------------------------------

--
-- Table structure for table `staffregister`
--

CREATE TABLE `staffregister` (
  `id` varchar(10) NOT NULL,
  `name` varchar(30) NOT NULL,
  `address` varchar(50) NOT NULL,
  `majorsub` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `staffregister`
--

INSERT INTO `staffregister` (`id`, `name`, `address`, `majorsub`) VALUES
('21srm001', 'Sivaraman', 'Lawspet', 'C,C++,Python'),
('22srm002', 'Lakhsmi', 'Reddiarpalayam', 'Tally');

-- --------------------------------------------------------

--
-- Table structure for table `studentregister`
--

CREATE TABLE `studentregister` (
  `name` varchar(30) NOT NULL,
  `dob` varchar(15) NOT NULL,
  `email` varchar(20) NOT NULL,
  `phnoc` varchar(10) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `eduqua` varchar(20) NOT NULL,
  `slno` varchar(8) NOT NULL,
  `course` varchar(20) NOT NULL,
  `doa` varchar(15) NOT NULL,
  `aadhar` varchar(20) NOT NULL,
  `issdate` varchar(15) NOT NULL,
  `expdate` varchar(15) NOT NULL,
  `address` varchar(50) NOT NULL,
  `pincode` varchar(10) NOT NULL,
  `state` varchar(15) NOT NULL,
  `city` varchar(15) NOT NULL,
  `fname` varchar(25) NOT NULL,
  `mname` varchar(25) NOT NULL,
  `phnop` varchar(10) NOT NULL,
  `religion` varchar(15) NOT NULL,
  `nation` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `studentregister`
--

INSERT INTO `studentregister` (`name`, `dob`, `email`, `phnoc`, `gender`, `eduqua`, `slno`, `course`, `doa`, `aadhar`, `issdate`, `expdate`, `address`, `pincode`, `state`, `city`, `fname`, `mname`, `phnop`, `religion`, `nation`) VALUES
('Mani', '2001-03-08', 'mani11@gmail.com', '9087598934', 'Male', 'B.com', '1', 'Python', '2021-06-09', '758493870928', '2022-07-08', '2027-07-08', 'undefined', '605010', 'Puducherry ', 'Puducherry', 'Srini', 'Malavika', '8735409866', 'hindu', 'india');

-- --------------------------------------------------------

--
-- Table structure for table `student_marks`
--

CREATE TABLE `student_marks` (
  `Marks` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `student_marks`
--

INSERT INTO `student_marks` (`Marks`) VALUES
('30'),
('40');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
