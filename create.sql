    CREATE TABLE Country (
     land VARCHAR(25) NOT NULL PRIMARY KEY
);

CREATE TABLE Game(
    play VARCHAR(50) NOT NULL PRIMARY KEY
);

CREATE TABLE Author(
    author_name VARCHAR(50) NOT NULL PRIMARY KEY,
    author_country VARCHAR(25) NOT NULL,
    author_url VARCHAR(256),
    FOREIGN KEY(author_country) REFERENCES Country (land)
);

CREATE TABLE Map (
    map_id INT DEFAULT 0 CHECK(map_id >= 0) PRIMARY KEY,
    author_name VARCHAR(50) NOT NULL,
    map_name VARCHAR(256) NOT NULL,
    map_date DATE NOT NULL,
    rating INT DEFAULT 0,
    map_game VARCHAR(50) NOT NULL,
    downloads INT DEFAULT 0 CHECK(downloads >= 0),
    FOREIGN KEY(author_name) REFERENCES Author (author_name),
    FOREIGN KEY(map_game) REFERENCES Game (play)
    );