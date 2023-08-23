# listing out all tables in a certain database
import MySQLdb

CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa

#create a variable
database = MySQLdb.connect(host = "localhost", port = 3306, user= "Aloni", passwd = "password", db = "hbtn_0e_0_usa")

#create a 'cursor', note it can be named anything
cursor = database.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id))");

state = ("California", "Arizona", "Texas", "Arizona", "Nevada")

for state in states:
    cursor.execute("INSERT INTO states (name) VALUES (%s)", states)