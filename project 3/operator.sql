CREATE TABLE customers (
NUMBER TEXT PRIMARY KEY,
NAME TEXT,
GRADE INTEGER,
CITY TEXT);

INSERT INTO customers (NUMBER,NAME ,GRADE ,CITY) VALUES
('S1','Smith', 103, 'London'),
('S2','Jones', 80, 'New york'),
('S3','Blake', 124, 'Paris'),
('S4','Clarke', 97, 'New york'),
('S5','Adams', 150, 'New york'),
('S5','James', 134, 'Kolkata'),
('S5','Lily', 23, 'New Delhi');


SELECT * FROM customers 
WHERE CITY= 'New york' AND GRADE > 100;

SELECT * FROM customers 
WHERE CITY= 'New york' AND GRADE < 100;