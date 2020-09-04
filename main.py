# Libraries for secure email sending
import smtplib
import ssl

# Import MIME libraries for emails
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import mimetypes
import email.mime.application

# For inbox checking
import imaplib as mail
import email
mail = mail.IMAP4_SSL("imap.gmail.com")

# Safe(er) password input
import getpass

# Import BS4
from bs4 import BeautifulSoup

# TODO: #3 #2 #1 Add JSON support

# Create Dummy File to prevent opening errors
ThatFile = open("lists.py", "a")
ThatFile.close()

# Import email list
from lists import *

# Create ssl for security
context = ssl.create_default_context()

# Initiate email sending
s = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context)

# Instantiate username and password
username = ""
password = ""

# Instantiate name and username
name = ""
theirUsername = ""

# Instantiate number of times email.DI() was called
debugLogNum = 0

# Instantiate varable for removeName function
listLen = 0

# Bool to keep track of the users logged in state
login = 0 

# Counts how many times it has looped
interactionCounts = 0

class email:
  
  def DI(DebugLog):
    """Adds String to debug file

    Args:
        DebugLog (String): The string to log
    """    
    
    # Global to acces varables outside of function
    global debugLogEnabled, debugLogNum
    
    # If advanced debugging is on it will show in command line
    if(debugLogEnabled == 1):
      
      # increase times called
      debugLogNum += 1
      
      # Print to terminal
      print(str(debugLogNum) + ": Debug Info: "+DebugLog)
      
    else:
      
      # increase times called
      debugLogNum += 1
    
    # Append and save debug log
    debugFile = open("debug.log","a")
    debugFile.write("\nDebug Info: "+DebugLog)
    debugFile.close()
    
  def save():
    """Saves all files
    """
    
    # Debug log
    
    # Open lists
    theLists = open("lists.py", "w")
    
    # Create String
    stringToSave = 'names = ['
    for i in names:
      stringToSave = stringToSave+'"'+i+'",'
    
    stringToSave = stringToSave+'"'+names[(len(names)-1)]+'"]\nemails = ['
    
    # Add emails
    for i in range(len(emails)-1):
      stringToSave = stringToSave+'"'+emails[i]+'",'
    stringToSave = stringToSave+'"'+emails[(len(emails)-1)]+'"]'+"\ndebugLogEnabled = "+str(debugLogEnabled)
    theLists.write(str(stringToSave))
    email.DI("Saved String: \n"+stringToSave)
  def loginSMTP():
    """Promt user to log in
    """    
    
    # Promt user for username and password
    theirUsername = str(input("What is your Gmail account Email address? \n"))
    print("What is your Gmail password?\n")
    password = str(getpass.getpass())
    try: 
      s.login(str(theirUsername), str(password))
      login = 1
      print("\nDebug Info: Succesful you are now logged in and can send emails\n\n")
      
    except:
      print("Debug Info: Login Failed \nReenter your credentials\n or turn on less secure app access in your gmail account settings\n\n")
      login = 0
      
  def addEmail():
    """Add Email to the mailing list locally
    """
    
    # Ask for name input
    nameInput = str(input("What is the Name you would like to add to the name list\n"))
    names.append(nameInput)
    
    # ask for Email
    emailInput = str(input("What is the email of the reciver\n"))
    emails.append(emailInput)
    
    # Save file
    email.save()
    
    # Add to debug log
    email.DI("Added Email")
    
  def checkEmail():
    mail.login(str(theirUsername), str(password))
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
  def removeEmail(emailName):
    """Removes and email from the list

    Args:
        emailName (String): The name or email you want to remove
    """    
    
    # init varable to keep track of index
    listLen = 0
    
    # Try finding it in list
    try:
      listLen = names.index(emailName)
    except:
      # If it is not in names look in emails
      email.DI("Failed to find "+emailName+" in local name list, trying email")
      listLen = emails.index(emailName)
    
    # Pop that item in list from both names and emails
    emails.remove(emails[listLen])
    names.remove(names[listLen])
    
    # Save email list
    email.save()
    
  def userRemoveEmail():
    """Asks a user what email they want to remove
    """
    
    # Ask for input
    removeEmail(input("What is the name or email you want to remove.(Caps Sensitive)\n"))
    
  def reportBug():
    """Reports a but to the debug log
    """    
    
    explainBug = input("Give us a brief overview of what happened and when it happened")
    email.DI("User submited a bug, info brief overview \n\n"+explainBug)
    email.sendDebugInfo()
  def sendEmail():
    """Sends an email with user input

    Returns:
        int: failed or not
    """
    
    # Intsantiate a varable with the message 
    msg = MIMEMultipart()
    
    # Promt user
    answer = str(input("This will send an email to all of these people \n"+str(names)+"\nAnd all these emails\n"+str(emails)+"\nWould you like to continue\nPress enter to continue and stop to return to main menu\n"))
    
    if answer == "":
      print("Continuing")
    else:
      email.DI("Failed to send email the user did not want to send to the list")
      return 0
    
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
        msg.attach(files)
      except:
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
      index = 0
      if doContinue.lower() == "y":
        print("You chose to continue")
      else:
        return 0
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
      signature = title + nameOfSender
      msg.attach(MIMEText("Dear *[Name]*,\n\n"+str(message)+"\n\n"+signature, 'plain'))
      text = msg.as_string()
      doContinue = input(text+"Would you like to confirm(Y/N)")
      index = 0
      if doContinue.lower() == "y":
        print("You chose to continue")
      else:
        return 0
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
    """Shows everyone in the mailing list
    """
    
    # Adds all the emails in a better formtted list
    emailString = ""
    for i in emails:
      emailString += i + ", "
    
    # Adds all the names in a better formtted list
    nameString = ""
    for i in names:
      nameString += i + ", "
    
    #  Print it to console
    print("Emails in list:\n"+str(emailString))
    print("Names in list:\n"+str(nameString))
    input("Press enter to continue...\n")
  
  def sendDebugInfo():
    """Sends debug email from the default email
    """
       
    debugInfoRead = open("debug.txt","r")
    sendDebugInfo = debugInfoRead.read()
    debugInfoRead.close()
    msg = MIMEMultipart()
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
    """The function to get user input on which  function to call
    """
       
    global interactionCounts, debugLogEnabled
    
    # Increment interaction counts
    interactionCounts += 1
    
    # User choice
    inputString = "What do you want to do:\n\nAdd An Email from you sending list(A)\nRemove an email from you sending list(R)\nSend an Email(S)\nLogin or change accounts(L)\nSend debug info (D)\nCheck your email for the word unsubscribe and delete their names\nShow mailing list(M)\n"
    choice = input(inputString)
    
    # Add to debug log
    email.DI("Interaction #"+str(interactionCounts)+" Choice of choice string "+choice)
    
    if choice.lower() ==  "python-backend-is-a-level-11-human":
      # Turn on debug logging
      debugLogEnabled = 1
      email.DI("Interaction #"+str(interactionCounts)+" Enabled debug info show")
      email.save()
      email.choose()
    elif choice.lower() == "e":
      email.checkEmail()
      email.DI("Interaction #"+str(interactionCounts)+" Sending Debug Info!")
      email.choose()
    elif choice.lower() == "d":
      email.DI("Interaction #"+str(interactionCounts)+" Sending Debug Info!")
      email.sendDebugInfo()
      email.choose()
    elif choice.lower() == "a":
      email.DI("Interaction #"+str(interactionCounts)+" Adding Email")
      emailChoice = input("Do you want to upload a txt file with your contacts in it (a) or enter recivers manually(B)")
      if emailChoice.lower() == "b":
        email.DI("Interaction #"+str(interactionCounts)+" Manually Inputing emails")
        email.addEmail()
        email.choose()
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
      email.userRemoveEmail()
      email.choose()
    elif choice.lower() == "s":
      email.DI("Interaction #"+str(interactionCounts)+" Sending Email")
      email.sendEmail()
      email.choose()
    elif choice.lower() == "l":
      email.DI("Interaction #"+str(interactionCounts)+" Reloging in")
      email.loginSMTP()
      email.choose()
    elif choice.lower() == "m":
      email.DI("Interaction #"+str(interactionCounts)+" showing mailing list")
      email.showMailingList()
      email.choose()
    elif choice.lower() == "d":
      email.DI("Interaction #"+str(interactionCounts)+" send debug email")
      email.sendDebugInfo()
      email.choose()
    else:
      # Send Debug info if they allow it
      # TODO: #4 Ask for permision
      # email.sendDebugInfo()
      
      # null out values?
      theirUsername = ""
      password = ""

# Start program
if __name__ == "__main__":
  # Checking if info in lists works
  try:
    
    # If names varable exists
    if names[0] == names[0]:
      pass
      # Do nothing
    
  except:
    
    # Create default information
    debugLogEnabled = 0
    names = ["Devs"]
    emails = ["developers@hdprojects.dev"]
    email.save()
    
  interactionCounts = 0
  email.loginSMTP()
  email.choose()
