CREATE TABLE flights (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    origin TEXT NOT NULL,
    destination TEXT NOT NULL,
    duration INTEGER NOT NULL
);
 INSERT INTO flights (origin, destination, duration) VALUES ("New York", "London ", 245);
 UPDATE flights
    SET duration = 430
    WHERE origin = 'New York'
    ADD destination = 'London';
CREATE TABLE airports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    origin_id INTEGER PRIMARY KEY AUTOINCREMENT,
    destination_id INTEGER PRIMARY KEY AUTOINCREMENT,
);
CREATE TABLE passengers (
    person_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
);
SELECT first_name, origin, destination 
    FROM flights JOIN passengers 
    ON passenegers.flight_id = flights.id;
CREATE INDEX name_index ON passengers(first);