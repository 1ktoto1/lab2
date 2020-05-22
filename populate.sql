INSERT INTO Country(country)
VALUES('Англия');
INSERT INTO Country(country)
VALUES('Россия');
INSERT INTO Country(country)
VALUES('Украина');
INSERT INTO Country(country)
VALUES('США');
INSERT INTO Country(country)
VALUES('Норвегия');
INSERT INTO Country(country)
VALUES('Дания');
INSERT INTO Country(country)
VALUES('Корея');
INSERT INTO Country(country)
VALUES('Италия');

INSERT INTO game(game)
VALUES('Герои Меча и Магии III: Рог Бездны');
INSERT INTO game(game)
VALUES('Герои Меча и Магии III: Клинок Армагеддона');

INSERT INTO Author(name, country, url)
VALUES('Antti Karhu','Англия','http://heroesportal.net/profile.php?id=588');
INSERT INTO Author(name, country, url)
VALUES('Stian Olsen','Норвегия','http://heroesportal.net/profile.php?id=590');
INSERT INTO Author(name, country, url)
VALUES('Morten','Дания','http://heroesportal.net/profile.php?id=582');
INSERT INTO Author(name, country, url)
VALUES('Rocco D Giordano','Италия','http://heroesportal.net/profile.php?id=586');
INSERT INTO Author(name,country, url)
VALUES('C Mojo','Корея','http://heroesportal.net/profile.php?id=574');
INSERT INTO Author(name, country, url)
VALUES('Never','Россия','http://heroesportal.net/profile.php?id=573');
INSERT INTO Author(name, author_country, url)
VALUES('Kian Colestock','США','http://heroesportal.net/profile.php?id=577');
INSERT INTO Author(name,country, url)
VALUES('Gorbik','Украина','http://heroesportal.net/profile.php?id=11');
INSERT INTO Author(name, country, url)
VALUES('il','Украина','http://heroesportal.net/profile.php?id=587');
INSERT INTO Author(name, country,url)
VALUES('Matteo Carriero','Италия','http://heroesportal.net/profile.php?id=572');

INSERT INTO Map(id, name, game, rating, author_name, dowloads, map_date);
VALUES(1,'The Quest','Герои Меча и Магии III: Рог Бездны',12,'Antti Karhu',64543,2002-05-13);
INSERT INTO Map(id, name, game, rating, author_name, dowloads, map_date);
VALUES(2,'Winter Wars','Герои Меча и Магии III: Рог Бездны',15,'Stian Olsen',7642,2006-12-13);
INSERT INTO Map(id, name, game, rating, author_name, dowloads, map_date);
VALUES(3,'queen','Герои Меча и Магии III: Рог Бездны',24,'Never',1235,2002-05-13,12);
INSERT INTO Map(id, name, game, rating, author_name, dowloads, map_date);
VALUES(4,'final fanta','Герои Меча и Магии III: Клинок Армагеддона',36,'Antti Karhu',78659,2005-04-03);
INSERT INTO Map(id, name, game, rating, author_name, dowloads, map_date);
