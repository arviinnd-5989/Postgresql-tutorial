import psycopg2

conn = psycopg2.connect(
    database = "mydb", user = "postgres", password = "Intain@123",
    host = '127.0.0.1', port = '5432'
)
conn.autocommit = True
cursor = conn.cursor()

cursor.execute('''SELECT * from EMPLOYEE ORDER BY AGE''')

result = cursor.fetchone()
print(result)

result=cursor.fetchall()
print(result)

conn.commit()

conn.close()

