CREATE TABLE employees (
SNO TEXT PRIMARY KEY,
SNAME TEXT,
STATUS INTEGER,
CITY TEXT);

INSERT INTO employees (SNO,SNAME ,STATUS,CITY) VALUES
('S1','Smith', 20, 'London'),
('S2','Jones', 30, 'Paris'),
('S3','Blake', 40, 'Paris'),
('S4','Clarke', 10, 'London'),
('S5','Adams', 50, 'Kolkata');
SELECT * FROM employees;
SELECT SNAME,CITY FROM employees;
SELECT * FROM employees
WHERE CITY= 'London';