#! C:/Users/anczo/AppData/Local/Programs/Python/Python38-32/python.exe
# -*- coding: utf-8 -*-

import cgi

import mysql.connector

import htmlCodes as html

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
    token = form.getvalue("token")
    return token


token = getData()

mycursor = mydb.cursor()
try:
    sql = "SELECT u.email FROM auth AS a JOIN users AS u WHERE u.token LIKE %s"
    mycursor.execute(sql, (token,))
    x = mycursor.fetchone()

    if x is not None:
        print(html.passReset)
    else:
        print("Błędny token")

except mysql.connector.IntegrityError as err:
    web = """
            <span>Nie udało się połączyć z bazą danych. Spróbuj później lub skontaktuj się z administratorem.</span> <br>
             <i class="fa fa-circle-o-notch fa-spin"></i>
             <script type="text/javascript">
             setTimeout(function() {
             history.back();    
             }, 5000);

             </script>"""

    print(web)
