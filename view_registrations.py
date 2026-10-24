import sqlite3

connection = sqlite3.connect("registrations.db")
cursor = connection.cursor()

cursor.execute("""
    SELECT
        id,
        name,
        email,
        course,
        mobile,
        age,
        gender,
        skills,
        other_skills,
        form_name,
        registration_date,
        registration_time,
        reason
    FROM registrations
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()
