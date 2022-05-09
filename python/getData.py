import os
from base64 import b64decode

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import unpad
import config


def decodeCiphher(iv, ct):
    cipher = AES.new(bytes.fromhex(config.key_pass), AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt


def getUserData(fetch):
    data = ""
    ctr = 1

    for row in fetch:
        password = decodeCiphher(b64decode(row[2]), b64decode(row[1])).decode('utf-8')

        tmp = str(row[3]).replace(";", "\n")
        data += f"""<tr><td>{ctr}</td><td>{row[0]}</td><td>
        <div class="input-group">
            <input type='password' class='td_pass form-control' value='{password}' data-toggle="password" style="text-align:center;" readonly>
            <div class="input-group-append">
            <span class="input-group-text td_pass">
                <i class="fa fa-eye-slash"></i>
            </span>
            </div>
        </div>
        </td>
        <td>{tmp}</td><td><button class=\"btn btn-success btn-sm float-middle\" type=\"button\">Edytuj</button></td></tr> """

        ctr += 1
    return data.replace(";", "\n")


def getSharedData(fetch):
    data = ""
    ctr = 1
    for row in fetch:
        password = decodeCiphher(b64decode(row[3]), b64decode(row[2])).decode('utf-8')

        data += f"""<tr><td>{ctr}</td><td>{row[0]}</td><td>{row[1]}</td>
        <td>
        <div class="input-group">
            <input type='password' class='td_pass form-control' value='{password}' data-toggle="password" style="text-align:center;" readonly>
            <div class="input-group-append">
            <span class="input-group-text td_pass">
                <i class="fa fa-eye-slash"></i>
            </span>
            </div>
        </div>
        </td></tr>"""
        ctr += 1
    return data


def getData(mycursor, user: bool, share: bool, token=None):
    if token is None:
        email = os.environ.get('HTTP_COOKIE').split("=")[1]
    else:
        email = token

    userData = ""
    shareData = ""

    if user:
        sql = "SELECT d.site, d.password, d.iv, d.allowed FROM users_data AS d JOIN users as u ON d.email = u.email WHERE u.user_token LIKE %s"
        mycursor.execute(sql, (email,))
        userData = getUserData(mycursor.fetchall())

    if share:
        sql = "SELECT email FROM users WHERE user_token LIKE %s"
        mycursor.execute(sql, (email,))
        x = mycursor.fetchall()
        if len(x) == 1:
            sql = "SELECT email, site, password, iv FROM users_data WHERE allowed LIKE %s AND email NOT LIKE %s; "
            mycursor.execute(sql, ('%'+x[0][0]+'%', x[0][0]))
            shareData = getSharedData(mycursor.fetchall())
        else:
            shareData = "Nie tym razem"

    if user and share:
        return userData, shareData
    elif user and not share:
        return userData
    elif not user and share:
        return shareData
    else:
        return None
