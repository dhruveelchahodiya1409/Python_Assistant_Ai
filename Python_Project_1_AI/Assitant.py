import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


# set up for speech recognition
engine = pyttsx3.init('sapi5')
voices  = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


# set up for speck audio
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("What Can i do For You")


# set up for voice input
def takeVoice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 200
        audio = r.listen(source)
    try:
        print("Recognition...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        print(e)
        print("Say That Again Please...")
        return "None"
    return query

# def sendEmail(to,content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('hgain4966@gmail.com','P@isa@143')
#     server.sendmail('hgain4966@gmail.com',to,content)
#     server.close()

if __name__ == '__main__':
    speak("Jay Shree Ram")
    # wishMe()
    loop = True
    while loop:
        query = takeVoice().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            # query = query.replace('wikipedia','')
            result = wikipedia.summary(query,sentences=2)
            speak("According To wikipedia")
            print(result)
            speak(result)
        elif 'open youtube' in query:
            webbrowser.open("Youtube.com")

        elif 'open google' in query:
            webbrowser.open("Google.com")

        elif 'open instagram' in query:
            webbrowser.open("Instagram.com")

        elif 'open facebook' in query:
            webbrowser.open("Facebook.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("Stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'E:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            srtTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(srtTime)
            speak(f"Sir,the Time is :{srtTime}")

        elif 'open pycharm' in query:
            path = "C:\\Program Files\\JetBrains\\PyCharm 2023.2.3\\bin\\pycharm64.exe"
            os.startfile(path)

        elif 'open chrome' in query:
            path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(path)

        elif 'open android studio' in query:
            path = "C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe"
            os.startfile(path)

        elif 'stop listening' in query or 'bye' in query or 'quit' in query:
            speak("Thank you For Using")
            exit()

        elif 'who are you' in query:
            print("I am AI")
            speak("I am AI")

        # elif 'send email' in query:
        #     try:
        #         speak("what should I say?")
        #         content = takeVoice()
        #         to = "pureskillstudent@gmail.com"
        #         sendEmail(to,content)
        #         speak("Email has been send..")
        #     except Exception as e:
        #         print(e)
        #         speak("i am not able to send Email")
