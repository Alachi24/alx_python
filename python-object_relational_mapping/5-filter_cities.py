# imported these packages for use
import MySQLdb
import sys

if __name__ == '__main__':

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # created a variable that establishes connection to MySQL server
    database = MySQLdb.connect(host="localhost", port=3306,
                               user=username,
                               passwd=password,
                               db=database)

    cursor = database.cursor()
    query = " SELECT cities.name FROM cities\
              JOIN states ON cities.state_id = states.id\
              WHERE states.name = %s\
              ORDER BY cities.id ASC"

    state = sys.argv[4]

    # executing a query
    cursor.execute(query, (state, ))

    # fetch all the matching rows
    cities = cursor.fetchall()

    rows = cursor.fetchall()
    city_names = [row[0] for row in rows]
    print(", ".join(city_names))

    # close both cursor and database connection
    cursor.close()
    database.close()
