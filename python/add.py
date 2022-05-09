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
    cipher = AES.new(bytes.fromhex(config.key_pass), AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(password.encode("utf-8"), AES.block_size))
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    return ct, iv


def getData(validate: bool):
    form = cgi.FieldStorage()

    zast = form.getvalue("zast")
    password = form.getvalue("pass")
    x = form.getvalue("share")
    if x is None:
        share = ''
    else:
        share = str(x).replace("\r", "")

    if x is None:
        share = ''

    email = os.environ.get('HTTP_COOKIE').split("=")[1]

    if validate:
        if not vld.validateEmailList(share) or not vld.validatePassword(password) or \
                vld.validateOther(zast):
            return email, '', '', ''

    share = share.rstrip() + "\n"

    password, iv = getCipher(password)

    return email, (zast, password, iv, share.replace("\n", ";"))


token, validatedData = getData(validate=True)

if '' not in validatedData[:-1]:
    mycursor = mydb.cursor()
    try:
        sql = "SELECT email FROM users WHERE user_token = %s"
        mycursor.execute(sql, (token,))
        x = mycursor.fetchall()
        if len(x) == 1:
            sql = "INSERT INTO users_data (email, site, password, iv, allowed) VALUES (%s, %s, %s, %s, %s)"
            mycursor.execute(sql, (x[0][0], validatedData[0], validatedData[1], validatedData[2], validatedData[3],))
            data = gd.getData(mycursor, True, False, token)
        else:
            data = "<tr><td>Not this time!</td></tr>"
        token1 = get_random_bytes(128).hex()
        sql = "UPDATE users SET user_token = %s WHERE user_token = %s"
        mycursor.execute(sql, (token1, token))

        mydb.commit()

        print(json.dumps({"success": True, "html": data + f"<script>document.cookie = 'token={token1}'</script>"}))
    except mysql.connector.IntegrityError as err:
        web = """
        <script type="text/javascript">
            <alert>Wystąpił nieoczekiwany błąd. Proszę spróbować później</alert>
        </script>"""
        print(json.dumps({"success": False, "html": web}))
