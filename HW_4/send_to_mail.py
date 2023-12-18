import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os.path import basename


def sendemail():
    fromaddr = 'mara_1002@mail.ru'
    toaddr = 'mara_1002@mail.ru'
    mypass = 'F6sUqmhE2cCr6HZsEKgt'
    reportname = './logs/log.txt'

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = 'Hello from Python'
    text = 'Hello'

    msg.attach(MIMEText(text))

    with open(reportname, 'rb') as f:
        part = MIMEApplication(f.read(), Name=basename(reportname))
        part['Content-Disposition'] = f'attachment; filename="{basename(reportname)}"'
        msg.attach(part)

    # body = "Это тестовое сообщение"
    # msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    server.login(fromaddr, mypass)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()


if __name__ == '__main__':
    sendemail()
