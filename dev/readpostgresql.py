import psycopg2

conn = psycopg2.connect(
    dbname="mydb",
    user="myuser",
    password="mypassword",
    host="postgres-service",
    port="5432"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM your_table;")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
conn.close()

