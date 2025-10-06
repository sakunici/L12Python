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