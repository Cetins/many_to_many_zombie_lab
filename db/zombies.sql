DROP TABLE IF EXISTS bitings;
DROP TABLE IF EXISTS humans;
DROP TABLE IF EXISTS zombies;
DROP TABLE IF EXISTS zombie_types;

CREATE TABLE humans (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE zombie_types (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE zombies (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    zombie_type_id INT REFERENCES zombie_types(id)
);

CREATE TABLE bitings (
    id SERIAL PRIMARY KEY,
    zombie_id SERIAL REFERENCES zombies(id),
    human_id SERIAL REFERENCES humans(id)
);
