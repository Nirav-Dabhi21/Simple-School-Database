import mysql.connector

# ---------- Connect to MySQL ----------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password"
)

cursor = conn.cursor()

# ---------- Create Database ----------
cursor.execute("CREATE DATABASE IF NOT EXISTS school_db")
cursor.execute("USE school_db")

# ---------- Create Class 1 Table ----------
cursor.execute("""
CREATE TABLE IF NOT EXISTS class_1 (
    roll_no INT PRIMARY KEY,
    student_id VARCHAR(20) UNIQUE,
    name VARCHAR(50),
    father_name VARCHAR(50),
    mother_name VARCHAR(50),
    address VARCHAR(100),
    mobile_no VARCHAR(15)
)
""")

# ---------- Create Tables for Class 2–12 ----------
for i in range(2, 13):
    cursor.execute(f"CREATE TABLE IF NOT EXISTS class_{i} LIKE class_1")

# ---------- Manual Student-Like Data for All Classes ----------
class_students = {
    1: [
        (1,'C1S001','Aarav Kumar','Rohit Kumar','Pooja Kumar','Delhi','9000000001'),
        (2,'C1S002','Anaya Singh','Vikas Singh','Neha Singh','Delhi','9000000002'),
        (3,'C1S003','Kabir Jain','Amit Jain','Ritu Jain','Delhi','9000000003'),
        (4,'C1S004','Myra Shah','Nikhil Shah','Kajal Shah','Delhi','9000000004'),
        (5,'C1S005','Vivaan Verma','Rakesh Verma','Sunita Verma','Delhi','9000000005'),
        (6,'C1S006','Isha Mehta','Suresh Mehta','Anita Mehta','Delhi','9000000006'),
        (7,'C1S007','Arjun Patel','Mahesh Patel','Kiran Patel','Delhi','9000000007'),
        (8,'C1S008','Siya Gupta','Raj Gupta','Seema Gupta','Delhi','9000000008'),
        (9,'C1S009','Reyansh Malhotra','Rajiv Malhotra','Anjali Malhotra','Delhi','9000000009'),
        (10,'C1S010','Diya Joshi','Manoj Joshi','Rekha Joshi','Delhi','9000000010')
    ],
    2: [
        (1,'C2S001','Rohan Patel','Mahesh Patel','Kiran Patel','Ahmedabad','9000000011'),
        (2,'C2S002','Diya Patel','Mahesh Patel','Kiran Patel','Ahmedabad','9000000012'),
        (3,'C2S003','Yash Shah','Amit Shah','Nidhi Shah','Ahmedabad','9000000013'),
        (4,'C2S004','Khushi Mehta','Suresh Mehta','Anita Mehta','Ahmedabad','9000000014'),
        (5,'C2S005','Ayaan Khan','Salman Khan','Farah Khan','Ahmedabad','9000000015'),
        (6,'C2S006','Nisha Joshi','Manoj Joshi','Rekha Joshi','Ahmedabad','9000000016'),
        (7,'C2S007','Dev Patel','Rakesh Patel','Sunita Patel','Ahmedabad','9000000017'),
        (8,'C2S008','Riya Sharma','Amit Sharma','Sunita Sharma','Ahmedabad','9000000018'),
        (9,'C2S009','Ishaan Gupta','Raj Gupta','Seema Gupta','Ahmedabad','9000000019'),
        (10,'C2S010','Anvi Jain','Sanjay Jain','Poonam Jain','Ahmedabad','9000000020')
    ],
    3: [
        (1,'C3S001','Arjun Mehta','Suresh Mehta','Anita Mehta','Mumbai','9000000021'),
        (2,'C3S002','Kavya Shah','Nikhil Shah','Kajal Shah','Mumbai','9000000022'),
        (3,'C3S003','Vivaan Verma','Rakesh Verma','Sunita Verma','Mumbai','9000000023'),
        (4,'C3S004','Anaya Singh','Vikas Singh','Neha Singh','Mumbai','9000000024'),
        (5,'C3S005','Isha Mehta','Suresh Mehta','Anita Mehta','Mumbai','9000000025'),
        (6,'C3S006','Reyansh Malhotra','Rajiv Malhotra','Anjali Malhotra','Mumbai','9000000026'),
        (7,'C3S007','Diya Joshi','Manoj Joshi','Rekha Joshi','Mumbai','9000000027'),
        (8,'C3S008','Aarav Kumar','Rohit Kumar','Pooja Kumar','Mumbai','9000000028'),
        (9,'C3S009','Arjun Patel','Mahesh Patel','Kiran Patel','Mumbai','9000000029'),
        (10,'C3S010','Siya Gupta','Raj Gupta','Seema Gupta','Mumbai','9000000030')
    ],
    4: [
        (1,'C4S001','Raghav Sharma','Amit Sharma','Sunita Sharma','Jaipur','9000000031'),
        (2,'C4S002','Meera Singh','Vikas Singh','Neha Singh','Jaipur','9000000032'),
        (3,'C4S003','Aryan Jain','Amit Jain','Ritu Jain','Jaipur','9000000033'),
        (4,'C4S004','Tara Shah','Nikhil Shah','Kajal Shah','Jaipur','9000000034'),
        (5,'C4S005','Krish Verma','Rakesh Verma','Sunita Verma','Jaipur','9000000035'),
        (6,'C4S006','Sanya Mehta','Suresh Mehta','Anita Mehta','Jaipur','9000000036'),
        (7,'C4S007','Ritvik Patel','Mahesh Patel','Kiran Patel','Jaipur','9000000037'),
        (8,'C4S008','Mira Gupta','Raj Gupta','Seema Gupta','Jaipur','9000000038'),
        (9,'C4S009','Aarav Malhotra','Rajiv Malhotra','Anjali Malhotra','Jaipur','9000000039'),
        (10,'C4S010','Anaya Joshi','Manoj Joshi','Rekha Joshi','Jaipur','9000000040')
    ],
    5: [
        (1,'C5S001','Rahul Sharma','Amit Sharma','Sunita Sharma','Bhopal','9000000041'),
        (2,'C5S002','Nikita Singh','Vikas Singh','Neha Singh','Bhopal','9000000042'),
        (3,'C5S003','Aditya Jain','Amit Jain','Ritu Jain','Bhopal','9000000043'),
        (4,'C5S004','Tanya Shah','Nikhil Shah','Kajal Shah','Bhopal','9000000044'),
        (5,'C5S005','Vihaan Verma','Rakesh Verma','Sunita Verma','Bhopal','9000000045'),
        (6,'C5S006','Ira Mehta','Suresh Mehta','Anita Mehta','Bhopal','9000000046'),
        (7,'C5S007','Arjun Patel','Mahesh Patel','Kiran Patel','Bhopal','9000000047'),
        (8,'C5S008','Riya Gupta','Raj Gupta','Seema Gupta','Bhopal','9000000048'),
        (9,'C5S009','Reyansh Malhotra','Rajiv Malhotra','Anjali Malhotra','Bhopal','9000000049'),
        (10,'C5S010','Diya Joshi','Manoj Joshi','Rekha Joshi','Bhopal','9000000050')
    ],
    6: [
        (1,'C6S001','Nikhil Sharma','Amit Sharma','Sunita Sharma','Indore','9000000051'),
        (2,'C6S002','Anvi Singh','Vikas Singh','Neha Singh','Indore','9000000052'),
        (3,'C6S003','Rohan Jain','Amit Jain','Ritu Jain','Indore','9000000053'),
        (4,'C6S004','Mira Shah','Nikhil Shah','Kajal Shah','Indore','9000000054'),
        (5,'C6S005','Krish Verma','Rakesh Verma','Sunita Verma','Indore','9000000055'),
        (6,'C6S006','Sanya Mehta','Suresh Mehta','Anita Mehta','Indore','9000000056'),
        (7,'C6S007','Arjun Patel','Mahesh Patel','Kiran Patel','Indore','9000000057'),
        (8,'C6S008','Riya Gupta','Raj Gupta','Seema Gupta','Indore','9000000058'),
        (9,'C6S009','Reyansh Malhotra','Rajiv Malhotra','Anjali Malhotra','Indore','9000000059'),
        (10,'C6S010','Diya Joshi','Manoj Joshi','Rekha Joshi','Indore','9000000060')
    ],
    7: [
        (1,'C7S001','Aarav Sharma','Amit Sharma','Sunita Sharma','Lucknow','9000000061'),
        (2,'C7S002','Nikita Singh','Vikas Singh','Neha Singh','Lucknow','9000000062'),
        (3,'C7S003','Aditya Jain','Amit Jain','Ritu Jain','Lucknow','9000000063'),
        (4,'C7S004','Tanya Shah','Nikhil Shah','Kajal Shah','Lucknow','9000000064'),
        (5,'C7S005','Vihaan Verma','Rakesh Verma','Sunita Verma','Lucknow','9000000065'),
        (6,'C7S006','Ira Mehta','Suresh Mehta','Anita Mehta','Lucknow','9000000066'),
        (7,'C7S007','Arjun Patel','Mahesh Patel','Kiran Patel','Lucknow','9000000067'),
        (8,'C7S008','Riya Gupta','Raj Gupta','Seema Gupta','Lucknow','9000000068'),
        (9,'C7S009','Reyansh Malhotra','Rajiv Malhotra','Anjali Malhotra','Lucknow','9000000069'),
        (10,'C7S010','Diya Joshi','Manoj Joshi','Rekha Joshi','Lucknow','9000000070')
    ],
    8: [
        (1,'C8S001','Raghav Sharma','Amit Sharma','Sunita Sharma','Noida','9000000071'),
        (2,'C8S002','Meera Singh','Vikas Singh','Neha Singh','Noida','9000000072'),
        (3,'C8S003','Aryan Jain','Amit Jain','Ritu Jain','Noida','9000000073'),
        (4,'C8S004','Tara Shah','Nikhil Shah','Kajal Shah','Noida','9000000074'),
        (5,'C8S005','Krish Verma','Rakesh Verma','Sunita Verma','Noida','9000000075'),
        (6,'C8S006','Sanya Mehta','Suresh Mehta','Anita Mehta','Noida','9000000076'),
        (7,'C8S007','Ritvik Patel','Mahesh Patel','Kiran Patel','Noida','9000000077'),
        (8,'C8S008','Mira Gupta','Raj Gupta','Seema Gupta','Noida','9000000078'),
        (9,'C8S009','Aarav Malhotra','Rajiv Malhotra','Anjali Malhotra','Noida','9000000079'),
        (10,'C8S010','Anaya Joshi','Manoj Joshi','Rekha Joshi','Noida','9000000080')
    ],
    9: [
        (1,'C9S001','Rahul Sharma','Amit Sharma','Sunita Sharma','Pune','9000000081'),
        (2,'C9S002','Nikita Singh','Vikas Singh','Neha Singh','Pune','9000000082'),
        (3,'C9S003','Aditya Jain','Amit Jain','Ritu Jain','Pune','9000000083'),
        (4,'C9S004','Tanya Shah','Nikhil Shah','Kajal Shah','Pune','9000000084'),
        (5,'C9S005','Vihaan Verma','Rakesh Verma','Sunita Verma','Pune','9000000085'),
        (6,'C9S006','Ira Mehta','Suresh Mehta','Anita Mehta','Pune','9000000086'),
        (7,'C9S007','Arjun Patel','Mahesh Patel','Kiran Patel','Pune','9000000087'),
        (8,'C9S008','Riya Gupta','Raj Gupta','Seema Gupta','Pune','9000000088'),
        (9,'C9S009','Reyansh Malhotra','Rajiv Malhotra','Anjali Malhotra','Pune','9000000089'),
        (10,'C9S010','Diya Joshi','Manoj Joshi','Rekha Joshi','Pune','9000000090')
    ],
    10: [
        (1,'C10S001','Aarav Sharma','Amit Sharma','Sunita Sharma','Chennai','9000000091'),
        (2,'C10S002','Nikita Singh','Vikas Singh','Neha Singh','Chennai','9000000092'),
        (3,'C10S003','Aditya Jain','Amit Jain','Ritu Jain','Chennai','9000000093'),
        (4,'C10S004','Tanya Shah','Nikhil Shah','Kajal Shah','Chennai','9000000094'),
        (5,'C10S005','Vihaan Verma','Rakesh Verma','Sunita Verma','Chennai','9000000095'),
        (6,'C10S006','Ira Mehta','Suresh Mehta','Anita Mehta','Chennai','9000000096'),
        (7,'C10S007','Arjun Patel','Mahesh Patel','Kiran Patel','Chennai','9000000097'),
        (8,'C10S008','Riya Gupta','Raj Gupta','Seema Gupta','Chennai','9000000098'),
        (9,'C10S009','Reyansh Malhotra','Rajiv Malhotra','Anjali Malhotra','Chennai','9000000099'),
        (10,'C10S010','Diya Joshi','Manoj Joshi','Rekha Joshi','Chennai','9000000100')
    ],
    11: [
        (1,'C11S001','Raghav Sharma','Amit Sharma','Sunita Sharma','Bangalore','9000000101'),
        (2,'C11S002','Meera Singh','Vikas Singh','Neha Singh','Bangalore','9000000102'),
        (3,'C11S003','Aryan Jain','Amit Jain','Ritu Jain','Bangalore','9000000103'),
        (4,'C11S004','Tara Shah','Nikhil Shah','Kajal Shah','Bangalore','9000000104'),
        (5,'C11S005','Krish Verma','Rakesh Verma','Sunita Verma','Bangalore','9000000105'),
        (6,'C11S006','Sanya Mehta','Suresh Mehta','Anita Mehta','Bangalore','9000000106'),
        (7,'C11S007','Ritvik Patel','Mahesh Patel','Kiran Patel','Bangalore','9000000107'),
        (8,'C11S008','Mira Gupta','Raj Gupta','Seema Gupta','Bangalore','9000000108'),
        (9,'C11S009','Aarav Malhotra','Rajiv Malhotra','Anjali Malhotra','Bangalore','9000000109'),
        (10,'C11S010','Anaya Joshi','Manoj Joshi','Rekha Joshi','Bangalore','9000000110')
    ],
    12: [
        (1,'C12S001','Rahul Sharma','Amit Sharma','Sunita Sharma','Hyderabad','9000000111'),
        (2,'C12S002','Nikita Singh','Vikas Singh','Neha Singh','Hyderabad','9000000112'),
        (3,'C12S003','Aditya Jain','Amit Jain','Ritu Jain','Hyderabad','9000000113'),
        (4,'C12S004','Tanya Shah','Nikhil Shah','Kajal Shah','Hyderabad','9000000114'),
        (5,'C12S005','Vihaan Verma','Rakesh Verma','Sunita Verma','Hyderabad','9000000115'),
        (6,'C12S006','Ira Mehta','Suresh Mehta','Anita Mehta','Hyderabad','9000000116'),
        (7,'C12S007','Arjun Patel','Mahesh Patel','Kiran Patel','Hyderabad','9000000117'),
        (8,'C12S008','Riya Gupta','Raj Gupta','Seema Gupta','Hyderabad','9000000118'),
        (9,'C12S009','Reyansh Malhotra','Rajiv Malhotra','Anjali Malhotra','Hyderabad','9000000119'),
        (10,'C12S010','Diya Joshi','Manoj Joshi','Rekha Joshi','Hyderabad','9000000120')
    ]
