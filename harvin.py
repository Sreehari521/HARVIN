import webbrowser as wb

print("""                                                                                              
  _                      _       
 | |                    (_)      
 | |__   __ _ _ ____   ___ _ __  
 | '_ \ / _` | '__\ \ / / | '_ \ 
 | | | | (_| | |   \ V /| | | | |
 |_| |_|\__,_|_|    \_/ |_|_| |_|
                                 
                                 
""")
print("Hi, I am harvin. Your personal assistant chat-bot program.")
print("")
print("")

name = input("Name: ")
print("")
print(f'Hi, {name}. I am harvin. Your personal assistant chat-bot program.')
print("")

while True:
    res = input("Please enter your command: ")
    res = res.lower()
    
    if "hi" in res:
        print("")
        print("Hello Sir/Madam")
        print("")
    
    elif "hello" in res:
        print("")
        print("Hi Sir/Madam")
        print("")
    
    elif "good morning" in res:
        print("")
        print("Good Morning Sir/Madam. Have a nice day")
        print("")
    
    elif "good night" in res:
        print("")
        print("Good Night Sir/Madam. Have a nice nightmare")
        print("")
    
    elif "google" in res:
        print("")
        wb.open("https://www.google.com/")
        print("")
    
    elif "mail" in res:
        print("")
        wb.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
        print("")
    
    elif "github" in res:
        print("")
        wb.open("https://github.com")
        print("")
    
    elif "scratch" in res:
        print("")
        wb.open("https://scratch.mit.edu")
        print("")
    
    elif "twitter" in res:
        print("")
        wb.open("https://twitter.com")
        print("")
    
    elif "facebook" in res:
        print("")
        wb.open("https://facebook.com")
        print("")
    
    elif "instagram" in res:
        print("")
        wb.open("https://instagram.com")
        print("")
    
    elif "who are u" in res or "who are you" in res:
        print("")
        print("I am harvin. Your personal assistant chat-bot program.")
        print("")
    
    elif "who am i" in res or "who i am" in res:
        print("")
        print(f"You are {name}")
        print("")
    
    elif "what is your favorite color" in res or "what is your favorite colour" in res or "what's your favorite color" in res or "what's your favorite colour" in res:
        print("")
        print("My favourite color is Blue!")
        print("")
    
    elif "bye" in res or "goodbye" in res:
        print("")
        print(f"Ok {name} sir/madam. Thanks for using me!")
        print("")
    
    elif "how are u" in res or "how are you" in res:
        print("")
        print(f"I am fine {name} sir/madam.")
        print("")

    elif res == "":
        print("")
        print("Sir/Madam atleast type anything")
        print("")

    elif res == "br" or res == "break":
        print("")
        print("")
    
    else:
        print("")
        print("Sir/Madam I don't understand your command")
        print("")