-- Day 4 ฟังก์ชันพื้นฐาน (COUNT, SUM, AVG)
-- นับจำนวนพนักงานทั้งหมด
SELECT COUNT(id) FROM Employees

-- หาผลรวมเงินเดือนของพนักงานทุกคน
SELECT SUM(salary) FROM Employees

-- โจทย์ประจำวัน: เขียนคำสั่ง SQL เพื่อหา "ค่าเฉลี่ย" เงินเดือนของพนักงานทุกคน
SELECT AVG(salary) FROM Employees

-- Day 5: การจัดกลุ่มข้อมูล (GROUP BY)
-- นับจำนวนพนักงานใน "แต่ละแผนก"
SELECT department_id, COUNT(id)
FROM Employees
GROUP BY department_id
-- ผลลัพธ์ที่ได้จะเป็นการบอกว่า department_id 1 มีกี่คน, id 2 มีกี่คน เป็นต้น
-- โจทย์ประจำวัน: เขียนคำสั่ง SQL เพื่อหา "เงินเดือนเฉลี่ย" ของ "แต่ละแผนก" 
SELECT AVG(salary) 
FROM Employees
GROUP BY department_id

-- Day 6: การเชื่อมตาราง (JOIN)
-- แสดงชื่อพนักงานคู่กับ "ชื่อแผนก" ของพวกเขา
SELECT E.first_name, D.department_name
FROM Employees AS E
JOIN Departments AS D ON E.department_id = D.id

--โจทย์ประจำวัน: เขียนคำสั่ง SQL เพื่อแสดงชื่อพนักงาน, เงินเดือน, และชื่อแผนก ของพนักงานที่อยู่แผนก Technology เท่านั้น
SELECT E.first_name, salary, D.department_name
FROM Employees AS E
JOIN Departments AS D ON E.department_id = D.id
WHERE department_name = "Technology"

--Day 7: ทบทวนและรวมร่าง!
-- โจทย์ประจำวัน: "จงหาชื่อแผนกที่มีเงินเดือนเฉลี่ยของพนักงานสูงกว่า 75,000 บาท"
-- คำใบ้: คุณต้องใช้ SELECT, AVG, FROM, JOIN, GROUP BY และ HAVING (คล้าย WHERE แต่ใช้กับเงื่อนไขของ GROUP BY)
SELECT D.department_name, AVG(salary)
FROM Employees AS E
JOIN Departments AS D ON E.department_id = D.id
GROUP BY department_id
HAVING salary >= 75000


