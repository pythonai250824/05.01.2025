import sqlite3

# connector
db_name: str = "18_12_2024db.db"
conn = sqlite3.connect(db_name) # creates a connector
conn.row_factory = sqlite3.Row # allow me to use column name

# cursor
cursor = conn.cursor()  # creates a cursor

cursor.execute("SELECT * FROM sales")
rows = cursor.fetchall()
for row in rows:
    print(tuple(row))

conn.close()

