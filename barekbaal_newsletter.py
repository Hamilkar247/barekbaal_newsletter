#!/home/matball-ssd/Projects/barekbaal_newsletter/venv/bin/python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv


def konfiguracje():
    load_dotenv()


def wysylanie(sender_address, sender_pass, receiver_address, mail_content):
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'semper - zawsze, et - i, ego - ja '   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mejl wysłany')


def main():
    konfiguracje()
    mail_content = '''onerāria

ōlim una nāvis solvit vela
eī ‘olla theāria’ nōmen erat
aurae flābat ut prōram mergere 
facite iter scītē

mox adsit onerāria,
theam, rhomium, sacchara,
afferat et post sectūram
in ōtium ībimus

post parvōs diēs in mare altō
navem appāruit bālaena
exin navarchus dedit jūra
fuiss’ opus cetum ductū

sunt caesī ratēs magnā pugnā
quia bālaen’ ē altā undā
eīs damnum dabat caudā suā 
sīc cēpit jaculī vulnus 

nāvarchō, līneā vexatīs,
cētāriī vidēbantur fātus
sīc rīdet mens nunquam avārīs
enim remulcum manet

remīsit cetī mersiōne
remulcum in secūtiōne
sed manet pugna usque ā hāc hōrā
(usqu’ ‘ac ‘ora)
nītuntur in gressiōne

quātenus sciō, superest pugna,
jam vēnāns cētus, remulcum
dūrat,
ab onerāriā spēs aguntur
nāvarchō, gregī, omnibus

mox adsit onerāria,
theam, rhomium, sacchara,
afferat et post sectūram
in ōtium ībimus
    '''
    #The mail addresses and password
    sender_address = os.getenv('SENDER_ADDRESS')
    sender_pass = os.getenv('SENDER_PASS')
    receiver_address = os.getenv('RECEIVER_ADDRESS')
    wysylanie(sender_address, sender_pass, receiver_address, mail_content)


if __name__ == "__main__":
    main()