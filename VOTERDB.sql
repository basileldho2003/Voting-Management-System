-- MariaDB dump 10.19  Distrib 10.6.11-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: VOTERDB
-- ------------------------------------------------------
-- Server version	10.6.11-MariaDB-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Database creation
DROP DATABASE IF EXISTS VOTERDB ;
CREATE DATABASE VOTERDB ;

--
-- Table structure for table `ADMIN_CREDENTIALS`
--

DROP TABLE IF EXISTS `ADMIN_CREDENTIALS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ADMIN_CREDENTIALS` (
  `PASSWORD` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ADMIN_CREDENTIALS`
--

LOCK TABLES `ADMIN_CREDENTIALS` WRITE;
/*!40000 ALTER TABLE `ADMIN_CREDENTIALS` DISABLE KEYS */;
INSERT INTO `ADMIN_CREDENTIALS` VALUES ('admin#123');
/*!40000 ALTER TABLE `ADMIN_CREDENTIALS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CANDIDATE_LIST`
--

DROP TABLE IF EXISTS `CANDIDATE_LIST`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CANDIDATE_LIST` (
  `CID` varchar(5) NOT NULL,
  `CNAME` varchar(30) NOT NULL,
  `PARTY` varchar(8) NOT NULL,
  `SYMBOL` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`CID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CANDIDATE_LIST`
--

LOCK TABLES `CANDIDATE_LIST` WRITE;
/*!40000 ALTER TABLE `CANDIDATE_LIST` DISABLE KEYS */;
/*!40000 ALTER TABLE `CANDIDATE_LIST` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CANDIDATE_VOTED`
--

DROP TABLE IF EXISTS `CANDIDATE_VOTED`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CANDIDATE_VOTED` (
  `CID` varchar(5) NOT NULL,
  `VOTED` int(1) NOT NULL DEFAULT 0,
  KEY `CANDIDATE_VOTED_FK` (`CID`),
  CONSTRAINT `CANDIDATE_VOTED_FK` FOREIGN KEY (`CID`) REFERENCES `CANDIDATE_LIST` (`CID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CANDIDATE_VOTED`
--

LOCK TABLES `CANDIDATE_VOTED` WRITE;
/*!40000 ALTER TABLE `CANDIDATE_VOTED` DISABLE KEYS */;
/*!40000 ALTER TABLE `CANDIDATE_VOTED` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `LOGIN_DETAILS`
--

DROP TABLE IF EXISTS `LOGIN_DETAILS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `LOGIN_DETAILS` (
  `AADHAR_ID` bigint(11) NOT NULL,
  `PASSWORD` varchar(255) NOT NULL,
  PRIMARY KEY (`AADHAR_ID`),
  CONSTRAINT `LOGIN_DETAILS_FK` FOREIGN KEY (`AADHAR_ID`) REFERENCES `VOTER_DETAILS` (`AADHAR_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LOGIN_DETAILS`
--

LOCK TABLES `LOGIN_DETAILS` WRITE;
/*!40000 ALTER TABLE `LOGIN_DETAILS` DISABLE KEYS */;
/*!40000 ALTER TABLE `LOGIN_DETAILS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `VOTED`
--

DROP TABLE IF EXISTS `VOTED`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `VOTED` (
  `AADHAR_ID` bigint(11) NOT NULL,
  `VOTED` int(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (`AADHAR_ID`),
  CONSTRAINT `VOTED_FK` FOREIGN KEY (`AADHAR_ID`) REFERENCES `VOTER_DETAILS` (`AADHAR_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `VOTED`
--

LOCK TABLES `VOTED` WRITE;
/*!40000 ALTER TABLE `VOTED` DISABLE KEYS */;
/*!40000 ALTER TABLE `VOTED` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `VOTER_DETAILS`
--

DROP TABLE IF EXISTS `VOTER_DETAILS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `VOTER_DETAILS` (
  `AADHAR_ID` bigint(11) NOT NULL,
  `VNAME` varchar(30) NOT NULL,
  `DOB` date NOT NULL,
  `AGE` int(3) NOT NULL,
  `GENDER` char(1) NOT NULL,
  `EDUCATION` varchar(25) DEFAULT NULL,
  `CID` char(5) DEFAULT NULL,
  PRIMARY KEY (`AADHAR_ID`),
  UNIQUE KEY `VOTER_DETAILS_UN` (`CID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `VOTER_DETAILS`
--

LOCK TABLES `VOTER_DETAILS` WRITE;
/*!40000 ALTER TABLE `VOTER_DETAILS` DISABLE KEYS */;
/*!40000 ALTER TABLE `VOTER_DETAILS` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-21 17:20:54
