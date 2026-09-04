import sqlite3


connection = sqlite3.connect("practice.db")

cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    course TEXT NOT NULL,
    marks REAL NOT NULL
)
""")


cursor.execute(
    "INSERT INTO students (name, course, marks) VALUES (?, ?, ?)",
    ("Navya", "Python", 90)
)

cursor.execute(
    "INSERT INTO students (name, course, marks) VALUES (?, ?, ?)",
    ("John", "Java", 80)
)

cursor.execute(
    "INSERT INTO students (name, course, marks) VALUES (?, ?, ?)",
    ("Sara", "SQL", 95)
)


connection.commit()


cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

print("\nAll Students:")

for student in students:
    print(student)


minimum_marks = float(input("\nShow students with marks above: "))

cursor.execute(
    "SELECT * FROM students WHERE marks > ?",
    (minimum_marks,)
)

results = cursor.fetchall()

print("\nMatching Students:")

for student in results:
    print(student)


connection.close()


def get_all_students():
    connection = sqlite3.connect("practice.db")
    cursor = connection.cursor()

    cursor.execute("SELECT*FROM students")
    students = cursor.fetchall()
    connection.close()
    return students

print("\nStudents returned from function:")

students = get_all_students()

for student in students:
    print(
        f"ID: {student[0]} | "
        f"Name: {student[1]} | "
        f"Course: {student[2]} | "
        f"Marks: {student[3]}"
    )

# Find students in one course
connection = sqlite3.connect("practice.db")
cursor = connection.cursor()

course = input("\nEnter course to search: ")

cursor.execute(
    "SELECT * FROM students WHERE course = ?",
    (course,)
)

students = cursor.fetchall()

print("\nStudents in that course:")

for student in students:
    print(student)


# Calculate average marks
cursor.execute("SELECT AVG(marks) FROM students")

average = cursor.fetchone()[0]

print(f"\nAverage marks: {average:.2f}")


# Update one student's marks
student_id = int(input("\nEnter student ID to update: "))
new_marks = float(input("Enter new marks: "))

cursor.execute(
    "UPDATE students SET marks = ? WHERE id = ?",
    (new_marks, student_id)
)

connection.commit()


# Delete one student
delete_id = int(input("\nEnter student ID to delete: "))

cursor.execute(
    "DELETE FROM students WHERE id = ?",
    (delete_id,)
)

connection.commit()


# Display final table
cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

print("\nFinal Students Table:")

for student in students:
    print(student)

connection.close()