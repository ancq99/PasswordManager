#! C:/Users/anczo/AppData/Local/Programs/Python/Python38-32/python.exe
# -*- coding: utf-8 -*-

import cgi
import json
import os
from base64 import b64encode

import mysql.connector
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
import config
import getData as gd
import validate as vld

print("Content-Type: application/json")
print()

mydb = mysql.connector.connect(
    host="localhost",
    user="change",
    password="lJHZk(95.Sx.]Ash",
    database="projekt"
)


def getCipher(password):
    key = bytes.fromhex(config.key_pass)
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(password.encode("utf-8"), AES.block_size))
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    return ct, iv


def getData(validate: bool):
    form = cgi.FieldStorage()

    zast = form.getvalue("zast_new")
    password = form.getvalue("pass_new")
    x = form.getvalue("share_new")
    if x is None:
        share = ''
    else:
        share = str(x).replace("\r", "")

    zast_old = form.getvalue("zast")
    password_old = form.getvalue("pass")
    x_old = form.getvalue("share")

    if x_old is None:
        share_old = ''
    else:
        share_old = str(x_old).replace("\r", "")

    email = os.environ.get('HTTP_COOKIE').split("=")[1]

    if validate:
        if not vld.validateEmailList(share) or not vld.validatePassword(password) or \
                vld.validateOther(zast):
            return '', '', ''
    share = share.rstrip() + "\n"

    password, iv = getCipher(password)

    return zast, password, iv, share.replace("\n", ";"), email, zast_old, share_old.replace("\n", ";")


validatedData = getData(validate=True)

if '' not in validatedData[:-1]:
    mycursor = mydb.cursor()
    try:
        sql = "SELECT email FROM users WHERE user_token = %s"
        mycursor.execute(sql, (validatedData[4],))
        x = mycursor.fetchall()
        if len(x) == 1:
            sql = "UPDATE `users_data` SET `site`= %s,`password`= %s, `iv` = %s, `allowed`= %s " \
                  "WHERE email LIKE %s AND site LIKE %s AND allowed LIKE %s"
            val = (validatedData[0], validatedData[1], validatedData[2], validatedData[3], x[0][0], validatedData[5], validatedData[6])
            mycursor.execute(sql, val)

        token = get_random_bytes(128).hex()
        data = gd.getData(mycursor, True, False, validatedData[4])

        sql = "UPDATE users SET user_token = %s WHERE user_token LIKE %s"
        mycursor.execute(sql, (token, validatedData[4]))
        mydb.commit()
        print(json.dumps({"success": True, "html": data + f"<script>document.cookie = 'token={token}'</script>"}))
    except mysql.connector.IntegrityError as err:
        web = """
                <script type="text/javascript">
                    alert("Nie udało sie edytować danych. Proszę spróbować ponownie!")
                </script>"""
        print(json.dumps({"success": False, "html": web}))
