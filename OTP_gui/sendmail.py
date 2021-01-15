import os, math
import random, sys
import smtplib
mailid = sys.argv[1]
digits = '0123456789'
OTP = ""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
msg = 'Your Verificaton for app is '+OTP+' Note... Please enter otp within 2 minutes and 3 attempts, otherwise it becomes invalid'
file2 = open('otp.txt', 'w')
file2.write(OTP)
file2.close()

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login('shaileshsachan1997@gmail.com', 'App pasword')
print(msg)
s.sendmail('your email id', mailid, msg)
os.system('python second_screen.py')