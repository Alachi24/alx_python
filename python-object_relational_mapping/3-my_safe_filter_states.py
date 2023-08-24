# imported these packages for use
import MySQLdb
import sys

if __name__ == "__main__":

    # created a variable
    database = MySQLdb.connect(host="localhost", port=3306,
                               user=sys.argv[1],
                               passwd=sys.argv[2],
                               db=sys.argv[3])

    cursor = database.cursor()
    query = "SELECT id, name FROM states \
            WHERE BINARY name = %s \
            ORDER BY id ASC"

    state_name = sys.argv[4]

    cursor.execute = (query, (state_name, ))
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    database.close()
