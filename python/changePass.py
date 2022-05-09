#! C:/Users/anczo/AppData/Local/Programs/Python/Python38-32/python.exe
# -*- coding: utf-8 -*-

import cgi
import hashlib
import json
import os

import mysql.connector
from Crypto.Random import get_random_bytes

import config
import validate as vld

print("Content-Type: application/json")
print()

mydb = mysql.connector.connect(
    host="localhost",
    user="change",
    password="lJHZk(95.Sx.]Ash",
    database="projekt"
)


def getData(validate: bool):
    form = cgi.FieldStorage()

    oldPassword = form.getvalue("oldPass")
    newPassword = form.getvalue("newPass")

    if validate:
        if not vld.validatePassword(oldPassword) or not vld.validatePassword(newPassword):
            return '', ''

    return oldPassword, newPassword


validatedData = getData(validate=True)

if '' not in validatedData:
    mycursor = mydb.cursor()
    try:
        email = os.environ.get('HTTP_COOKIE').split("=")[1]
        sql = "SELECT email FROM users WHERE user_token = %s"
        mycursor.execute(sql, (email,))
        x = mycursor.fetchall()
        if len(x) == 1:
            sql = "SELECT `hash`, `salt` FROM `auth` WHERE `email` LIKE %s"
            mycursor.execute(sql, (email,))

            x = mycursor.fetchall()

            dbHash = x[0][0]
            salt = x[0][1]
            pepper = config.pepper

            key = hashlib.pbkdf2_hmac('sha256', bytes.fromhex(pepper) + validatedData[0].encode('utf-8'), bytes.fromhex(salt), 100000, dklen=256)

            if key == bytes.fromhex(dbHash):
                salt = os.urandom(64)
                key = hashlib.pbkdf2_hmac('sha256', validatedData[1].encode('utf-8'), salt, 100000, dklen=256)
                sql = "UPDATE `auth` SET `hash`= %s,`salt`= %s WHERE `email` LIKE %s"
                mycursor.execute(sql, (key.hex(), salt.hex(), email,))

                token = get_random_bytes(128).hex()
                sql = "UPDATE users SET user_token = %s WHERE user_token LIKE %s"
                mycursor.execute(sql, (token, email))

                print(json.dumps({"success": True}))
            else:
                web = """
                    <script type="text/javascript">
                        alert("Podanno błedne hasło. Nastąpi wylogowanie!") ? "" : location.reload();
                    </script>"""
                print(json.dumps({"success": False, "html": web}))

        mydb.commit()

    except mysql.connector.IntegrityError as err:
        web = """
                <script type="text/javascript">
                    alert("Nie udało sie zmienić hasła!")
                </script>"""
        print(json.dumps({"success": False, "html": web}))
