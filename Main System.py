import mysql.connector

# connection with database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql",
    database="school_db"
)

cur = con.cursor()

# function to add student
def add_student(c):
    r = int(input("Enter roll no: "))
    sid = input("Enter student id: ")
    n = input("Enter name: ")
    fn = input("Enter father's name: ")
    mn = input("Enter mother's name: ")
    ad = input("Enter address: ")
    mob = input("Enter mobile no: ")

    try:
        cur.execute(
            "INSERT INTO class_%s VALUES (%s,%s,%s,%s,%s,%s,%s)" % c,
            (r, sid, n, fn, mn, ad, mob)
        )
        con.commit()
        print("Student added successfully")
    except:
        print("Error: record already exists")

# function to view all students of a class
def view_class(c):
    cur.execute("SELECT * FROM class_%s" % c)
    data = cur.fetchall()

    if data == []:
        print("No data found")
    else:
        for i in data:
            print(i)

# function to view one student
def view_student(c):
    r = int(input("Enter roll no: "))
    cur.execute("SELECT * FROM class_%s WHERE roll_no=%s" % c, (r,))
    d = cur.fetchone()

    if d:
        print(d)
    else:
        print("Student not found")

# function to update mobile number
def update_student(c):
    r = int(input("Enter roll no: "))
    m = input("Enter new mobile no: ")
    cur.execute(
        "UPDATE class_%s SET mobile_no=%s WHERE roll_no=%s" % c,
        (m, r)
    )
    con.commit()

    if cur.rowcount > 0:
        print("Record updated")
    else:
        print("Student not found")

# function to delete student
def delete_student(c):
    r = int(input("Enter roll no: "))
    cur.execute("DELETE FROM class_%s WHERE roll_no=%s" % c, (r,))
    con.commit()

    if cur.rowcount > 0:
        print("Record deleted")
    else:
        print("Student not found")

# main program
while True:
    print("\n------ SCHOOL DATABASE MENU ------")
    print("1. Add Student")
    print("2. View all students of a class")
    print("3. View a particular student")
    print("4. Update student mobile number")
    print("5. Delete student record")
    print("6. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 6:
        print("Program finished")
        break

    c = int(input("Enter class (1-12): "))

    if c < 1 or c > 12:
        print("Invalid class")
        continue

    if ch == 1:
        add_student(c)
    elif ch == 2:
        view_class(c)
    elif ch == 3:
        view_student(c)
    elif ch == 4:
        update_student(c)
    elif ch == 5:
        delete_student(c)
    else:
        print("Wrong choice")

con.close()
