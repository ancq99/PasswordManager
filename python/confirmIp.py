#! C:/Users/anczo/AppData/Local/Programs/Python/Python38-32/python.exe
# -*- coding: utf-8 -*-

import cgi

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="change",
    password="lJHZk(95.Sx.]Ash",
    database="projekt"
)

print("Content-type: text/html; charset=UTF-8")
print()


def getData():
    form = cgi.FieldStorage()
    token = form.getvalue("token").split("_")
    ip = token[1]
    token = '_'.join(token)
    return token, ip


token, ip = getData()

mycursor = mydb.cursor()
try:
    sql = "SELECT email FROM users WHERE new_connection_token LIKE %s"
    mycursor.execute(sql, (token,))
    x = mycursor.fetchall()

    if len(x) == 1:
        sql = "UPDATE users SET connections = CONCAT(connections, %s), new_connection_token = NULL WHERE new_connection_token LIKE %s"
        mycursor.execute(sql, (ip + ";", token))

        print("Adres IP został potwierdzony")
    else:
        print("Błędny token")
    mydb.commit()

except mysql.connector.IntegrityError as err:
    print("Wystąpił nieoczekiwany błąd!")
