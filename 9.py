
import psycopg2

conn = psycopg2.connect(
    database = "mydb", user = "postgres", password = "Intain@123",
    host = '127.0.0.1', port = '5432'
)
conn.autocommit = True
cursor = conn.cursor()

print("Contents of the Employee table: ")
sql = '''SELECT * FROM EMPLOYEE'''
cursor.execute(sql)
print(cursor.fetchall())

#updating the records
sql = "DELETE FROM EMPLOYEE WHERE AGE >25 "
cursor.execute(sql)

print("Contents of the Employee table after update")
sql = '''SELECT * FROM EMPLOYEE'''
cursor.execute(sql)
print(cursor.fetchall())

conn.commit()

conn.close()

