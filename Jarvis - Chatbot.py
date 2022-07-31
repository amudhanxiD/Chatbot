import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib

s = (random.randint(0,178))

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

wishMe()

speak("I am Jarvis and may i know your name please sir ?")
name=input("- My name is ")
query1 = "Hi , Mr."+ name +"What can i do for you!"
results1 = query1
print(results1)
speak(results1)

def ask():
    query = input("- ")
    return(query)

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 578)
    server.ehlo()
    server.starttls()
    server.login('gtk2027@gmail.com','Gtk@85368536')
    server.sendmail('arumaa07@gmail.com', to, content)
    server.close()
    return(to,content)


if __name__ == "__main__":
   
    #while True:
    if 1:
        
        query = ask()
        
        #logic on executing tasks based on query

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        if 'open youtube' in query:
            print("Opening youtube for you,sir...")
            speak("Opening youtube for you,sir...")
            webbrowser.open("youtube.com")

        elif 'google' in query:
            print("Opening google for you,sir...")
            speak("Opening google for you,sir...")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            print("Opening stackoverflow for you,sir...")
            speak("Opening stackoverflow for you,sir...")
            webbrowser.open("stackoverflow.com")

        elif 'music' in query:
            print("playing music for you,sir...")
            speak("playing music for you,sir...")
            music_dir = 'C:\\Users\\User\\Desktop\\my fav. songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[s]))

        elif 'the time' in query:
            print("showing the time for you,sir...")
            speak("showing the time for you,sir...")
            strTime =datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is{strTime}")
            print(strTime)

        elif 'open code' in query:
            codePath = ""
            os.startfile(codePath)

        elif 'email' in query:
            try:
                speak("what should i say")
                content = ask()
                to = "gtk2027@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry boss, i could not send your email now")
