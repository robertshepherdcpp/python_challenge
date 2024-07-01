# Create an SQLite database named school.db.
# Create a table named teachers with fields for id, name, subject, and years_of_experience.
# Insert at least three records into the teachers table.
# Write a script to query and print all records from the teachers table.
import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE students
                  (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, subject TEXT)''')
conn.commit()
cursor.execute("INSERT INTO students (name, age, subject) VALUES (?, ?, ?)", ('Michael', 16, 'Maths'))
conn.commit()

cursor.execute('SELECT * FROM students')
data = cursor.fetchall()
for i in data:
    print(i)


