#ca marche !

import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='mokkiDB',
                                         user='root',
                                         password='root',port=8889)

    mySql_insert_query = """INSERT INTO Users (first_name, last_name, company_email) 
                           VALUES 
                           ('jackie', 'chan', 'jacke@chan.china') """

    cursor = connection.cursor()
    result = cursor.execute(mySql_insert_query)
    connection.commit()
    print("Record inserted successfully into Laptop table")
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into Laptop table {}".format(error))

finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")