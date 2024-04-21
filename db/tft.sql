DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS player_ranking_summoner;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    puuid VARCHAR(255),
    username VARCHAR(255),
    tagline VARCHAR(255)
);

CREATE TABLE player_ranking_summoner (
    id SERIAL PRIMARY KEY,
    puuid VARCHAR(255),
    tagline VARCHAR(255),
    matchid VARCHAR(255),
    ranking SMALLINT
);