import time
import smtplib
try:
    gmail_user='dbhavale6767@gmail.com'
    gmail_password='dbhavale4831'

    send_from = gmail_user
    to=['dbhavale4831@outlook.com']
    email='Hello Deepak!' \
          'How are You ?'
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    server.login(gmail_user,gmail_password)
    server.sendmail(send_from,to,email)
    server.close()

    print('Mail Sent Successully')

except Exception as e:
    print(e)


