import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Path('index.html').read_text()
email = EmailMessage()
email['from'] = 'Andrei Neagoie'
email['to'] = 'andrei@zerotpmastery.io'
email['subject'] = 'you won a thousand dollars!'

email.set_content(html.substitute({'name': 'Tintin', }), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('zerotomastery1@gmail.com', 'helloztmmyoldfriend1')
    smtp.send_message(email)
    print('all good boss!')