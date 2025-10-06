-- ลบตาราง demo เก่าทิ้งไปก่อน (ถ้ามี)
DROP TABLE IF EXISTS demo;

-- ส่วนที่ 1: สร้างโครงตาราง Departments
CREATE TABLE Departments (
    id INTEGER PRIMARY KEY,
    department_name TEXT
);

-- ส่วนที่ 2: สร้างโครงตาราง Employees
CREATE TABLE Employees (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    department_id INTEGER,
    salary INTEGER
);

-- ส่วนที่ 3: เพิ่มข้อมูลลงในตาราง Departments
INSERT INTO Departments (id, department_name) VALUES (1, 'Marketing');
INSERT INTO Departments (id, department_name) VALUES (2, 'Technology');
INSERT INTO Departments (id, department_name) VALUES (3, 'Management');

-- ส่วนที่ 4: เพิ่มข้อมูลลงในตาราง Employees
INSERT INTO Employees (id, first_name, last_name, department_id, salary) VALUES (1, 'Somchai', 'Rakdee', 1, 55000);
INSERT INTO Employees (id, first_name, last_name, department_id, salary) VALUES (2, 'Somsri', 'Jaidee', 1, 60000);
INSERT INTO Employees (id, first_name, last_name, department_id, salary) VALUES (3, 'Peter', 'Parker', 2, 72000);
INSERT INTO Employees (id, first_name, last_name, department_id, salary) VALUES (4, 'Tony', 'Stark', 3, 95000);
INSERT INTO Employees (id, first_name, last_name, department_id, salary) VALUES (5, 'Bruce', 'Banner', 2, 80000);

-- ดูข้อมูลทุกอย่างจากตาราง Employees
SELECT * FROM Employees;

-- ดูแค่ชื่อจริงและนามสกุลของพนักงาน
SELECT first_name, last_name FROM Employees;

--Day 1 โจทย์ประจำวัน: เขียนคำสั่ง SQL เพื่อดู department_name ทั้งหมดจากตาราง Departments
SELECT department_name from Departments; 

--Day 2 โจทย์ประจำวัน: เขียนคำสั่ง SQL เพื่อหาชื่อจริงของพนักงานที่เงินเดือนน้อยกว่า 60000
SELECT first_name from Employees WHERE salary <60000;

--Day 3 โจทย์ประจำวัน: เขียนคำสั่ง SQL เพื่อหาพนักงานที่มีเงินเดือนสูงที่สุด 3 อันดับแรก
SELECT first_name,salary from Employees ORDER by salary DESC LIMIT 3;

--Day 3.1 โจทย์ประจำวัน: เขียนคำสั่ง SQL เพื่อหาชื่อ และ รหัสพนักงานชื่อ Somchai
SELECT id,first_name FROM Employees WHERE first_name LIKE 'Somchai' ;