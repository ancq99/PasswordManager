#! C:/Users/anczo/AppData/Local/Programs/Python/Python38-32/python.exe
# -*- coding: utf-8 -*-

import json
import os

import mysql.connector
from Crypto.Random import get_random_bytes

import getData as gd

print("Content-Type: application/json")
print()

mydb = mysql.connector.connect(
    host="localhost",
    user="change",
    password="lJHZk(95.Sx.]Ash",
    database="projekt"
)

email = os.environ.get('HTTP_COOKIE').split("=")[1]

mycursor = mydb.cursor()
try:
    token = get_random_bytes(128).hex()
    data = gd.getData(mycursor, False, True, email)

    sql = "UPDATE users SET user_token = %s WHERE user_token = %s"
    mycursor.execute(sql, (token, email))
    mydb.commit()

    print(json.dumps({"success": True, "html": data + f"<script>document.cookie = 'token={token}'</script>"}))
except mysql.connector.IntegrityError as err:
    web = """
        <script type="text/javascript">
            console.log("Nie udało sie odświeżyć tabeli")
        </script>"""
    print(json.dumps({"success": False, "html": web}))
