
import mysql.connector
from mysql.connector import errorcode
import config
from datetime import datetime
from math import floor

def getFromDatabase():
    tables = []
    query = (
        "select start, end "
        "from sessions"
        )
    try:
        cnx = mysql.connector.connect(**config.getConfig())
        cursor = cnx.cursor()
        cursor.execute(query)
        tables = [(start,end) for (start, end) in cursor if(end != None)]
    except mysql.connector.Error as error:
        print(error.msg)
    finally: 
        cursor.close()
        cnx.close()
        return tables

def getStatus():
    times = getFromDatabase()
    formattedDict = makeDict(times)
    formatted = formattedDict.values()
    eightHours = 8 * 3600
    completeSum = sum([(time.seconds - eightHours) for time in formatted])
    standings = convertSeconds(completeSum)
    print(standings)

def convertSeconds(seconds):
    s = inject_zero(floor(seconds % 60))
    m = inject_zero(floor((seconds / 60) % 60))
    h = inject_zero(floor((seconds / 60 / 60) % 24))
    return "{0}:{1}:{2}".format(h, m, s)


def inject_zero(number):
    if(number < 10):
        return "0{}".format(number)
    else:
        return number


def getDate(start):
    return "{0}-{1}-{2}".format(start.year, start.month, start.day)

def makeDict(liste):
    myDict = {}
    for (start, end) in liste:
        date = getDate(start)
        myDict[date] = getValue(myDict, date, start, end)
    return myDict

def getValue(myDict, date, start, end):
    if(myDict.get(date) != None):
        return myDict[date] + (end - start)
    else:
        return (end - start)