# listing out all tables in a certain database
import MySQLdb

# create a variable
database = MySQLdb.connect(host="localhost", port=3306,
                           user="Aloni", passwd="password", db="hbtn_0e_0_usa")

# create a 'cursor', note it can be named anything
cursor = database.cursor()
cursor.execute("SELECT id, name FROM states ORDER BY id ASC")
states = cursor.fetchall()

for state in states:
    print(state)

cursor.close()
database.close()
