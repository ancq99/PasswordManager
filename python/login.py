#! C:/Users/anczo/AppData/Local/Programs/Python/Python38-32/python.exe
# -*- coding: utf-8 -*-

import cgi
import hashlib
import json
import os
import time
from datetime import timedelta, datetime

import mysql.connector
from Crypto.Random import get_random_bytes

import getData as gd
import htmlCodes as html
import sendMail as sM
import validate as vld
import config


mydb = mysql.connector.connect(
    host="localhost",
    user="login",
    password="h6/fEJK4akpelnA7",
    database="projekt"
)

print("Content-Type: application/json")
print()


def getData(validate: bool):
    form = cgi.FieldStorage()

    email = form.getvalue("email")
    password = form.getvalue("password")

    if validate:
        if not vld.validateEmail(email) or not vld.validatePassword(password):
            return '', ''

    return email, password


ip = str(os.environ["REMOTE_ADDR"])
validatedData = getData(validate=True)
time.sleep(3)
if '' not in validatedData:
    mycursor = mydb.cursor()
    try:
        sql = "SELECT email FROM users WHERE email LIKE %s"
        mycursor.execute(sql, (validatedData[0],))
        x = mycursor.fetchall()

        if len(x) == 1:
            sql = "SELECT connections FROM users WHERE connections LIKE %s AND email LIKE %s"
            mycursor.execute(sql, ("%" + ip + "%", validatedData[0]))
            x = mycursor.fetchall()

            if len(x) == 1:
                sql = "SELECT error_login_number, last_error_timestamp FROM users WHERE `email` LIKE %s"
                mycursor.execute(sql, (validatedData[0],))
                x = mycursor.fetchall()
                if x is not None:
                    count = x[0][0]
                    timestamp = x[0][1]

                    if count < 5:
                        sql = "SELECT `hash`, `salt` FROM `auth` WHERE `email` LIKE %s"
                        mycursor.execute(sql, (validatedData[0],))

                        x = mycursor.fetchall()

                        dbHash = x[0][0]
                        salt = x[0][1]
                        pepper = config.pepper

                        key = hashlib.pbkdf2_hmac('sha256', bytes.fromhex(pepper) + validatedData[1].encode('utf-8'), bytes.fromhex(salt), 100000, dklen=256)

                        if key == bytes.fromhex(dbHash):
                            token = get_random_bytes(128).hex()
                            sql = "UPDATE users SET error_login_number = 0, user_token = %s WHERE `email` LIKE %s"
                            mycursor.execute(sql, (token, validatedData[0]))

                            userData, shareData = gd.getData(mycursor, True, True, token)
                            sql = "SELECT name, surname FROM users WHERE `email` LIKE %s"
                            mycursor.execute(sql, (validatedData[0],))
                            x = mycursor.fetchall()

                            website = html.main.format(userData, shareData) + "<script>document.cookie = 'token="+token+"';$('#modal_shared').popover({" \
                                     "trigger:'focus'}); $(" \
                                     "'#modal_shared1').popover({" \
                                     "trigger:'focus'}); $(" \
                                     "'#user_name').html('Zalogowany " \
                                     "użytkownik: " + x[0][0] + " " + x[0][1] + "'); \
                                      $('#user_ip').html('Adres ip: " + str(os.environ['REMOTE_ADDR']) + "'); </script> "
                            test = {'success': True, 'htmlData': website}

                            print(json.dumps(test, indent=1))


                        else:
                            sql = "UPDATE users SET error_login_number = error_login_number + 1, last_error_timestamp = NOW()  WHERE `email` LIKE %s"
                            mycursor.execute(sql, (validatedData[0],))

                            print(json.dumps({'success': False, "htmlData": "Błędne dane logowania"}))
                    else:
                        sql = "UPDATE users SET last_error_timestamp = NOW() WHERE `email` LIKE %s"
                        mycursor.execute(sql, (validatedData[0],))

                        web = "Błędne dane logowania <script type=\"text/javascript\">"
                        web += "$(\"#alertMsg\").html(\"Przekroczono ilość nieudanych prób logowania! Konto zostało zablokowane na 15 minut. Każda próba zalogowania w tym czasie resetuje odmierzany czas. Ponowne zalogowanie możliwe o " + (
                                    datetime.now() + timedelta(minutes=15)).strftime("%Y-%m-%d %H:%M:%S") + "\");"
                        web += "$(\".alert\").slideDown(400);"
                        web += "</script> "
                        print(json.dumps({'success': False, 'htmlData': web}))
                else:
                    print(json.dumps({'success': False, "htmlData": "Błędne dane logowania"}))
            else:
                web = "Nowe połączenie  <script type=\"text/javascript\">"
                web += "$(\"#alertMsg\").html(\"Zablokowno połączenie z nowego adresu IP. W celu zalogowania się, potwierdź ten adres w wysłanym do Ciebie mailu. Link jest ważny 24 godziny\");"
                web += "$(\".alert\").slideDown(400);"
                web += "</script> "
                print(json.dumps({'success': False, 'htmlData': web}))
                token = get_random_bytes(128).hex()
                link = "https://passwordmng.project/python/confirmIp.py?token={}".format(token + "_" + ip)
                sql = "UPDATE `users` SET new_connection_token = %s, connection_token_timestamp = NOW() WHERE email LIKE %s"
                mycursor.execute(sql, (token + "_" + ip, validatedData[0]))

                email_text = """
                Subject: New Connection Attempt
    
                
                Wykryto próbę połączenia z nowego adresu IP: {}. Jeśli to nie Ty, zignoruj tą wiadomość. W przeciwnym przypadku, potwierdź ten adres klikając w poniższy link.
                
        
                {}
                """

                sM.send(validatedData[0], email_text.format(ip, link))
        else:
            web = """Nie udało się zalogować."""

            print(json.dumps({"success": False, "htmlData": web}))
        mydb.commit()

    except mysql.connector.IntegrityError as err:
        web = """Nie udało się zalogować."""

        print(json.dumps({"success": False, "htmlData": web}))
