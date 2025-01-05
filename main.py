import sqlite3

# connector
db_name: str = "18_12_2024db.db"
conn = sqlite3.connect(db_name) # creates a connector
conn.row_factory = sqlite3.Row # allow me to use column name

# cursor
cursor = conn.cursor()  # creates a cursor

#################### read from db

cursor.execute("SELECT * FROM sales")
rows = cursor.fetchall()  # [ sql_obj, sql_obj ... ]

# 1
# result = []
# for row in rows:
#     print(tuple(row))
#     result.append(tuple(row))
#     # usage of column name:
#     # print(row['category'])

# 2
result_list = [list(row) for row in rows]
result_dict = [dict(row) for row in rows]
result_tuple = [tuple(row) for row in rows]

for result in [result_list, result_dict, result_tuple]:
    print(result)

# read 1 result
# cursor.execute("SELECT * FROM sales where id = 1")
# row1 = cursor.fetchone()  # sql_obj
# print(tuple(row1))

#################### change the db

# cursor.execute("Delete from sales where id = 1")

# 1
# cursor.execute("update sales set product_name='Wireless Mouse 2.0' where id = 1")

# 2 better
cursor.execute("update sales set product_name=? where id =?",
               ('Wireless Mouse 3.0', 1))

# must commit after EACH update query
conn.commit()  # writes into db file

# Step 1: Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
''')
print("Table created or already exists.")

# Step 2: Insert data into the table
cursor.execute('''
    INSERT INTO users (name, age)
    VALUES (?, ?)
''', ("Alice", 30))
cursor.execute('''
    INSERT INTO users (name, age)
    VALUES (?, ?)
''', ("Bob", 25))
print("Data inserted.")

# Commit the changes
conn.commit()

# Step 4: Read data from the table
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()

print("\nData in 'users' table:")
for row in rows:
    print(tuple(row))

conn.close()

