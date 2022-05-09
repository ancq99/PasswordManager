import smtplib

gmail_user = 'noreply.passmng.project@gmail.com'
gmail_password = 'Bz5u8AMHiMrf4bf'


def send(send_to, msg):
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.ehlo()  # Can be omitted
        server.starttls()
        server.ehlo()  # Can be omitted
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, send_to, msg.encode('utf-8'))
        server.close()
