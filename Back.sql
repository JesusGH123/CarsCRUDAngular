CREATE DATABASE cars;
USE cars;

DROP TABLE IF EXISTS car;
CREATE TABLE car(
	id INT AUTO_INCREMENT PRIMARY KEY,
    brand VARCHAR(30),
    model VARCHAR(30),
    year VARCHAR(4)
);

INSERT INTO car VALUES (0, 'Mazda', 'MX-5', '2018');
INSERT INTO car VALUES (0, 'Kia', 'Forte', '2022');
INSERT INTO car VALUES (0, 'Volkswagen', 'Beatle', '2005');
INSERT INTO car VALUES (0, 'BMW', 'Z4', '2021');
INSERT INTO car VALUES (0, 'Audi', 'A8', '2020');
INSERT INTO car VALUES (0, 'Kia', 'Rio', '2021');
INSERT INTO car VALUES (0, 'Mazda', 'Mazda 2', '2019');

SELECT * FROM car;