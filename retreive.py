import pymysql

source_conn = pymysql.connect(host='localhost', user='root', password='root', db='db2')

cursor = source_conn.cursor()
cursor.execute('SELECT * FROM klant')
data = cursor.fetchall()

print(data)


target_conn = pymysql.connect(host='localhost', user='root', password='root', db='db1')

# Post the data to the target database
cursor = target_conn.cursor()
for row in data:
    cursor.execute('INSERT INTO klant (voornaam,achternaam,mail,registratie_datum) VALUES (%s, %s, %s, %s)', row)

# Commit the changes to the target database
target_conn.commit()

# Close the database connections
source_conn.close()
target_conn.close()


