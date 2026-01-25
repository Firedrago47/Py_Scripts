import smtplib
import subprocess

from_email = ""
to_email = ""
passwd = ""


def send_mail(from_email, to_email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(from_email, password)
    server.sendmail(from_email, to_email, message)
    server.quit()


com = "ls"

msg = subprocess.check_output(com, shell=True)

# respected functions and data to mail can written further

send_mail(from_email, to_email, passwd, msg)
