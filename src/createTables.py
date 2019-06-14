import mysql.connector
from mysql.connector import errorcode
import config

def getTables():
    Tables = {}
    Tables["sessions"] = (
    "create table `sessions`("
    "`id` int(11) not null auto_increment,"
    "`start` datetime not null,"
    "`end` datetime,"
    "primary key(`id`)"
    ")" 
    )
    return Tables


def createTable():
    table = getTables()["sessions"]
    try:
        cnx = mysql.connector.connect(**config.getConfig())
        cursor = cnx.cursor()
        cursor.execute(table)
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Already here")
        else:
            print(error.msg)
    else:
        print("ok")
    finally:
        cursor.close()
        cnx.close()

if(__name__ == "__main__"):
    createTable()
    print("hei")
