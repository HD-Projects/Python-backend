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
listLen = 0

class email:
  def save():
    print(emails)
    print(names)
    theLists = open("lists.py", "w")
    stringToSave = 'names = ['
    for i in range(len(names)-1):
      stringToSave = stringToSave+'"'+names[i]+'",'
    stringToSave = stringToSave+'"'+names[(len(names)-1)]+'"]\nemails = ['
    i = 1
    for i in range(len(emails)-1):
      stringToSave = stringToSave+'"'+emails[i]+'",'
    stringToSave = stringToSave+'"'+emails[(len(emails)-1)]+'"]'
    theLists.write(str(stringToSave))
    print(stringToSave)
  def loginSMTP():
    provider = input("What provider do you want to use Gmail(G), Outlook(O), Yahoo(Y), AOL(A) \n")
    theirUsername = str(input("What is your username \n"))
    password = str(input("What is your password \n"))
    print("Debug Info: Username, "+  theirUsername+" Password, "+password)
    # Authentication
    try:
       s.starttls()
       print("Debug Info: TLS Worked")
    except:
       print("Debug Info: TLS Failed") 
    try: 
      s.login(str(theirUsername), str(password))
      print("Debug Info: Succesful you are now logged in and can send emails\n\n")
    except:
      print("Debug Info: Login Failed \n\n")
  def addEmail():
    nameInput = str(input("What is the Name you would like to append\n"))
    names.append(nameInput)
    emailInput = str(input("What is the email of the reciver\n"))
    emails.append(emailInput)
    email.save()
  def removeEmail():
    removeName = input("What is the name you want to remove\n")
    listLen = 0
    try:
      listLen = names.index(removeName)
    except:
      print("Debug Info: Failed to find "+removeName+" in list")
    emails.remove(emails[listLen])
    names.remove(names[listLen])
    email.save()
  def sendEmail():
    subject = input("What Is The Subject Of Your Message \n")
    message = input("Message\nDear *[name]*,\n\n")
    index = 0
    i = 0
    for i in range(len(names)):
      index += 1
      if (index > 10):
        index = 0
        s.quit()
        try:
           s.starttls()
           print("Debug Info: TLS Worked")
        except:
           print("Debug Info: TLS Failed") 
        try: 
          s.login(str(theirUsername), str(password))
          print("Debug Info: Succesful you are now logged in and can send emails\n\n")
        except:
          print("Debug Info: Login Failed \n\n")
      msg = MIMEMultipart()       # create a message
      # setup the parameters of the message
      msg['From']=theirUsername
      msg['To']=emails[i]
      msg['Subject']="This is TEST"
      msg.attach(MIMEText("Dear "+names[i]+",\n\n"+message, 'plain'))
      text = msg.as_string()
      s.sendmail("asteroid.dodge.devs@gmail.com", emails[i], text)
      print("Sent, "+text)
      msg = ""
  def choose():
    choice = input("What do you want to do:\n\nAdd An Email from you sending list(A)\nRemove an email from you sending list(R)\nSend an Email(S)\n")
    
    if choice == "A":
      email.addEmail()
      email.choose()
    elif choice == "R":
      email.removeEmail()
      email.choose()
    elif choice == "S":
      email.sendEmail()
      email.choose()
    else:
      print("Debug Info: Session Finnished")

email.loginSMTP()
email.choose()