# author: Egehan Asal

import codecs
from twilio.rest import Client
import datetime

# Student list
students = []

here = list()

for line in codecs.open("attendance.txt", encoding="utf8"):
    # To get rid of the hour at the end of the name -> line[:-9]
    line_upper = line[:-9].upper()
    if line_upper in students and line_upper not in here:
        here.append(line_upper)

not_attended = list(set(students).difference(here))

# Phone number that you'll get from twilio
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
for i in range(len(not_attended)):
    report += "-"+not_attended[i].title() + "\n"

client.messages.create(body=report, from_=from_whatsapp_number, to=to_whatsapp_number)
