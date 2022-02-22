#!/home/matball-ssd/Projects/barekbaal_newsletter/venv/bin/python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
import re
from random import seed
from random import randint

class Mejlowanie:
    def __init__(self):
        self.konfiguracje()
        self.main()


    def konfiguracje(self):
        load_dotenv()

   
    def przygotowanie_zawartosci_maila(self):
        print("niech ryczy")
        self.file_csv="./"+"motyw_tygodniowy"+"/"+"fārsī.csv"
        with open(self.file_csv, 'r', encoding="utf-8") as file_csv:
            wszystkie_zapytania=file_csv.read()
        wzor_regeksowy=r'---*'
        lista_zapytan=re.split(wzor_regeksowy,wszystkie_zapytania)
        print(lista_zapytan)
        self.losowanie(lista_zapytan)
        self.mail_content=lista_zapytan[self.wylosowany]


    def losowanie(self, lista_zapytan):
        seed(1)
        self.wylosowany=randint(1,len(lista_zapytan)-1)
        print(self.wylosowany)


    def main(self):
        self.przygotowanie_zawartosci_maila()
        #The mail addresses and password
        self.sender_address = os.getenv('SENDER_ADDRESS')
        self.sender_pass = os.getenv('SENDER_PASS')
        self.receiver_address = os.getenv('RECEIVER_ADDRESS')
        self.wysylanie()


    def wysylanie(self):
        #Setup the MIME
        self.message = MIMEMultipart()
        self.message['From'] = self.sender_address
        self.message['To'] = self.receiver_address
        self.message['Subject'] = self.mail_content.split('\n', 2)[1] #The subject line
        print("ahoj" + str(self.message['Subject']))
        #The body and the attachments for the mail
        self.message.attach(MIMEText(self.mail_content, 'plain'))#, "UTF-8"))
        #Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(self.sender_address, self.sender_pass) #login with mail_id and password
        print("self.message")
        #print(str(self.message))
        text = self.message.as_string()
        session.sendmail(self.sender_address, self.receiver_address, text)
        session.quit()
        print('Mejl wysłany')


if __name__ == "__main__":
    mejlowanie=Mejlowanie()