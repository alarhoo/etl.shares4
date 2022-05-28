from hdbcli import dbapi

conn = dbapi.connect(
    address="<hostname>",
    port=3,
    user="<username>",
    password="<password>"
)

cursor = conn.cursor()
cursor.execute("CREATE TABLE T1 (ID INTEGER PRIMARY KEY, C2 VARCHAR(255))")
cursor.close()

sql = 'INSERT INTO T1 (ID, C2) VALUES (?, ?)'
cursor = conn.cursor()
cursor.execute(sql, (1, 'hello'))
# returns True
cursor.execute(sql, (2, 'hello again'))
# returns True
cursor.close()
