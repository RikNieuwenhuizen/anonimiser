import pymysql
import pandas as pd
from anonimize import data

target_conn = pymysql.connect(host='localhost', user='root', password='root', db='db1')


# Post the data to the target database
# insert the DataFrame into the database
data = pd.DataFrame(data = pd.DataFrame(data, columns=['voornaam', 'achternaam','mail','registratie_datum']))

# Commit the changes to the target database
target_conn.commit()

# Close the database connections
target_conn.close()