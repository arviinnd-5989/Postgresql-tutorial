import psycopg2

conn = psycopg2.connect(
    database = "mydb", user = "postgres", password = "Intain@123",
    host = '127.0.0.1', port = '5432'
)
conn.autocommit = True
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

sql = '''CREATE TABLE EMPLOYEE(
    FIRST_NAME CHAR(20) NOT NULL,
    LAST_NAME CHAR(20),
    AGE INT,
    SEX CHAR(1),
    INCOME FLOAT)'''

cursor.execute(sql)

print("Table created successfully..............")

conn.close()
