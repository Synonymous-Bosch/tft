DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    puuid VARCHAR(255),
    username VARCHAR(255),
    tagline VARCHAR(255)
);