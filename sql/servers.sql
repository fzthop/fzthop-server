-- MySQL dump 10.13  Distrib 5.5.15, for Linux (x86_64)
--
-- Host: localhost    Database: servers
-- ------------------------------------------------------
-- Server version	5.5.15-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cpuinfo`
--

DROP TABLE IF EXISTS `cpuinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cpuinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hostid` varchar(40) NOT NULL DEFAULT '0',
  `us` varchar(10) NOT NULL DEFAULT '0',
  `sy` varchar(10) NOT NULL DEFAULT '0',
  `ni` varchar(10) NOT NULL DEFAULT '0',
  `idle` varchar(10) NOT NULL DEFAULT '0',
  `wa` varchar(10) NOT NULL DEFAULT '0',
  `hi` varchar(10) NOT NULL DEFAULT '0',
  `si` varchar(10) NOT NULL DEFAULT '0',
  `st` varchar(10) NOT NULL DEFAULT '0',
  `timestamp` int(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1837 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `diskinfo`
--

DROP TABLE IF EXISTS `diskinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `diskinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hostid` varchar(40) NOT NULL DEFAULT '0',
  `filesystem` varchar(100) NOT NULL DEFAULT '0',
  `mountedon` varchar(100) NOT NULL DEFAULT '0',
  `size` varchar(100) NOT NULL DEFAULT '0',
  `used` varchar(100) NOT NULL DEFAULT '0',
  `availused` varchar(100) NOT NULL DEFAULT '0',
  `sizeuse` varchar(100) NOT NULL DEFAULT '0',
  `nodeuse` varchar(100) NOT NULL DEFAULT '0',
  `timestamp` int(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16219 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `hardwareinfo`
--

DROP TABLE IF EXISTS `hardwareinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hardwareinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hostid` varchar(40) NOT NULL DEFAULT '0',
  `blos` varchar(1000) NOT NULL DEFAULT '0',
  `system` varchar(1000) NOT NULL DEFAULT '0',
  `cpu` varchar(2000) NOT NULL DEFAULT '0',
  `mem` varchar(10000) NOT NULL DEFAULT '0',
  `cache` varchar(1000) NOT NULL DEFAULT '0',
  `disk` varchar(1000) NOT NULL DEFAULT '0',
  `net` varchar(2000) NOT NULL DEFAULT '0',
  `timestamp` int(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `hostinfo`
--

DROP TABLE IF EXISTS `hostinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hostinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hostid` varchar(40) NOT NULL DEFAULT '0',
  `groupid` varchar(40) NOT NULL DEFAULT '0',
  `osversion` varchar(40) NOT NULL DEFAULT '0',
  `osname` varchar(40) NOT NULL DEFAULT '0',
  `kernel` varchar(40) NOT NULL DEFAULT '0',
  `ipadd` varchar(40) NOT NULL DEFAULT '0',
  `timestamp` int(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `hostid` (`hostid`)
) ENGINE=InnoDB AUTO_INCREMENT=1747 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ioinfo`
--

DROP TABLE IF EXISTS `ioinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ioinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hostid` varchar(40) NOT NULL DEFAULT '0',
  `await` varchar(20) NOT NULL DEFAULT '0',
  `util` varchar(20) NOT NULL DEFAULT '0',
  `device` varchar(20) NOT NULL DEFAULT '0',
  `timestamp` int(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19891 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `loadsinfo`
--

DROP TABLE IF EXISTS `loadsinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `loadsinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hostid` varchar(40) NOT NULL DEFAULT '0',
  `load1` varchar(5) NOT NULL DEFAULT '0',
  `load5` varchar(5) NOT NULL DEFAULT '0',
  `load15` varchar(5) NOT NULL DEFAULT '0',
  `timestamp` int(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1837 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `memoryinfo`
--

DROP TABLE IF EXISTS `memoryinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `memoryinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hostid` varchar(40) NOT NULL DEFAULT '0',
  `physical_total` varchar(20) NOT NULL DEFAULT '0',
  `physical_used` varchar(20) NOT NULL DEFAULT '0',
  `physical_free` varchar(20) NOT NULL DEFAULT '0',
  `physical_shard` varchar(20) NOT NULL DEFAULT '0',
  `physical_buffers` varchar(20) NOT NULL DEFAULT '0',
  `physical_cached` varchar(20) NOT NULL DEFAULT '0',
  `buffers_used` varchar(20) NOT NULL DEFAULT '0',
  `buffers_cache` varchar(20) NOT NULL DEFAULT '0',
  `swap_total` varchar(20) NOT NULL DEFAULT '0',
  `swap_used` varchar(20) NOT NULL DEFAULT '0',
  `swap_free` varchar(20) NOT NULL DEFAULT '0',
  `timestamp` int(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1837 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `netinfo`
--

DROP TABLE IF EXISTS `netinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `netinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hostid` varchar(40) NOT NULL DEFAULT '0',
  `input` varchar(100) NOT NULL DEFAULT '0',
  `output` varchar(100) NOT NULL DEFAULT '0',
  `ipadd` varchar(100) NOT NULL DEFAULT '0',
  `name` varchar(40) NOT NULL DEFAULT '0',
  `timestamp` int(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13465 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `processinfo`
--

DROP TABLE IF EXISTS `processinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `processinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hostid` varchar(40) NOT NULL DEFAULT '0',
  `total` varchar(5) NOT NULL DEFAULT '0',
  `running` varchar(5) NOT NULL DEFAULT '0',
  `sleeping` varchar(5) NOT NULL DEFAULT '0',
  `stopped` varchar(5) NOT NULL DEFAULT '0',
  `zombie` varchar(5) NOT NULL DEFAULT '0',
  `timestamp` int(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1837 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2013-04-16 16:49:16
