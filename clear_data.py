import sqlite3

connection = sqlite3.connect("registrations.db")
cursor = connection.cursor()

cursor.execute("DELETE FROM registrations")

connection.commit()
connection.close()

print("All old registrations have been deleted.")
