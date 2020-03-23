import smtplib
import ssl
ThatFile = open("lists.py", "a")
ThatFile.close()
from lists import *
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import poplib
from email import parser

username = ""
password = ""
interactionCounts = 0
name = ""
theirUsername = ""

listLen = 0
login = 0 

class email:
  interactionCount = 0
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
    answer = str(input("This will send an email to all of these people \n"+str(names)+"\nAnd all these emails\n"+str(emails)+"\nWould you like to continue\nPress enter to continue and stop to return to main menu\n"))
    if answer == "":
      print("Continuing")
    else:
      email.DI("Failed to send email the user did not want to send to the list")
      return 0;
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
  def showMailingList():
    print("Emails in list:\n"+str(emails))
    print("Names in list:\n"+str(names))
    input("Press enter to continue...\n")
  def checkMailbox():
    try:
      mail = imaplib.IMAP4_SSL(SMTP_SERVER)
      mail.login(FROM_EMAIL,FROM_PWD)
      mail.select('inbox')

      type, data = mail.search(None, 'ALL')
      mail_ids = data[0]

      id_list = mail_ids.split()   
      first_email_id = int(id_list[0])
      latest_email_id = int(id_list[-1])


      for i in range(latest_email_id,first_email_id, -1):
        typ, data = mail.fetch(i, '(RFC822)' )

        for response_part in data:
          if isinstance(response_part, tuple):
            msg = email.message_from_strin(response_part[1])
          email_subject = msg['subject']
          email_from = msg['from']
          print ('From : ' + email_from + '\n')
          print ('Subject : ' + email_subject +'\n')

   def choose(interactionCounts):
      inputString = "What do you want to do:\n\nAdd An Email from you sending list(A)\nRemove an email from you sending list(R)\nShow the mailing list(M)\nSend an Email(S)\nLogin or change accounts(L)\nSend debug info (D)\n Check your email (C)"
      choice = input(inputString)
      email.DI("Interaction #"+str(interactionCounts)+" Choice of choice string "+choice)
      if choice.lower() == "D":
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
    elif choice.lower() == "c":
      email.DI("Interaction #"+str(interactionCounts)+" check mailbox")
      email.checkMailbox()
      email.choose((interactionCounts+1))
    else:
      email.DI("Session Finished, all personal information deleting...\n\n\n\n")
      email.sendDebugInfo()
      theirUsername = ""
      password = ""
      print("All personal information has been deleted")


def search_string(uid_max, criteria):
    c = list(map(lambda t: (t[0], '"'+str(t[1])+'"'), criteria.items())) + [('UID', '%d:*' % (uid_max+1))]
    return '(%s)' % ' '.join(chain(*c))
    # Produce search string in IMAP format:
    #   e.g. (FROM "me@gmail.com" SUBJECT "abcde" BODY "123456789" UID 9999:*)


def get_first_text_block(msg):
    type = msg.get_content_maintype()

    if type == 'multipart':
        for part in msg.get_payload():
            if part.get_content_maintype() == 'text':
                return part.get_payload()
    elif type == 'text':
        return msg.get_payload()


server = imaplib.IMAP4_SSL(imap_ssl_host, imap_ssl_port)
server.login(username, password)
server.select('INBOX')

result, data = server.uid('search', None, search_string(uid_max, criteria))

uids = [int(s) for s in data[0].split()]
if uids:
    uid_max = max(uids)
    # Initialize `uid_max`. Any UID less than or equal to `uid_max` will be ignored subsequently.

server.logout()

try:
  if names[0] == names[0]:
    names = names
    emails = emails
except:
  names = ["Alex", "Riley","Alex"]
  emails = ["adickhans@gmail.com","rilesdk@gmail.com","dickha.alexan27@svvsd.org"]
  emails.save()

interactionCount = 0
email.loginSMTP()
email.choose((interactionCounts+1))