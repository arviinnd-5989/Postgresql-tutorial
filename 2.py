import psycopg2

conn = psycopg2.connect(
    database = "postgres", user = "postgres", password = "Intain@123",
    host = '127.0.0.1', port = '5432'
)
conn.autocommit = True
cursor = conn.cursor()

sql = '''CREATE database mydb'''

cursor.execute(sql)
print("Database created successfully..............")

conn.close()
