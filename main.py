import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import  Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Adie Chris'
email['to'] = 'adiec7@gmail.com'
email['subject'] = 'Enquiries for company registration'

email.set_content(html.substitute(name='Chris'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('karisoft23@gmail.com', 'adiec23guy')
    smtp.send_message(email)
    print('all done boss !')
