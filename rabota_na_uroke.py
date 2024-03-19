import smtplib, ssl
from email.message import EmailMessage
smtp_server = "smtp.gmail.com"
port = 587
sender_email ="babjakbk.ru@gmail.com"
password = input("Kirjuta oma salsõna ja vajuta enter:")
context = ssl.create_default_context()
msg = EmailMessage()
msg.set_content("Tere tulemast! Olen kirja keha!")
msg['Subject']="Kirja teema"
msg['From']="Devid Babjak"
msg['to']="marina.oleinik@tthk.ee"
with open("Red_Kitty.jpg",'rb') as fpilt:
    pilt=fpilt.read()
    msg.add_attachment(pilt,maintype='image',subtype='jpg')
try:
    server = smtplib.SMTP(smtp_server,port)
    server.starttls(context=context)
    server.login(sender_email, password)
    server.send_message(msg)
    print("Kiri on saatnud")
except Exception as e:
    print(e)
finally:
    server.quit()