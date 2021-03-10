# author: Egehan Asal

import codecs
from twilio.rest import Client
import datetime

# Student list
students = ['ONUR AKKAYA', 'SEYFULLAH ALTIN', 'ALİ EMİR ALTIN', 'MERTCAN ARSLAN', 'UMUT AYDIN', 'HİKMETCAN AYTEMÜR',
            'MEHMET BAHADIR BAĞ', 'NADA BOUKHARI', 'MİTHATCAN CENGİZ', 'ARDA CEYLAN', 'ELİF ÇOLAK', 'AHMET DEMİR',
            'EKİN ERDEM EKİNCİ', 'ÜMİT BORA GÜNAYDIN', 'ABDURRAHMAN GÜNDÜZLÜ',
            'MIRHASAN HAJI HASANLI', 'OĞUZHAN İÇELLİLER', 'EMRE İLHAN', 'EREN UTKU KARATAŞ', 'TAHA EREN KELEŞ',
            'GÖKTUĞ KESKİ', 'YAHYA KOYUNCU', 'MEHMET İHSAN KÜPELİKILINÇ', 'BARIŞ CEM ÖZTÜRK', 'METEHAN RECBER',
            'İREM TUĞBA SAĞSÖZ', 'ALP ŞAHİN', 'BARIŞ CAN SARIAHMETOĞLU', 'SADIK SEZGİN', 'CEM SÖZEN', 'BEYZA TAPAN',
            'FATMA TUĞÇE TERZİ', 'NEVZAT OĞUZHAN TOPUZ', 'MEHMETHAN TURAN', 'ALPER TURUNÇ', 'MAHMUT YUSUF ÜNGÖR',
            'BEGÜM YILDIRIM']

here = list()

for line in codecs.open("C:\\Users\\user\\Desktop\\cse101_attendance.txt", encoding="utf8"):
    if len(line[:-9]) and line[:-9] in students:
        here.append(line[:-9])

not_attended = list(set(students).difference(here))

# Phone number that you'll get from twilio
from_whatsapp_number = 'whatsapp:+14155238886'
# Your phone number
to_whatsapp_number = 'whatsapp:+905063078720'

# Your Account SID from twilio
account_sid = "ACa7c044ec3c07b830f6ca0461d12df001"
# Your Auth Token from twilio
auth_token = "0a5914b51b5889167e4692939ca8d034"

client = Client(account_sid, auth_token)

date = datetime.date.today()
report = "Tarih: " + str(date) + "\nKatılımcı sayısı: " + str(len(here)) + "\n\nDerse Katılmayan Öğrenciler:\n"
for i in range(len(not_attended)):
    report += "-"+not_attended[i].title() + "\n"

client.messages.create(body=report, from_=from_whatsapp_number, to=to_whatsapp_number)
