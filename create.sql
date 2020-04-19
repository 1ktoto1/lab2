CREATE TABLE Country (
     land VARCHAR(25) NOT NULL PRIMARY KEY
);

CREATE TABLE Game(
    play VARCHAR(50) NOT NULL PRIMARY KEY
);

CREATE TABLE Author(
    author_name VARCHAR(50) NOT NULL PRIMARY KEY,
    author_country VARCHAR(25) NOT NULL,
    author_url VARCHAR(255)
);

CREATE TABLE Map (
    map_id INT DEFAULT 0 CHECK(map_id >= 0) PRIMARY KEY,
    author_name VARCHAR(50) NOT NULL,
    map_name VARCHAR(70) NOT NULL,
    map_size VARCHAR(10) NOT NULL,
    rating INT DEFAULT 0,
    map_game VARCHAR(50) NOT NULL,
    downloads INT DEFAULT 0 CHECK(downloads >= 0)
);