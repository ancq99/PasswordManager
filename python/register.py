#! C:/Users/anczo/AppData/Local/Programs/Python/Python38-32/python.exe -u
# -*- coding: utf-8 -*-

import cgi
import hashlib
import os

import mysql.connector

import htmlCodes as html
import validate as vld
import config
print("Content-type: text/html; charset=UTF-8")
print()

mydb = mysql.connector.connect(
    host="localhost",
    user="register",
    password="!Ayv_Dvp9d95sGR0",
    database="projekt"
)


def getData(validate: bool):
    form = cgi.FieldStorage()

    name = form.getvalue("name")
    surname = form.getvalue("surname")
    email = form.getvalue("email")
    password = form.getvalue("password")
    question = form.getvalue("question")
    answer = form.getvalue("answer")

    if validate:
        if not vld.validateEmail(email) or not vld.validatePassword(password) or \
                vld.validateOther(name) or vld.validateOther(surname) or vld.validateOther(answer) or question == 0:
            return '', '', '', '', '', ''

    return (name, surname, email, question, answer, str(os.environ["REMOTE_ADDR"]) + ";"), password


validatedData, password = getData(validate=True)

if '' not in validatedData:
    mycursor = mydb.cursor()
    try:
        sql = "INSERT INTO users (name, surname, email, question, answer, connections) VALUES (%s, %s, %s, %s, %s, %s)"
        mycursor.execute(sql, validatedData)

        sql = "INSERT INTO auth (email, hash, salt) VALUES (%s, %s, %s)"
        salt = os.urandom(64)
        key = hashlib.pbkdf2_hmac('sha256', bytes.fromhex(config.pepper) + password.encode('utf-8'), salt, 100000, dklen=256)
        val = (validatedData[2], key.hex(), salt.hex())
        mycursor.execute(sql, val)

        mydb.commit()
        web = """
                <span>Udało się utworzyć konto użytkownika, przekierowanie nastąpi za 5 sekund.</span> <br>
                <i class="fa fa-circle-o-notch fa-spin"></i>
                <script type="text/javascript">
                    setTimeout(function() {
                      location.href = '../index.html'    
                  }, 5000);

                </script>"""
        print(html.error.format(web))
    except mysql.connector.IntegrityError as err:
        web = """
        <span>Nie udało się utworzyć konta, przekierowanie nastąpi za 5 sekund.</span> <br>
        <i class="fa fa-circle-o-notch fa-spin"></i>
        <script type="text/javascript">
            setTimeout(function() {
              history.back();    
          }, 5000);
              
        </script>"""
        print(html.error.format(web))
