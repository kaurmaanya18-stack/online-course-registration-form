
import sqlite3

connection = sqlite3.connect("registrations.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS registrations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    course TEXT
)
""")

cursor.execute("PRAGMA table_info(registrations)")
existing_columns = [column[1] for column in cursor.fetchall()]

new_columns = [
    ("mobile", "TEXT"),
    ("age", "INTEGER"),
    ("gender", "TEXT"),
    ("skills", "TEXT"),
    ("other_skills", "TEXT"),
    ("form_name", "TEXT"),
    ("registration_date", "TEXT"),
    ("registration_time", "TEXT"),
    ("reason", "TEXT")
]

for column_name, data_type in new_columns:
    if column_name not in existing_columns:
        cursor.execute(
            f"ALTER TABLE registrations ADD COLUMN {column_name} {data_type}"
        )
        print(f"Added column: {column_name}")

connection.commit()
connection.close()

print("Database setup completed successfully!")
