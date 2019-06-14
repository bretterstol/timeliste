import mysql.connector
from mysql.connector import errorcode
import config
from datetime import datetime

def getNow():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def clockIn():
    enter = {
        "start": getNow()
    }
    query = ("insert into sessions(start) values(%(start)s)")
    setIntoDatabase(query, enter)
    print(enter["start"])


def clockOut():
    query = ("update sessions set `end` = %(end)s where `end` is null and date(`start`) = %(to_day)s")
    values = {
        "end" : getNow(),
        "to_day": datetime.now().date()
    }
    setIntoDatabase(query, values)
    print(values["end"])

def setIntoDatabase(query, values):
    try:
        cnx = mysql.connector.connect(**config.getConfig())
        cursor = cnx.cursor()
        cursor.execute(query,values)
        cnx.commit()
    except mysql.connector.Error as error:
        print(error.msg)
    finally:
        cursor.close()
        cnx.close()

