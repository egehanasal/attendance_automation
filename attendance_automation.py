# author: Egehan Asal

import codecs
from twilio.rest import Client
import datetime

students = []

here = list()

for line in codecs.open("attendance.txt", encoding="utf8"):
    if len(line[:-9]):
        here.append(line[:-9])

print(len(here))
new_list = list(set(students).difference(here))

# Number that you'll get from twilio
from_whatsapp_number = 'whatsapp:+'
# Your phone number
to_whatsapp_number = 'whatsapp:+'

# Your Account SID from twilio
account_sid = ""
# Your Auth Token from twilio
auth_token = ""

client = Client(account_sid, auth_token)

date = datetime.date.today()
report = "Tarih: " + str(date) + "\nKatılımcı sayısı: " + str(len(here)) + "\n\nDerse Katılmayan Öğrenciler:\n"
for i in range(len(new_list)):
    report += "-"+new_list[i].title() + "\n"

client.messages.create(body=report, from_=from_whatsapp_number, to=to_whatsapp_number)
