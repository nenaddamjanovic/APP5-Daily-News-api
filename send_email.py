import smtplib
import ssl
import os


def send_mail(message):
    host = "smtp.gmail.com"
    port = 465
    username = "informaticarmreze@gmail.com"
    # Dobija password iz env fajla windowsa
    password = os.getenv("PASSWORD_GMAIL")  # password = "zytr epbx ofor chps"
    receiver = "informaticarmreze@gmail.com"

    sslcontext = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=sslcontext) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

