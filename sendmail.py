from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

def sendmail(login, senha, corpo:str, sender):
    
    msg = MIMEMultipart()
    msg.attach(MIMEText(corpo,'html'))

    #enviar para:
    emails = 'guilherme.of.fernandes@gmail.com, carlosbutinhoni@gmail.com'

    #email em si
    msg['Subject'] = 'Nova publicação no edital do IFMT'
    msg['From'] = sender
    msg['To'] = emails 
    with smtplib.SMTP('smtp.mailgun.org', 587) as smtp_server:
        smtp_server.starttls()
        smtp_server.login(login,senha)
        smtp_server.sendmail(sender, emails.split(','),msg.as_string())
    print('enviado')
