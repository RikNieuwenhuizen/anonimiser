import pymysql

source_conn = pymysql.connect(host='localhost', user='root', password='root', db='db2')

cursor = source_conn.cursor()
cursor.execute('SELECT * FROM klant')
data = cursor.fetchall()

source_conn.close()

