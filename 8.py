
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
sql = "UPDATE EMPLOYEE SET AGE = AGE +1 WHERE SEX = 'M'"
cursor.execute(sql)
print("Table updated.............")

print("Contents of the Employee table after update")
sql = '''SELECT * FROM EMPLOYEE'''
cursor.execute(sql)
print(cursor.fetchall())

conn.commit()

conn.close()

