-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 09, 2023 at 07:10 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `onlineclassdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `discussion`
--

CREATE TABLE `discussion` (
  `disid` int(11) NOT NULL,
  `fromid` varchar(50) NOT NULL,
  `fromname` varchar(50) NOT NULL,
  `toid` varchar(50) NOT NULL,
  `toname` varchar(50) NOT NULL,
  `msg` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL DEFAULT 'create'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `ebooks`
--

CREATE TABLE `ebooks` (
  `bookid` int(11) NOT NULL,
  `bookname` varchar(50) NOT NULL,
  `bookpdf` varchar(50) NOT NULL,
  `subject` varchar(50) NOT NULL,
  `class` varchar(50) NOT NULL,
  `tutorid` varchar(50) NOT NULL,
  `tutorname` varchar(50) NOT NULL,
  `date` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL DEFAULT 'create'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `marklist`
--

CREATE TABLE `marklist` (
  `markid` int(11) NOT NULL,
  `tutorid` varchar(50) NOT NULL,
  `tutorname` varchar(50) NOT NULL,
  `parentid` varchar(50) NOT NULL,
  `parentname` varchar(50) NOT NULL,
  `date` varchar(50) NOT NULL,
  `mark` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL DEFAULT 'create'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `onlinetest`
--

CREATE TABLE `onlinetest` (
  `testid` int(11) NOT NULL,
  `tutorid` varchar(50) NOT NULL,
  `tutorname` varchar(50) NOT NULL,
  `date` varchar(50) NOT NULL,
  `question` varchar(200) NOT NULL,
  `option1` varchar(50) NOT NULL,
  `option2` varchar(50) NOT NULL,
  `option3` varchar(50) NOT NULL,
  `option4` varchar(50) NOT NULL,
  `correctanswer` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL DEFAULT 'create'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `parent`
--

CREATE TABLE `parent` (
  `parentid` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `qualification` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `dob` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `date` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL DEFAULT 'create',
  `photo` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

CREATE TABLE `payment` (
  `pid` int(11) NOT NULL,
  `tutorid` int(11) NOT NULL,
  `tutorname` varchar(50) NOT NULL,
  `class` varchar(50) NOT NULL,
  `subject` varchar(50) NOT NULL,
  `parentid` int(11) NOT NULL,
  `parentname` varchar(50) NOT NULL,
  `price` varchar(50) NOT NULL,
  `date` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL DEFAULT 'create',
  `parentphoto` varchar(500) NOT NULL,
  `tutorphoto` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `progress`
--

CREATE TABLE `progress` (
  `prgid` int(11) NOT NULL,
  `tutorid` varchar(50) NOT NULL,
  `tutorname` varchar(50) NOT NULL,
  `parentid` varchar(50) NOT NULL,
  `parentname` varchar(50) NOT NULL,
  `progressdtl` varchar(500) NOT NULL,
  `progresscard` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL DEFAULT 'create'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `rating`
--

CREATE TABLE `rating` (
  `ratingid` int(11) NOT NULL,
  `parentid` varchar(50) NOT NULL,
  `parentname` varchar(50) NOT NULL,
  `tutorid` varchar(50) NOT NULL,
  `tutorname` varchar(50) NOT NULL,
  `rating` varchar(50) NOT NULL,
  `feedback` varchar(500) NOT NULL,
  `status` varchar(50) NOT NULL DEFAULT 'create'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tutor`
--

CREATE TABLE `tutor` (
  `tutorid` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `qualification` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `dob` varchar(50) NOT NULL,
  `subject` varchar(50) NOT NULL,
  `class` varchar(50) NOT NULL,
  `experience` varchar(50) NOT NULL,
  `fees` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL DEFAULT 'create',
  `photo` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `video`
--

CREATE TABLE `video` (
  `videoid` int(11) NOT NULL,
  `videoname` varchar(50) NOT NULL,
  `videofile` varchar(500) NOT NULL,
  `subject` varchar(50) NOT NULL,
  `class` varchar(50) NOT NULL,
  `tutorid` varchar(50) NOT NULL,
  `tutorname` varchar(50) NOT NULL,
  `date` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL DEFAULT 'create'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `discussion`
--
ALTER TABLE `discussion`
  ADD PRIMARY KEY (`disid`);

--
-- Indexes for table `ebooks`
--
ALTER TABLE `ebooks`
  ADD PRIMARY KEY (`bookid`);

--
-- Indexes for table `marklist`
--
ALTER TABLE `marklist`
  ADD PRIMARY KEY (`markid`);

--
-- Indexes for table `onlinetest`
--
ALTER TABLE `onlinetest`
  ADD PRIMARY KEY (`testid`);

--
-- Indexes for table `parent`
--
ALTER TABLE `parent`
  ADD PRIMARY KEY (`parentid`);

--
-- Indexes for table `payment`
--
ALTER TABLE `payment`
  ADD PRIMARY KEY (`pid`);

--
-- Indexes for table `progress`
--
ALTER TABLE `progress`
  ADD PRIMARY KEY (`prgid`);

--
-- Indexes for table `rating`
--
ALTER TABLE `rating`
  ADD PRIMARY KEY (`ratingid`);

--
-- Indexes for table `tutor`
--
ALTER TABLE `tutor`
  ADD PRIMARY KEY (`tutorid`);

--
-- Indexes for table `video`
--
ALTER TABLE `video`
  ADD PRIMARY KEY (`videoid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `discussion`
--
ALTER TABLE `discussion`
  MODIFY `disid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `ebooks`
--
ALTER TABLE `ebooks`
  MODIFY `bookid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `marklist`
--
ALTER TABLE `marklist`
  MODIFY `markid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `onlinetest`
--
ALTER TABLE `onlinetest`
  MODIFY `testid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `parent`
--
ALTER TABLE `parent`
  MODIFY `parentid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `payment`
--
ALTER TABLE `payment`
  MODIFY `pid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `progress`
--
ALTER TABLE `progress`
  MODIFY `prgid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `rating`
--
ALTER TABLE `rating`
  MODIFY `ratingid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tutor`
--
ALTER TABLE `tutor`
  MODIFY `tutorid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `video`
--
ALTER TABLE `video`
  MODIFY `videoid` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
