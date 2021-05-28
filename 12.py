
import psycopg2

conn = psycopg2.connect(
    database = "mydb", user = "postgres", password = "Intain@123",
    host = '127.0.0.1', port = '5432'
)
conn.autocommit = True
cursor = conn.cursor()

cursor.execute("SELECT * FROM CRICKETERS INNER JOIN ODISTATS ON CRICKETERS.FIRST_NAME = ODISTATS.FIRST_NAME")
result = cursor.fetchall()
print(result)

conn.commit()

conn.close()

