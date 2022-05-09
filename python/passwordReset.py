#! C:/Users/anczo/AppData/Local/Programs/Python/Python38-32/python.exe
# -*- coding: utf-8 -*-

import cgi
import json

import mysql.connector
from Crypto.Random import get_random_bytes

import sendMail as sM
import validate as vld

email_text = """
Subject: Password Reset


Została wysłana prośba o zmianę hasła. Poniższy link jest ważny przez 15 minut od jego utworzenia. Jeżeli nic nie zleacałeś/aś, możesz zignorować tą wiadomość!

{}
"""

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

    email = form.getvalue("email")

    if validate:
        if not vld.validateEmail(email):
            return ''

    return email


validatedData = getData(validate=True)
flag = 0

if '' in validatedData:
    mycursor = mydb.cursor()
    try:
        sql = "SELECT email FROM `users` WHERE `email` LIKE %s"
        mycursor.execute(sql, (validatedData,))
        x = mycursor.fetchone()
        if x is not None:

            token = get_random_bytes(128).hex()
            link = "https://passwordmng.project/python/resetPage.py?token={}".format(token)
            sql = "UPDATE `users` SET token = %s, token_timestamp = NOW() WHERE email LIKE %s"
            mycursor.execute(sql, (token, validatedData))

            sM.send(validatedData, email_text.format(link))

            web = """
                    <span>Na podany adres email została wysłana wiadomość. Link w niej zawarty jest ważny 15 minut.</span> 
                    <br> <br>
                     <i class="fa fa-circle-o-notch fa-spin"></i>
                     <script type="text/javascript">
                     setTimeout(function() {
                        location.href = 'index.html';    
                     }, 5000);

                     </script>"""

            print(json.dumps({"success": True, "html": web}))
        else:
            web = """
                <span>Nie udało się wysłać maila na podony adres. Spróbuj później lub skontaktuj się z administratorem.</span> <br>
                 <i class="fa fa-circle-o-notch fa-spin"></i>
                 <script type="text/javascript">
                 setTimeout(function() {
                 history.back();    
                 }, 5000);

                 </script>"""

            print(json.dumps({"success": False, "html": web}))

        mydb.commit()
    except mysql.connector.IntegrityError as err:
        web = """
            <span>Nie udało się wysłać maila na podony adres. Spróbuj później lub skontaktuj się z administratorem.</span> <br>
             <i class="fa fa-circle-o-notch fa-spin"></i>
             <script type="text/javascript">
             setTimeout(function() {
             history.back();    
             }, 5000);

             </script>"""

        print(json.dumps({"success": False, "html": web}))
