import smtplib
ThatFile = open("lists.py", "a")
ThatFile.close()
from lists import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

s = smtplib.SMTP('smtp.gmail.com', 587) 

username = ""
password = ""

name = ""
theirUsername = ""

l = "smtp.gmail.com"
s = smtplib.SMTP(l, 587)
listLen = 0
login = 0 

try:
  if names[0] == names[0]:
    names = names
    emails = emails
except:
  names = ["Alex", "Riley","Alex"]
  emails = ["adickhans@gmail.com","rilesdk@gmail.com","dickha.alexan27@svvsd.org"]

class email:
  def save():
    print("Debug Info: Names:"+str(names))
    print("Debug Info: Emails:"+str(emails))
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
    print("Debug Info: Saved String: "+stringToSave)
  def loginSMTP():
    theirUsername = str(input("What is your Gmail account Email address? \n"))
    password = str(input("What is your Gmail password?\n"))
    print("Debug Info: Username, "+  theirUsername+" Password, "+password)
    # Authentication
    try:
       s.starttls()
       print("Debug Info: TLS Worked")
    except:
       print("Debug Info: TLS Failed") 
    login = 0
    try: 
      s.login(str(theirUsername), str(password))
      login = 1
      print("Debug Info: Succesful you are now logged in and can send emails\n\n")
    except:
      print("Debug Info: Login Failed \nTry changing you allow less secure app access in your gmail account settings, Or reenter your credentials\n\n")
      login = 0
  def addEmail():
    nameInput = str(input("What is the Name you would like to add to the name list\n"))
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
    nameOfSender = input("What is the name you would like at the end of your email?\n")
    title = input("What is your job title")
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
      msg['Subject']=subject
      msg.attach(MIMEText("Dear "+names[i]+",\n\n"+str(message)+"\n\n"+nameOfSender+"\n"+title, 'plain'))
      text = msg.as_string()
      s.sendmail("asteroid.dodge.devs@gmail.com", emails[i], text)
      print("\n\nSent, "+text)
      msg = ""
  def choose():
    inputString = "What do you want to do:\n\nAdd An Email from you sending list(A)\nRemove an email from you sending list(R)\nSend an Email(S)\nLogin or change accounts(L)\n"
    choice = input(inputString)
    
    if choice.lower() == "a":
      email.addEmail()
      email.choose()
    elif choice.lower() == "r":
      email.removeEmail()
      email.choose()
    elif choice.lower() == "s":
      email.sendEmail()
      email.choose()
    elif choice.lower() == "l":
      email.loginSMTP()
      email.choose()
    else:
      print("Debug Info: Session Finished, all personal information deleting...")
      theirUsername = ""
      password = ""
      print("All personal information has been deleted")

email.loginSMTP()
email.choose()