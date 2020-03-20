import smtplib
import json
from lists import *
import cgi
import time
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

listToWrite = ["hi","this","is","a","test"]

print ("Content-type: text/html")

messages = """<html>
<head><title>My first Python CGI app</title></head>
<body>
<p>Hello, 'world'!</p>
</body>
</html>"""

s = smtplib.SMTP('smtp.gmail.com', 587) 

username = ""
password = ""

name = ""
theirUsername = ""

l = "smtp.gmail.com"
s = smtplib.SMTP(l, 587)

class email:
  def save():
    theLists = open("lists.py", "w")
    stringToSave = 'names = ['
    for i in range(len(names)-2):
      stringToSave = stringToSave+'"'+names[i]+'",'
    stringToSave = stringToSave+'"'+names[(len(names)-1)]+'"]\nemails = ['
    i = 1
    for i in range(len(emails)-2):
      stringToSave = stringToSave+'"'+emails[i]+'",'
    stringToSave = stringToSave+'"'+emails[(len(emails)-1)]+'"]'
    theLists.write(stringToSave)
    print(stringToSave)
  def loginSMTP():
    provider = input("What provider do you want to use Gmail(G), Outlook(O), Yahoo(Y), AOL(A) \n")
    #if(provider == "G"):
    #  l = 'smtp.gmail.com'
    #elif(provider == "Y"):
    #  l = 'smtp.mail.yahoo.com'
    #elif(provider == "O"):
    #  l = 'smtp-mail.outlook.com'
    #elif(provider == "A"):
    #  l = 'smtp.aol.com'
    #else:
    #  print("that provider is not supported")
    #s = smtplib.SMTP(l, 587)
    theirUsername = str(input("What is your username \n"))
    password = str(input("What is your password \n"))
    print("Debug Info: Username, "+  username+" Password, "+password)
    # Authentication
    try:
       s.starttls()
       print("Debug Info: TLS Worked")
    except:
       print("Debug Info: TLS Failed") 
    try: 
      s.login(str(theirUsername), str(password))
      print("Succesful you are now logged in and can send emails")
    except:
      print("It did not work")
  def addEmail():
    nameInput = str(input("What is the Name you would like to append\n"))
    names.append(nameInput)
    emailInput = str(input("What is the email of the reciver\n"))
    emails.append(emailInput)
    email.save
  def removeEmail():
    
    listLen = len(emails)-1    
    print("the email", emails(listLen-1), "was removed")
    emails.remove(listLen)
    names.remove(listLen)
    emails.save
    names.save
   
  def sendEmail():
    subject = input("What Is The Subject Of Your Message \n")
    message = input("Message\nDear *[name]*,\n\n")
    i = 0
    for i in range(len(names)):
      msg = MIMEMultipart()       # create a message
      # setup the parameters of the message
      msg['From']=theirUsername
      msg['To']=emails[i]
      msg['Subject']="This is TEST"
      msg.attach(MIMEText("Dear "+names[i]+",\n"+message, 'plain'))
      text = msg.as_string()
      s.sendmail("asteroid.dodge.devs@gmail.com", emails[i], text)
      print("Sent, "+text)
      msg = ""
  def choose():
    choice = input("What do you want to do\nAdd An Emailfrom you sending list(A)\nRemove an email from you sending list(R)\nSend an Email(S)\nStop(F)\n")
    
    if choice == "A":
      email.addEmail()
    elif choice == "R":
      email.removeEmail()
    elif choice == "S":
      email.sendEmail()
    elif choice == "F":
      sys.exit()
    else:
      email.choose()
    email.choose()

email.loginSMTP()
email.choose()