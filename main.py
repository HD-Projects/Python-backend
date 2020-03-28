


#U&(9rB4IflE
import smtplib
import ssl
ThatFile = open("lists.py", "a")#BeautifulSoup
ThatFile.close()
from termcolor import cprint
from lists import *
import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import mimetypes
import email.mime.application
import imaplib
import imaplib as mail
import email
mail = imaplib.IMAP4_SSL("imap.gmail.com")
import bs4

context = ssl.create_default_context()
s = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context)

username = ""
password = ""
interactionCounts = 0
name = ""
theirUsername = ""
debugLogNum = 0

listLen = 0
login = 0 

class email:
  interactionCounts = 0
  def DI(DebugLog):
    global debugLogEnabled
    global debugLogNum
    if(debugLogEnabled == 1):
<<<<<<< HEAD
      cprint("Debug Info: "+DebugLog,"green")
=======
      debugLogNum += 1
      print(str(debugLogNum) + ": Debug Info: "+DebugLog)
>>>>>>> origin/master
    else:
      debugLogNum += 1
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
    stringToSave = stringToSave+'"'+emails[(len(emails)-1)]+'"]'+"\ndebugLogEnabled = "+str(debugLogEnabled)
    theLists.write(str(stringToSave))
    email.DI("Saved String: \n"+stringToSave)
  def loginSMTP():
    theirUsername = str(input("What is your Gmail account Email address? \n"))
    password = str(input("What is your Gmail password?\n"))
    email.DI("Debug Info: Username, "+  theirUsername+" Password, "+password)
    try: 
      s.login(str(theirUsername), str(password))
      login = 1
      cprint("\nDebug Info: Succesful you are now logged in and can send emails\n\n", "green")
      
    except:
      cprint("Debug Info: Login Failed \nReenter your credentials\n or turn on less secure app access in your gmail account settings\n\n", "red")
      login = 0
  def addEmail():
    nameInput = str(input("What is the Name you would like to add to the name list\n"))
    names.append(nameInput)
    emailInput = str(input("What is the email of the reciver\n"))
    emails.append(emailInput)
    email.save()
    email.DI("Added Email: "+emailInput+"Name: "+nameInput)
  
  def checkEmail():
    
    s.login(str(theirUsername), str(password))
    mail.list()
    # Out: list of "folders" aka labels in gmail.
    mail.select("inbox") # connect to inbox.
    
    #Get an email
    result, data = mail.uid('fetch', b'1', '(RFC822)')
    raw_email = data[0][1]
    email_message = email.message_from_bytes(raw_email)
    maintype = email_message.get_content_maintype()
    #HERE COMES TROUBLES - if hmtl will be base64 string
    if maintype == 'multipart':
      for part in email_message.get_payload():
        print(part.get_content_maintype())
        if part.get_content_maintype() == 'text':
          html = str(part.get_payload())
        elif maintype == 'text':
            html = str(email_message.get_payload())

        #Now I Can parse HTML
        if html is not None:
            soup = BeautifulSoup(html, 'html.parser')


            
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
  def reportBug():
    explainBug = input("Give us a brief overview of what happened and when it happened")
    email.DI("User submited a bug, info brief overview \n\n"+explainBug)
  def sendEmail():
    msg = MIMEMultipart()
    answer = str(input("This will send an email to all of these people \n"+str(names)+"\nAnd all these emails\n"+str(emails)+"\nWould you like to continue\nPress enter to continue and stop to return to main menu\n"))
    if answer == "":
      print("Continuing")
    else:
      email.DI("Failed to send email the user did not want to send to the list")
      return 0;
    subject = input("What Is The Subject Of Your Message \n")
    sendingName = input("What do you want your name to show as\n")
    html = input("Do you want to send html content(Y/N) \n")
    anyAttachments = input("Do you have any attachments you would like to add (Y/N)\n")
    if anyAttachments.lower() == "y":
      try:
        pathOfFile = input("What is the path or name of the file\n")
        files = open(pathOfFile, "r")
        email.mime.application.MIMEApplication(files.read(),_subtype="extension of file")
        attach.add_header('Content-Disposition','attachment',filename=pathOfFile)
        msg.attach(file)
      except:
        cprint("Failed","red")
        email.DI("Failed to attach message")
      index = 0
    if html.lower() == "y":
      htmlFile = str(input("Make sure the file is in the same folder as the .EXE or .PY file\nWhat is the name of the file\n"))
      htmlFileOpened = open(htmlFile,"r")
      htmlContent = htmlFileOpened.read()
      htmlFileOpened.close()
      msg['From']=sendingName+"<"+theirUsername+">"
      msg['To']="*[Name]*"
      msg['Subject']=subject
      msg.attach(MIMEText(htmlContent, "html"))
      text = msg.as_string()
      doContinue = input(text+"Would you like to confirm(Y/N)")
      if doContinue.lower() == "y":
        print("You chose to continue")
      else:
        return 0;
      for i in range(len(names)):
        index += 1
        if (index > 10):
          index = 0
          s.quit()
          try: 
            s.login(str(theirUsername), str(password))
            email.DI("Succesful you are now logged in and can send emails\n\n")
          except:
            return 0      
          email.DI("Login Failed \n\n")
        msg = Multipart()       # create a message
        # setup the parameters of the message
        msg['From']=sendingName+"<"+theirUsername+">"
        msg['To']=emails[i]
        msg['Subject']=subject
        msg.attach(MIMEText(htmlContent, "html"))
        text = msg.as_string()
        s.sendmail(theirUsername, emails[i], text)
        email.DI("\n\nSent, "+text)
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
      else:
        message = input("Message\nDear *[name]*,\n\n")
        nameOfSender = input("What is the name you would like at the end of your email?\n")
        title = input("What is your title (Dr. , Sir , Esquire)\n")
      msg['From']=sendingName+"<"+theirUsername+">"
      msg['To']="*[Name]*"
      msg['Subject']=subject
      msg.attach(MIMEText("Dear *[Name]*,\n\n"+str(message)+"\n\n"+signature, 'plain'))
      text = msg.as_string()
      doContinue = input(text+"Would you like to confirm(Y/N)")
      if doContinue.lower() == "y":
        print("You chose to continue")
      else:
        return 0;
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
        msg['From']=sendingName+"<"+theirUsername+">"
        msg['To']=emails[i]
        msg['Subject']=subject
        msg.attach(MIMEText("Dear "+names[i]+",\n\n"+str(message)+"\n\n"+signature, 'plain'))
        text = msg.as_string()
        s.sendmail(theirUsername, emails[i], text)
        print("\n\nSent, "+text)
        msg = ""
  def showMailingList():
    print("Emails in list:\n"+str(emails))
    print("Names in list:\n"+str(names))
    input("Press enter to continue...\n")
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
  def choose(interactionCounts):
    interactionCounts = 0
    inputString = "What do you want to do:\n\nAdd An Email from you sending list(A)\nRemove an email from you sending list(R)\nSend an Email(S)\nLogin or change accounts(L)\nSend debug info (D)\nCheck your email for the word unsubscribe and delete their names\nShow mailing list(M)\n"
    choice = input(inputString)
    email.DI("Interaction #"+str(interactionCounts)+" Choice of choice string "+choice)
    
    if choice.lower() ==  "python-backend-is-a-level-11-human":
      global debugLogEnabled
      debugLogEnabled = 1
      email.DI("Interaction #"+str(interactionCounts)+" Enabled debug info show")
      email.save()
      email.choose((interactionCounts+1))
    elif choice.lower() == "e":
      email.checkEmail()
      email.DI("Interaction #"+str(interactionCounst)+" Sending Debug Info!")
      email.choose((interactionCounts+1))
    elif choice.lower() == "d":
      email.DI("Interaction #"+str(interactionCounts)+" Sending Debug Info!")
      email.sendDebugInfo()
      email.choose((interactionCounts+1))
    elif choice.lower() == "a":
      email.DI("Interaction #"+str(interactionCounts)+" Adding Email")
      emailChoice = input("Do you want to upload a txt file with your contacts in it (a) or enter recivers manually(B)")
      if emailChoice.lower() == "b":
        email.DI("Interaction #"+str(interactionCounts)+" Manually Inputing emails")
        email.addEmail()
        email.choose((interactionCounts+1))
      elif emailChoice.lower() == "a":
        email.DI("Interaction #"+str(interactionCounts)+" Adding File")
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
        
            names.save(name)
        else:
          print("there was an error, try again")
    elif choice.lower() == "r":
      email.DI("Interaction #"+str(interactionCounts)+" Remove Email")
      email.removeEmail()
      email.choose((interactionCounts+1))
    elif choice.lower() == "s":
      email.DI("Interaction #"+str(interactionCounts)+" Sending Email")
      email.sendEmail()
      email.choose((interactionCounts+1))
    elif choice.lower() == "l":
      email.DI("Interaction #"+str(interactionCounts)+" Reloging in")
      email.loginSMTP()
      email.choose((interactionCounts+1))
    elif choice.lower() == "m":
      email.DI("Interaction #"+str(interactionCounts)+" showing mailing list")
      email.showMailingList()
      email.choose((interactionCounts+1))
    elif choice.lower() == "d":
      email.DI("Interaction #"+str(interactionCounts)+" send debug email")
      email.sendDebugInfo()
      email.choose((interactionCounts+1))
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
  debugLogEnabled = 0
  names = ["Alex", "Riley","Alex"]
  emails = ["adickhans@gmail.com","rilesdk@gmail.com","dickha.alexan27@svvsd.org"]
  email.save()

interactionCounts = 0
email.loginSMTP()
email.choose((interactionCounts+1))
