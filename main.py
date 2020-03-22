import smtplib
import ssl
ThatFile = open("lists.py", "a")
ThatFile.close()
from lists import *
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

context = ssl.create_default_context()
s = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context)

username = ""
password = ""
interactionCount = "0"
name = ""
theirUsername = ""

listLen = 0
login = 0 

class email:
  interactionCount = "0"
  def DI(DebugLog):
    print("Debug Info: "+DebugLog)
    debugFile = open("debug.txt","a")
    debugFile.write("\nDebug Info: "+DebugLog)
    debugFile.close
  def save():
    email.DI("Names:"+str(names))
    email.DI("Emails:"+str(emails))
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
    email.DI("Saved String: \n"+stringToSave)
  def loginSMTP():
    theirUsername = str(input("What is your Gmail account Email address? \n"))
    password = str(input("What is your Gmail password?\n"))
    email.DI("Debug Info: Username, "+  theirUsername+" Password, "+password)
    try: 
      s.login(str(theirUsername), str(password))
      login = 1
      print("Debug Info: Succesful you are now logged in and can send emails\n\n")
    except:
      print("Debug Info: Login Failed \nReenter your credentials\n or turn on less secure app access in your gmail account settings\n\n")
      login = 0
  def addEmail():
    nameInput = str(input("What is the Name you would like to add to the name list\n"))
    names.append(nameInput)
    emailInput = str(input("What is the email of the reciver\n"))
    emails.append(emailInput)
    email.save()
    email.DI("Added Email: "+emailInput+"Name: "+nameInput)
  def removeEmail():
    removeName = input("What is the name you want to remove\n")
    listLen = 0
    try:
      listLen = names.index(removeName)
    except:
      email.DI("Failed to find "+removeName+" in list")
    emails.remove(emails[listLen])
    names.remove(names[listLen])
    email.save()
  def sendEmail():
    subject = input("What Is The Subject Of Your Message \n")
    sendingName = input("What do you want your name to show as\n")
    html = input("Do you want to send html content(Y/N) \n")
    index = 0
    if html.lower() == "y":
      htmlFile = str(input("Make sure the file is in the same folder as the .EXE or .PY file\nWhat is the name of the file\n"))
      htmlFileOpened = open(htmlFile,"r")
      htmlContent = htmlFileOpened.read()
      for i in range(len(names)):
        index += 1
        if (index > 10):
          index = 0
          s.quit()
          try: 
            s.login(str(theirUsername), str(password))
            email.DI("Succesful you are now logged in and can send emails\n\n")
          except:
            email.DI("Login Failed \n\n")
        msg = MIMEMultipart()       # create a message
        # setup the parameters of the message
        msg['From']=sendingName
        msg['To']=emails[i]
        msg['Subject']=subject
        msg.attach(MIMEText(htmlContent, "html"))
        text = msg.as_string()
        s.sendmail(theirUsername, emails[i], text)
        print("\n\nSent, "+text)
        msg = ""
    else:
      textFile = input("Do you have a .TXT file you want to add from(Y/N)\n")
      if textFile.lower() == "y":
        textFileName = str(input("What is the text files name\nMake sure it is in the same folder as the .EXE or .PY file\nWill write Dear, *[Name]*\n"))
        try:
          textFileOpened = open(textFileName, "r")
          message = textFileOpened.read()
          textFileOpened.close()
          email.DI("File Opened")
        except:
          email.DI("File did not work")
          return 0
      else:
        message = input("Message\nDear *[name]*,\n\n")
        nameOfSender = input("What is the name you would like at the end of your email?\n")
        title = input("What is your title (Dr. , Sir , Esquire)\n")
      for i in range(len(names)):
        index += 1
        if (index > 10):
          index = 0
          s.quit()
          try: 
            s.login(str(theirUsername), str(password))
            email.DI("Succesful you are now logged in and can send emails\n\n")
          except:
            email.DI("Login Failed \n\n")
        msg = MIMEMultipart()       # create a message
        # setup the parameters of the message
        msg['From']=sendingName
        msg['To']=emails[i]
        msg['Subject']=subject
        msg.attach(MIMEText("Dear "+names[i]+",\n\n"+str(message)+"\n\n"+signature, 'plain'))
        text = msg.as_string()
        s.sendmail(theirUsername, emails[i], text)
        print("\n\nSent, "+text)
        msg = ""
  def sendDebugInfo():
    debugInfoRead = open("debug.txt","r")
    sendDebugInfo = debugInfoRead.read()
    debugInfoRead.close()
    msg = MIMEMultipart()       # create a message
    # setup the parameters of the message
    msg['From']=theirUsername
    msg['To']="debug.info.python.backend@gmail.com"
    msg['Subject']="Sending Debug info from "+theirUsername
    msg.attach(MIMEText(str(sendDebugInfo), 'plain'))
    text = msg.as_string()
    try:
      s.sendmail(theirUsername, "debug.info.python.backend@gmail.com", text)
    except:
      print("Sending Debug Info Failed\nTry to login\n")
  def choose():
    interactionCount = 0
    inputString = "What do you want to do:\n\nAdd An Email from you sending list(A)\nRemove an email from you sending list(R)\nSend an Email(S)\nLogin or change accounts(L)\nSend debug info (D)\n"
    choice = input(inputString)
    email.DI("Interaction #"+str(interactionCount)+" Choice of choice string "+choice)
    if choice.lower() == "D":
      email.DI("Interaction #"+str(interactionCount)+" Sending Debug Info!")
      email.sendDebugInfo()
      email.choose()
    elif choice.lower() == "a":
      email.DI("Interaction #"+str(interactionCount)+" Adding Email")
      emailChoice = input("Do you want to upload a txt file with your contacts in it (a) or enter recivers manually(B)")
      if emailChoice.lower() == "b":
        email.DI("Interaction #"+str(interactionCount)+" Manually Inputing emails")
        email.addEmail()
        email.choose()
      elif emailChoice.lower() == "a":
        email.DI("Interaction #"+str(interactionCount)+" Adding File")
        fileNameEmail = input("what is the name of the file of emails") 
        print("rename the file of emails to fileOfEmails.csv or fileOfEmails.txt depending on the formant")
        fileOfEmails = open(fileNameEmail, "r")
        print("rename the file to fileOfNames.csv or fileOfNames.txt depending on the format")
        fileNameName = input("what is the name of the file of names") 
        fileOfNames = open(fileNameName, "r")
        
        if fileOfEmails == "fileOfEmails.csv":
          reader = csv.reader(fileOfEmails)
          next(reader) #skips header
          for r in reader:
            r = email
            emails.append(email)
            emails.save()

        elif fileOfEmails == "filesOfEmails.txt":
         for line in fileOfEmails:
          line = email
          emails.append(email)
          emails.save()

        else:
          print("there was an error try again ")

        if fileOfNames == "fileOfNames.txt":
          for line in fileOfNames:
            line = name
            names.append(name)
            names.save()


        elif fileOfNames == "fileOfNames.csv":
          reader = csv.reader(fileOfNames)
          next(reader) #skips header
          for r in reader:
            r = name
            names.append(name)
            names.save(name)     
        
        else:
          print("there was an error, try again")
    elif choice.lower() == "r":
      email.DI("Interaction #"+str(interactionCount)+" Remove Email")
      email.removeEmail()
      email.choose()
    elif choice.lower() == "s":
      email.DI("Interaction #"+str(interactionCount)+" Sending Email")
      email.sendEmail()
      email.choose()
    elif choice.lower() == "l":
      email.DI("Interaction #"+str(interactionCount)+" Reloging in")
      email.loginSMTP()
      email.choose()
    else:
      email.DI("Session Finished, all personal information deleting...\n\n\n\n")
      email.sendDebugInfo()
      theirUsername = ""
      password = ""
      print("All personal information has been deleted")



try:
  if names[0] == names[0]:
    names = names
    emails = emails
except:
  names = ["Alex", "Riley","Alex"]
  emails = ["adickhans@gmail.com","rilesdk@gmail.com","dickha.alexan27@svvsd.org"]
  email.save()

interactionCount = 0
email.loginSMTP()
email.choose()