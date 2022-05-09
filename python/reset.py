#! C:/Users/anczo/AppData/Local/Programs/Python/Python38-32/python.exe
# -*- coding: utf-8 -*-

import cgi
import hashlib
import json
import os

import mysql.connector

import validate as vld

mydb = mysql.connector.connect(
    host="localhost",
    user="change",
    password="lJHZk(95.Sx.]Ash",
    database="projekt"
)

print("Content-Type: application/json")
print()


def getData(validate: bool):
    form = cgi.FieldStorage()

    password = form.getvalue("pass")
    token = form.getvalue("token")
    if validate:
        if not vld.validatePassword(password):
            return '', ''

    return token, password


token, password = getData(validate=True)

if '' not in zip(token, password):
    mycursor = mydb.cursor()
    try:
        sql = "SELECT u.email FROM auth AS a JOIN users AS u WHERE u.token LIKE %s"
        mycursor.execute(sql, (token,))
        x = mycursor.fetchall()
        mycursor.reset()
        if x is not None:
            email = x[0][0]
            sql = "UPDATE auth SET hash = %s, salt = %s WHERE email LIKE %s"
            salt = os.urandom(64)
            key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000, dklen=256)
            val = (key.hex(), salt.hex(), email)
            mycursor.execute(sql, val)

            sql = "UPDATE users SET token = NULL WHERE email = %s"
            mycursor.execute(sql, (email,))
            mydb.commit()
            web = """
                            <span>Udało się zmienić hasło użytkownika, przekierowanie nastąpi za 5 sekund.</span> <br>
                            <i class="fa fa-circle-o-notch fa-spin"></i>
                            <script type="text/javascript">
                                setTimeout(function() {
                                  location.href = '../index.html'    
                              }, 5000);

                            </script>"""
            print(json.dumps({"success": True, "html": web}))
        else:
            print(json.dumps({"success": False, "html": "Wystąpił błąd"}))
        mydb.commit()
    except mysql.connector.IntegrityError as err:
        web = """
        <span>Nie udało się zmienić hasła użytkownika, przekierowanie nastąpi za 5 sekund.</span> <br>
        <i class="fa fa-circle-o-notch fa-spin"></i>
        <script type="text/javascript">
            setTimeout(function() {
              location.href = '../index.html'    
          }, 5000);

        </script>"""

        print(json.dumps({"success": False, "html": web}))
