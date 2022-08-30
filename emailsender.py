from http import server
import smtplib

to = input("Enter the recipient email\n")

content = input(" enter the content to your email")

subject = input(" enter the subject")

def sendEmail(to , content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login('bsrabdulsamad@gmail.com', "123@rgt.co   m")
    server.sendmail("abssamad505@gmail.com",to , content)
    server.close()

sendmail(to , content)