




















DROP TABLE IF EXISTS `boston_celtics_per_game_stats_renamed`;


CREATE TABLE `boston_celtics_per_game_stats_renamed` (
  `Rank` int DEFAULT NULL,
  `Player Name` text,
  `Age` int DEFAULT NULL,
  `Games Played` int DEFAULT NULL,
  `Games Started` int DEFAULT NULL,
  `Minutes Played` double DEFAULT NULL,
  `Field Goals Made` double DEFAULT NULL,
  `Field Goals Attempted` double DEFAULT NULL,
  `Field Goal Percentage` double DEFAULT NULL,
  `Three-Point Shots Made` double DEFAULT NULL,
  `Three-Point Shots Attempted` double DEFAULT NULL,
  `Three-Point Percentage` double DEFAULT NULL,
  `Two-Point Shots Made` double DEFAULT NULL,
  `Two-Point Shots Attempted` double DEFAULT NULL,
  `Two-Point Percentage` double DEFAULT NULL,
  `Effective Field Goal Percentage` double DEFAULT NULL,
  `Free Throws Made` double DEFAULT NULL,
  `Free Throws Attempted` double DEFAULT NULL,
  `Free Throw Percentage` double DEFAULT NULL,
  `Offensive Rebounds` double DEFAULT NULL,
  `Defensive Rebounds` double DEFAULT NULL,
  `Total Rebounds` double DEFAULT NULL,
  `Assists` double DEFAULT NULL,
  `Steals` double DEFAULT NULL,
  `Blocks` double DEFAULT NULL,
  `Turnovers` double DEFAULT NULL,
  `Personal Fouls` double DEFAULT NULL,
  `Points` double DEFAULT NULL
) ;








INSERT INTO `boston_celtics_per_game_stats_renamed` VALUES (1,'Jayson Tatum',25,74,74,35.7,9.1,19.3,0.471,3.1,8.2,0.376,6,11,0.542,0.552,5.6,6.7,0.833,0.9,7.2,8.1,4.9,1,0.6,2.5,2,26.9),(2,'Jaylen Brown',27,70,70,33.5,9,17.9,0.499,2.1,5.9,0.354,6.9,12.1,0.57,0.557,3,4.3,0.703,1.2,4.3,5.5,3.6,1.2,0.5,2.4,2.6,23),(3,'Jrue Holiday',33,69,69,32.8,4.8,10,0.48,2,4.7,0.429,2.8,5.3,0.526,0.581,0.9,1,0.833,1.2,4.2,5.4,4.8,0.9,0.8,1.8,1.6,12.5),(4,'Derrick White',29,73,73,32.6,5.3,11.5,0.461,2.7,6.8,0.396,2.6,4.7,0.555,0.578,1.9,2.1,0.901,0.7,3.5,4.2,5.2,1,1.2,1.5,2.1,15.2),(5,'Kristaps PorziÅ†Ä£is',28,57,57,29.6,6.8,13.2,0.516,1.9,5.1,0.375,4.9,8.1,0.606,0.589,4.5,5.3,0.858,1.7,5.5,7.2,2,0.7,1.9,1.6,2.7,20.1),(6,'Al Horford',37,65,33,26.8,3.3,6.4,0.511,1.7,4,0.419,1.6,2.5,0.658,0.64,0.4,0.5,0.867,1.3,5.1,6.4,2.6,0.6,1,0.7,1.4,8.6),(7,'Payton Pritchard',26,82,5,22.3,3.6,7.7,0.468,1.8,4.7,0.385,1.8,3.1,0.593,0.583,0.6,0.7,0.821,0.9,2.4,3.2,3.4,0.5,0.1,0.7,1.3,9.6),(8,'Sam Hauser',26,79,13,22,3.2,7.1,0.446,2.5,5.9,0.424,0.7,1.2,0.559,0.623,0.2,0.2,0.895,0.6,2.9,3.5,1,0.5,0.3,0.4,1.3,9),(9,'Luke Kornet',28,63,7,15.6,2.3,3.2,0.7,0,0,1,2.2,3.2,0.698,0.702,0.8,0.9,0.907,1.9,2.3,4.1,1.1,0.4,1,0.3,1.2,5.3),(10,'Xavier Tillman Sr.',25,20,2,13.7,1.7,3.3,0.515,0.4,1.4,0.286,1.3,1.9,0.684,0.576,0.2,0.4,0.571,0.7,2,2.7,1,0.5,0.5,0.3,0.8,4),(12,'Oshae Brissett',25,55,1,11.5,1.2,2.8,0.444,0.3,1,0.273,1,1.8,0.541,0.493,0.9,1.5,0.602,1.1,1.8,2.9,0.8,0.3,0.1,0.4,1,3.7),(13,'Svi Mykhailiuk',26,41,2,10.1,1.4,3.3,0.416,1,2.6,0.389,0.4,0.7,0.517,0.569,0.1,0.2,0.667,0.3,1,1.2,0.9,0.3,0,0.3,0.5,4),(14,'Jordan Walsh',19,9,1,9.2,0.7,1.7,0.4,0.2,1,0.222,0.4,0.7,0.667,0.467,0.1,0.2,0.5,0.6,1.7,2.2,0.6,0.6,0.1,0.3,1.2,1.7),(16,'Jaden Springer',21,17,1,7.6,0.8,1.8,0.433,0.1,0.6,0.182,0.6,1.1,0.579,0.467,0.4,0.5,0.875,0.5,0.7,1.2,0.5,0.6,0.2,0.5,1,2.1),(17,'Dalano Banton',24,24,1,7.1,0.8,2.1,0.373,0.1,0.7,0.125,0.7,1.5,0.486,0.392,0.7,0.8,0.8,0.5,1,1.5,0.8,0.2,0.1,0.4,0.8,2.3),(18,'Lamar Stevens',26,19,1,6.4,1.1,2.4,0.467,0.2,0.4,0.375,0.9,1.9,0.486,0.5,0.4,0.6,0.727,0.6,1,1.6,0.4,0.3,0.3,0.5,0.7,2.8),(19,'JD Davison',21,8,0,4.9,0.6,1.5,0.417,0.4,0.9,0.429,0.3,0.6,0.4,0.542,0.4,0.5,0.75,0.3,1,1.3,1.3,0.1,0.1,0.3,0.5,2);












