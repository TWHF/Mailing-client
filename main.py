import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com', 25)

server.ehlo()

server.login('nutty1029butty@gmail.com','itsnutty123')

msg = MIMEMultipart()
msg['From'] = 'ItsTWHF'
msg['To'] = '18103123@mail.jiit.ac.in'
msg['Subject'] = 'Just a Test'

with open('message.text','r') as f:
    message = f.read()

msg.attach(MIMEText(message,'plain'))

filename = 'jojo.jpg'
attachment = open(filename, 'rb')

p = MIMEBase('application','octet.stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content.Dispostion',f'attachment; filename={filename}')
msg.attach(p)
text = msg.as_string()
server.sendmail('nutty1029butty@gmail.com','18103123@mail.jiit.ac.in',text)


